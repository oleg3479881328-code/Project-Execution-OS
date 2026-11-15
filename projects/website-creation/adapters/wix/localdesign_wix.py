#!/usr/bin/env python3
"""LocalDesign v2.4 -> native Wix Studio Two (one-section pilot).
Use the official Wix Origami export/lint/import/readback route.
No authentication, publishing, URL downloads, or placeholder assets.
"""
import argparse
import html
import json
import re
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

class Blocked(Exception):
    pass

def n(x):
    x=round(float(x),2)
    return str(int(x)) if x.is_integer() else str(x)

def extract(path,section):
    with zipfile.ZipFile(path) as z:
        data=json.loads(z.read('site-fingerprint.json'))
    if data.get('schema')!='localdesign.site-fingerprint.v2.4':
        raise Blocked('Expected LocalDesign v2.4 Fingerprint')
    pages=data.get('pages',[])
    if len(pages)!=1: raise Blocked('One-page capture required for pilot')
    views=pages[0]['views']
    profiles={}
    for key in ('desktop-1280','mobile-390'):
        if views.get(key,{}).get('status')!='observed':
            raise Blocked('Missing observed '+key)
        d=views[key]['data']
        sec=next((x for x in d['nodes'] if x['selector']==section),None)
        if not sec:raise Blocked('Section missing '+key)
        profiles[key]=(sec,{x['selector']:x for x in d['nodes']},d['nodes'])
    sec,desktop,nodes=profiles['desktop-1280']
    mobile_sec,mobile,_=profiles['mobile-390']
    out=[]
    for node in nodes:
        sel=node['selector']
        if not sel.startswith(section+' > ') or not node.get('visible'):continue
        r=node['rect']
        if r['width']<1 or r['height']<1:continue
        typ=None;url=None;text=''
        if node['tag'] in ('h1','h2','h3','h4','p','span','a') and node.get('text','').strip():
            if any(x['selector'].startswith(sel+' >') and x.get('text') for x in nodes):continue
            typ='text';text=node['text'].strip()
        else:
            urls=node.get('assets') or (mobile.get(sel) or {}).get('assets') or []
            if urls:typ='image';url=urls[0]
        if not typ:continue
        mate=mobile.get(sel)
        mr=mate['rect'] if mate and mate.get('visible') else None
        out.append(dict(type=typ,selector=sel,tag=node['tag'],text=text,asset=url,
            desktop=dict(centerX=round(r['x']-sec['rect']['x']-sec['rect']['width']/2,2),
                         y=round(r['y']-sec['rect']['y'],2),w=r['width'],h=r['height']),
            mobile=(dict(x=round(mr['x']-mobile_sec['rect']['x'],2),
                         y=round(mr['y']-mobile_sec['rect']['y'],2),
                         w=mr['width'],h=mr['height']) if mr else None)))
    if not any(e['type']=='image' for e in out):raise Blocked('No exact image sources')
    if not any(e['type']=='text' for e in out):raise Blocked('No text found')
    return dict(schema='localdesign.wix-geometry-recipe.v1',source=data['source'],
                section=section,desktopHeight=sec['rect']['height'],
                mobileHeight=mobile_sec['rect']['height'],elements=out)

def cid(block):
    m=re.search(r'\bid="([^"]+)"',block)
    if not m:raise Blocked('Missing native component id')
    return m[1]

def existing_text(block):
    m=re.search(r"""html:\s*(['"])(.*?)\1""",block,re.S)
    return html.unescape(re.sub('<[^>]*>','',m[2])).strip() if m else ''

def media_name(block):
    m=re.search(r"wix:image://v1/[^/]+/([^#'\"]+)",block)
    if not m:raise Blocked('Existing Wix image has no official URL')
    return unquote(m[1]).lower()

def cssrule(ident,geo,mobile=False):
    xy=('margin-left: '+n(geo['x'])+'px;' if mobile else
        'margin-left: calc(50% '+('+' if geo['centerX']>=0 else '-')+
        ' '+n(abs(geo['centerX']))+'px);')
    return ('.'+ident+' {\n'
      '    --spx-ref-width: '+('390' if mobile else '1280')+';\n'
      '    --spx-resolver-type: fixed;\n'
      '    width: '+n(geo['w'])+'px;\n'
      '    height: '+n(geo['h'])+'px;\n'
      '    grid-row: 1 / 2;\n    grid-column: 1 / 2;\n'
      '    align-self: start;\n    justify-self: start;\n'
      '    position: relative;\n    '+xy+'\n'
      '    margin-top: '+n(geo['y'])+'px;\n'
      '    margin-bottom: 0px;\n    margin-right: 0px;\n}')

def replace_rule(css,ident,geo,mobile=False):
    anchor=css.find('@media (--variants-')
    if anchor<0:raise Blocked('Wix responsive media rule missing')
    start,end=(anchor,len(css)) if mobile else (0,anchor)
    frag=css[start:end]
    patt=r'(?m)^\s*\.'+re.escape(ident)+r'\s*\{[^{}]*\}'
    matches=list(re.finditer(patt,frag))
    if len(matches)>1:raise Blocked('Duplicate CSS component rule')
    rule=cssrule(ident,geo,mobile)
    if matches:
        match=matches[0]
        frag=frag[:match.start()]+'\n'+rule+frag[match.end():]
    elif mobile:
        pos=frag.rfind('}')
        if pos<0:raise Blocked('Invalid mobile media rule')
        frag=frag[:pos]+'\n'+rule+'\n'+frag[pos:]
    else:frag+='\n'+rule+'\n'
    return css[:start]+frag+css[end:]

def apply(recipe,root,page):
    if recipe.get('schema')!='localdesign.wix-geometry-recipe.v1':
        raise Blocked('Invalid normalized recipe')
    if not re.fullmatch(r'[a-z0-9-]+',page) or page=='home':
        raise Blocked('Pilot only permits explicit non-home page')
    folder=Path(root)/'packages/site-app/src/pages'/page
    paths=[folder/x for x in ('structure.jsx','layout.css','style.css')]
    if not all(x.is_file() for x in paths):raise Blocked('Export current site via official Wix Origami first')
    structure,layout,style=[x.read_text() for x in paths]
    if structure.count('<Section ')!=1 or structure.count('<InternalContainer')!=1:
        raise Blocked('One-section target required')
    imgs=re.findall(r'<Image\b[\s\S]*?\n\s*/>',structure)
    texts=re.findall(r'<WRichText\b[\s\S]*?\n\s*/>',structure)
    if not imgs or not texts:raise Blocked('Expected existing images and rich text')
    if len(recipe['elements'])>25:raise Blocked('Pilot capacity exceeded')
    existing=set();blocks=[];mapped=[]
    for i,e in enumerate(recipe['elements']):
        if e['type']=='image':
            filename=unquote(urlsplit(e['asset']).path.rsplit('/',1)[-1]).lower()
            opts=[b for b in imgs if media_name(b)==filename and cid(b) not in existing]
            if len(opts)!=1:
                raise Blocked('Wix Media Manager image missing/ambiguous: '+filename)
            block=opts[0]
        elif e['type']=='text':
            opts=[b for b in texts if existing_text(b)==e['text'] and cid(b) not in existing]
            if len(opts)>1:raise Blocked('Ambiguous text; cannot map safely')
            if opts:block=opts[0]
            else:
                ident='ld-auto-'+str(i+1).zfill(2)
                tag=e['tag'] if e['tag'] in ('p','h1','h2','h3','h4') else 'p'
                rich='<'+tag+'>'+html.escape(e['text'],quote=False)+'</'+tag+'>'
                block=('                <WRichText id="'+ident+'" className="'+ident+
                   '" richText={{ id: "data-'+ident+
                   '", type: "Builder.RichText", html: '+json.dumps(rich,ensure_ascii=False)+' }} />')
                style+='\n.'+ident+' { color: #443F3D; text-align:left; font:normal normal 400 15px/1.2 raleway-v2; }\n'
        else:raise Blocked('Unsupported native element: '+e['type'])
        ident=cid(block)
        if ident in existing:raise Blocked('Duplicated native ID')
        existing.add(ident);blocks.append(block);mapped.append((ident,e))
    wrapper=structure.index('<InternalContainer')
    begin=structure.find('\n            >',wrapper)
    if begin<0:raise Blocked('Cannot locate Wix InternalContainer child start')
    begin+=len('\n            >')
    end=structure.find('</InternalContainer>',begin)
    if end<0:raise Blocked('Cannot locate Wix InternalContainer end')
    old=structure[begin:end]
    extra=re.sub(r'<(?:Image|WRichText)\b[\s\S]*?/>(?=\s|$)','',old)
    if extra.strip():raise Blocked('Extra Wix child component present; no destructive replace')
    structure=structure[:begin]+'\n'+'\n'.join(blocks)+'\n            '+structure[end:]
    if not re.search(r'grid-template-rows:\s*minmax\('+re.escape(n(recipe['desktopHeight']))+r'px',layout):
        raise Blocked('Target section has different desktop height')
    for ident,e in mapped:
        layout=replace_rule(layout,ident,e['desktop'])
        if e.get('mobile'):layout=replace_rule(layout,ident,e['mobile'],True)
    for path,data in zip(paths,(structure,layout,style)):path.write_text(data)
    return dict(page=page,elements=len(mapped),
                images=sum(e['type']=='image' for _,e in mapped),
                text=sum(e['type']=='text' for _,e in mapped),
                status='WORKSPACE_PATCH_ONLY_NEEDS_OFFICIAL_WIX_IMPORT_AND_QA')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest='cmd',required=True)
    x=sub.add_parser('extract');x.add_argument('--fingerprint',required=True)
    x.add_argument('--section',required=True);x.add_argument('--out',required=True)
    x=sub.add_parser('apply');x.add_argument('--recipe',required=True)
    x.add_argument('--wix-export',required=True);x.add_argument('--page',required=True)
    a=p.parse_args()
    try:
        if a.cmd=='extract':
            result=extract(a.fingerprint,a.section)
            Path(a.out).write_text(json.dumps(result,ensure_ascii=False,indent=2))
            print(json.dumps({'elements':len(result['elements']),'recipe':a.out}))
        else:
            result=apply(json.loads(Path(a.recipe).read_text()),a.wix_export,a.page)
            print(json.dumps(result,ensure_ascii=False))
    except (Blocked,KeyError,ValueError,zipfile.BadZipFile) as e:
        print('BLOCKED:',str(e),file=__import__('sys').stderr)
        raise SystemExit(2)
