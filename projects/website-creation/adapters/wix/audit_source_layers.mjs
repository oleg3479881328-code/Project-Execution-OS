#!/usr/bin/env node
/* Read-only completeness gate for the EXISTING LocalDesign -> Wix pipeline.
 * Audit the donor itself BEFORE touching the Wix target.
 * This is NOT a second scanner: it finds source media that the v2.4
 * fingerprint/recipe might have silently dropped.
 *
 * node audit_source_layers.mjs RECIPE.json OUTPUT.json
 */
import fs from 'node:fs';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const [recipeFile,reportFile]=process.argv.slice(2);
if(!recipeFile||!reportFile){
 console.error('Usage: node audit_source_layers.mjs RECIPE.json OUTPUT.json');process.exit(2);
}
const recipe=JSON.parse(fs.readFileSync(recipeFile,'utf8'));
if(recipe.schema!=='localdesign.wix-page-recipe.v1'||!/^https?:\/\//.test(recipe.source)){
 throw Error('Invalid source recipe');
}
let pw;
try{pw=require('playwright')}catch{
 try{pw=require('/usr/local/lib/node_modules/playwright')}
 catch{console.error('BLOCKED: Existing Playwright not available');process.exit(2)}
}
const normalizedUrl=value=>{
 if(!value)return null;
 try{return new URL(value,recipe.source).href}catch{return null}
};
(async()=>{
 const browser=await pw.chromium.launch({headless:true,args:['--no-sandbox']});
 const views=[];
 try{
  for(const [view,width,height] of [['desktop-1280',1280,911],['mobile-390',390,844]]){
   const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
   const response=await page.goto(recipe.source,{waitUntil:'domcontentloaded',timeout:45000});
   if(!response||response.status()!==200)throw Error('Donor unavailable: '+view+' '+response?.status());
   await page.evaluate(async()=>{
    for(let y=0;y<document.documentElement.scrollHeight;y+=Math.max(400,window.innerHeight*.7)){
     window.scrollTo(0,y);
     await new Promise(resolve=>setTimeout(resolve,70));
    }
    window.scrollTo(0,0);
   });
   await page.waitForTimeout(700);
   const source=await page.evaluate(sectionSelectors=>{
    const entries=[];
    for(const selector of sectionSelectors){
     const section=document.querySelector(selector);
     if(!section){entries.push({section:selector,error:'SOURCE_SECTION_MISSING'});continue}
     const candidates=[...section.querySelectorAll('video,iframe,canvas')];
     for(const el of candidates){
      const tag=el.tagName.toLowerCase(),computed=getComputedStyle(el),host=el.parentElement;
      const hostStyle=host?getComputedStyle(host):null;
      const sourceEl=tag==='video'?el.querySelector('source[src]'):null;
      const src=tag==='video'?(el.currentSrc||el.getAttribute('src')||sourceEl?.getAttribute('src')):el.getAttribute('src');
      const r=el.getBoundingClientRect(),s=section.getBoundingClientRect();
      // Include offscreen oversized cover videos if their clipping parent
      // overlaps the source section; this is common in Showit backgrounds.
      const visibleThroughParent=host&&host.getBoundingClientRect().width>1&&host.getBoundingClientRect().height>1;
      if(r.width<1&&r.height<1&&!visibleThroughParent)continue;
      entries.push({
       section:selector,kind:tag,src:src||null,poster:el.getAttribute('poster')||null,
       fallbackPoster:sourceEl?.getAttribute('onerror')||null,
       autoplay:tag==='video'?el.autoplay:null,loop:tag==='video'?el.loop:null,
       muted:tag==='video'?el.muted:null,controls:tag==='video'?el.controls:null,
       objectFit:computed.objectFit,opacity:computed.opacity,
       layerOpacity:hostStyle?.opacity??null,
       rect:{x:r.x-s.x,y:r.y-s.y,w:r.width,h:r.height},
       clippingParent:hostStyle?.overflow??null,
      });
     }
    }
    return entries;
   },recipe.sections.map(s=>s.sourceSelector));
   for(const entry of source){
    if(entry.src)entry.src=normalizedUrl(entry.src);
    if(entry.poster)entry.poster=normalizedUrl(entry.poster);
   }
   views.push({view,http:response.status(),layers:source});
   await page.close();
  }
 }finally{await browser.close()}
 const missing=[],observed=[];
 for(const view of views)for(const layer of view.layers){
  if(layer.error){missing.push({...layer,view:view.view});continue}
  observed.push({...layer,view:view.view});
  const section=recipe.sections.find(s=>s.sourceSelector===layer.section);
  const declared=[
   ...(section?.elements||[]).filter(e=>e.type===layer.kind||e.type==='video'||e.type==='iframe'||e.type==='canvas'),
   ...(section?.dynamicLayers||[]),
  ];
  if(!layer.src||!declared.some(e=>normalizedUrl(e.asset||e.src||e.url)===layer.src)){
   missing.push({...layer,view:view.view,reason:'DYNAMIC_LAYER_NOT_IN_FINGERPRINT_RECIPE'});
  }
 }
 const result={schema:'localdesign.source-dynamic-layer-audit.v1',source:recipe.source,
  status:missing.length?'BLOCKED_MISSING_SOURCE_LAYERS':'SOURCE_DYNAMIC_LAYERS_COVERED',
  observed:observed.length,missing,views};
 fs.writeFileSync(reportFile,JSON.stringify(result,null,2));
 console.log(JSON.stringify({status:result.status,observed:result.observed,missing:missing.length,
  missingDetails:missing.slice(0,12),report:reportFile}));
 if(missing.length)process.exitCode=3;
})().catch(e=>{console.error('BLOCKED_SOURCE_LAYER_AUDIT:',e.message);process.exitCode=2});
