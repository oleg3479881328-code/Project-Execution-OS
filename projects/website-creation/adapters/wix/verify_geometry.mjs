#!/usr/bin/env node
/* Read-only geometry QA using Wix's already-installed Playwright browser.
   Usage: node verify_geometry.mjs RECIPE.json PREVIEW_URL [1280,1920]
   Only LOCAL_GEOMETRY is assessed; this is not a publish operation.
*/
const fs=require('node:fs');
const [recipeFile,url,widthSpec='1280,1920']=process.argv.slice(2);
if(!recipeFile||!/^https?:\/\//.test(url||'')){
  console.error('Usage: node verify_geometry.mjs RECIPE.json PREVIEW_URL [1280,1920]');
  process.exit(2);
}
let pw;
try{pw=require('playwright')}
catch(e){try{pw=require('/usr/local/lib/node_modules/playwright')}
catch{console.error('BLOCKED: official Playwright runtime unavailable');process.exit(3)}}
const recipe=JSON.parse(fs.readFileSync(recipeFile,'utf8'));
if(recipe.schema!=='localdesign.wix-geometry-recipe.v1')throw Error('Invalid recipe');
const widths=widthSpec.split(',').map(Number);
(async()=>{
  const browser=await pw.chromium.launch({headless:true,args:['--no-sandbox']});
  const findings=[];
  try{
    for(const width of widths){
      const page=await browser.newPage({viewport:{width,height:911},deviceScaleFactor:1});
      const errors=[];
      page.on('pageerror',e=>errors.push(e.message));
      const response=await page.goto(url,{waitUntil:'domcontentloaded',timeout:45000});
      await page.waitForTimeout(1500);
      const observed=await page.evaluate(elements=>{
        const rect=el=>{
          const r=el.getBoundingClientRect();
          return {x:r.left,y:r.top,w:r.width,h:r.height};
        };
        const basename=url=>decodeURIComponent(new URL(url).pathname.split('/').at(-1)).toLowerCase();
        const normalize=s=>String(s||'').replace(/\s+/g,' ').trim();
        const rows=[];
        for(const item of elements){
          let element=null;let reason='';
          if(item.type==='image'){
            const name=basename(item.asset);
            const found=[...document.images].filter(x=>decodeURIComponent(x.currentSrc||x.src||'').toLowerCase().includes(name));
            if(found.length!==1)reason='image matches: '+found.length;
            else element=found[0].closest('wow-image')||found[0];
          }else if(item.type==='text'){
            const found=[...document.querySelectorAll('h1,h2,h3,h4,p,span,a')]
              .filter(x=>normalize(x.textContent)===normalize(item.text))
              .filter(x=>![...x.children].some(child=>normalize(child.textContent)===normalize(item.text)));
            if(found.length!==1)reason='text matches: '+found.length;
            else element=found[0].closest('div[id]')||found[0];
          }
          if(!element){rows.push({found:false,reason});continue}
          const section=element.closest('section');
          if(!section){rows.push({found:false,reason:'no section'});continue}
          const a=rect(element),b=rect(section);
          rows.push({found:true,elementId:element.id,
            frame:{centerX:a.x-b.x-b.w/2,y:a.y-b.y,w:a.w,h:a.h},
            sectionHeight:b.h});
        }
        return {rows,clientWidth:document.documentElement.clientWidth,scrollWidth:document.documentElement.scrollWidth};
      },recipe.elements);
      let pass=response.status()===200&&errors.length===0;
      const rows=[];
      for(let i=0;i<recipe.elements.length;i++){
        const item=recipe.elements[i],actual=observed.rows[i];
        const expected=width===390?item.mobile:item.desktop;
        if(!expected){rows.push({i,status:'NOT_MEASURED'});continue}
        if(!actual.found){rows.push({i,status:'MISSING',reason:actual.reason});pass=false;continue}
        const delta={};
        for(const key of Object.keys(expected)){
          const val=key==='x'?actual.frame.centerX+observed.clientWidth/2:actual.frame[key];
          delta[key]=Math.round((val-expected[key])*100)/100;
        }
        const ok=Object.values(delta).every(n=>Math.abs(n)<=1);
        if(!ok)pass=false;
        rows.push({i,type:item.type,id:actual.elementId,status:ok?'PASS':'FAIL',delta,frame:actual.frame});
      }
      findings.push({width,status:pass?'LOCAL_GEOMETRY_PASS':'LOCAL_GEOMETRY_FAIL',
        http:response.status(),clientWidth:observed.clientWidth,errors,rows});
      await page.close();
    }
  }finally{await browser.close()}
  console.log(JSON.stringify({schema:'localdesign.wix-geometry-qa.v1',
    source:recipe.source,viewports:findings},null,2));
  if(findings.some(x=>x.status!=='LOCAL_GEOMETRY_PASS'))process.exitCode=1;
})().catch(e=>{console.error('QA_BLOCKED:',e.message);process.exitCode=2});
