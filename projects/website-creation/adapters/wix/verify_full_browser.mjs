#!/usr/bin/env node
/* Read-only Playwright browser QA for native Wix full-page adapter.
   node verify_full_browser.mjs RECIPE.json PREVIEW_URL READBACK_EXPORT_DIR SCREENSHOTS_DIR
*/
import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const [recipePath,url,exportRoot,shotDir]=process.argv.slice(2);
if(!recipePath||!/^https?:\/\//.test(url||'')||!exportRoot||!shotDir){
 console.error('Usage: node verify_full_browser.mjs RECIPE.json PREVIEW_URL READBACK_EXPORT_DIR SCREENSHOTS_DIR');process.exit(2);
}
let pw;
try{pw=require('playwright')}catch{try{pw=require('/usr/local/lib/node_modules/playwright')}catch{console.error('BLOCKED: Playwright unavailable');process.exit(2)}}
const recipe=JSON.parse(fs.readFileSync(recipePath,'utf8'));
if(recipe.schema!=='localdesign.wix-page-recipe.v1')throw Error('Wrong recipe schema');
const target=process.env.WIX_TARGET_PAGE;
if(!target)throw Error('Set WIX_TARGET_PAGE');
const structure=fs.readFileSync(path.join(exportRoot,'packages/site-app/src/pages',target,'structure.jsx'),'utf8');
const sections=[...structure.matchAll(/<Section\s+id="([^"]+)"[\s\S]*?<\/Section>/g)];
if(sections.length!==recipe.sections.length)throw Error('Section coverage mismatch '+sections.length+'/'+recipe.sections.length);
const mappings=recipe.sections.map((section,i)=>{
 const found=[...sections[i][0].matchAll(/<(Image|WRichText)\b([\s\S]*?)\/>/g)];
 if(found.length!==section.elements.length)throw Error('Section '+i+' element coverage mismatch');
 return {wixId:sections[i][1],items:found.map((m,j)=>{
  const id=m[2].match(/\bid="([^"]+)"/);if(!id)throw Error('Native element ID missing');
  return {wixId:id[1],source:section.elements[j]};
 })};
});
const round=n=>Math.round(n*100)/100;
(async()=>{
 fs.mkdirSync(shotDir,{recursive:true});
 const browser=await pw.chromium.launch({headless:true,args:['--no-sandbox']});
 const views=[];
 try{
  for(const [label,width] of [['desktop-1280',1280],['mobile-390',390]]){
   const page=await browser.newPage({viewport:{width,height:911},deviceScaleFactor:1});
   const errors=[];page.on('pageerror',e=>errors.push(e.message));
   const response=await page.goto(url,{waitUntil:'domcontentloaded',timeout:45000});
   await page.waitForTimeout(1500);
   const results=await page.evaluate(groups=>{
    const rect=el=>{const x=el.getBoundingClientRect();return {x:x.left,y:x.top,w:x.width,h:x.height}};
    const rows=[];
    for(const g of groups){
     const sec=document.getElementById(g.wixId);
     if(!sec){rows.push({missing:true,items:[]});continue}
     const s=rect(sec),items=[];
     for(const it of g.items){
      const el=document.getElementById(it.wixId);
      if(!el){items.push({missing:true});continue}
      const e=rect(el),cs=getComputedStyle(el),img=el.querySelector('img');
      items.push({missing:false,visible:cs.visibility!=='hidden'&&e.w>.1&&e.h>.1,
       local:{centerX:e.x-s.x-s.w/2,x:e.x-s.x,y:e.y-s.y,w:e.w,h:e.h},
       imageURL:img?.currentSrc||img?.src||null});
     }
     rows.push({missing:false,section:s,items});
    }
    return {rows,clientWidth:document.documentElement.clientWidth,
     bannerHeight:document.getElementById('WIX_ADS')?.getBoundingClientRect().height||0};
   },mappings);
   let localPass=response?.status()===200&&errors.length===0,pagePass=true,assetsPass=true;
   let previousBottom=null;const details=[];
   for(let i=0;i<recipe.sections.length;i++){
    const sec=recipe.sections[i],act=results.rows[i],bp=width===390?'mobile':'desktop';
    if(act.missing){localPass=false;pagePass=false;details.push({section:sec.sourceSelector,error:'missing'});continue}
    const expectedHeight=sec[bp==='desktop'?'desktopSection':'mobileSection'].height;
    const hdiff=act.section.h-expectedHeight;
    if(Math.abs(hdiff)>1)pagePass=false;
    if(previousBottom!==null&&Math.abs(act.section.y-previousBottom)>1)pagePass=false;
    previousBottom=act.section.y+act.section.h;
    const items=[];
    for(let j=0;j<sec.elements.length;j++){
     const e=sec.elements[j],got=act.items[j],expected=e[bp];
     if(!expected){if(got?.visible){localPass=false;items.push({j,error:'should be hidden'})}continue}
     if(!got||got.missing||!got.visible){localPass=false;items.push({j,error:'missing or hidden'});continue}
     const delta={};
     for(const k of ['y','w','h',bp==='desktop'?'centerX':'x']){
      delta[k]=round(got.local[k]-expected[k]);
      if(Math.abs(delta[k])>1)localPass=false;
     }
     if(e.type==='image'){
      const basename=decodeURIComponent(new URL(e.asset).pathname.split('/').pop()).toLowerCase();
      if(!got.imageURL||!got.imageURL.toLowerCase().includes(basename))assetsPass=false;
     }
     items.push({j,delta});
    }
    details.push({section:sec.sourceSelector,sectionHeightDelta:round(hdiff),items});
   }
   const screenshot=path.join(shotDir,label+'.png');
   await page.screenshot({path:screenshot,fullPage:true});
   views.push({label,width,http:response?.status(),clientWidth:results.clientWidth,
    platformBannerPx:results.bannerHeight,localGeometry:localPass?'PASS':'FAIL',
    pageGeometry:pagePass?'PASS':'FAIL',assets:assetsPass?'PASS':'FAIL',
    errors,details,screenshot,visual:'NOT_ASSESSED',interactions:'NOT_ASSESSED'});
   await page.close();
  }
 }finally{await browser.close()}
 const pass=views.every(v=>v.localGeometry==='PASS'&&v.pageGeometry==='PASS'&&v.assets==='PASS');
 console.log(JSON.stringify({schema:'localdesign.wix-full-browser-qa.v1',source:recipe.source,url,
  status:pass?'GEOMETRY_ASSETS_PASS':'BROWSER_QA_FAIL',views,
  visualPixelParity:'NOT_ASSESSED',published:false},null,2));
 if(!pass)process.exitCode=1;
})().catch(e=>{console.error('BLOCKED:',e.message);process.exitCode=2});
