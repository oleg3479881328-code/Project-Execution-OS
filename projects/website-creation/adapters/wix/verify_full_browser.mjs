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
const desktopWidth=recipe.desktopWidth||1280;
if(![1280,1920].includes(desktopWidth)||!recipe.viewports?.['desktop-'+desktopWidth]?.viewport||!recipe.viewports?.['mobile-390']?.viewport)throw Error('Missing observed target viewports');
if(recipe.schema!=='localdesign.wix-page-recipe.v1')throw Error('Wrong recipe schema');
const target=process.env.WIX_TARGET_PAGE;
if(!target)throw Error('Set WIX_TARGET_PAGE');
const structure=fs.readFileSync(path.join(exportRoot,'packages/site-app/src/pages',target,'structure.jsx'),'utf8');
const sections=[...structure.matchAll(/<Section\s+id="([^"]+)"[\s\S]*?<\/Section>/g)];
if(sections.length!==recipe.sections.length)throw Error('Section coverage mismatch '+sections.length+'/'+recipe.sections.length);
const mappings=recipe.sections.map((section,i)=>{
 const found=[...sections[i][0].matchAll(/<(Image|SvgImage|WRichText)\b([\s\S]*?)\/>/g)];
 if(found.length!==section.elements.length)throw Error('Section '+i+' element coverage mismatch');
 const bkg=sections[i][0].match(/<Background\s+id="([^"]+)"/);
 const videoId=sections[i][0].match(/wix:video:\/\/v1\/([A-Za-z0-9_-]+)\//);
 return {wixId:sections[i][1],backgroundId:bkg?.[1]||null,videoMediaId:videoId?.[1]||null,items:found.map((m,j)=>{
  const id=m[2].match(/\bid="([^"]+)"/);if(!id)throw Error('Native element ID missing');
  const uri=m[2].match(/\buri:\s*['"]([^'"]+)['"]/);
  const vector=m[2].match(/wix:image:\/\/v1\/([^'"]+\.svg)/);
  return {wixId:id[1],source:section.elements[j],nativeType:m[1],
    mediaUri:m[1]==='Image'?uri?.[1]||null:
      m[1]==='SvgImage'?vector?.[1]||null:null};
 })};
});
const round=n=>Math.round(n*100)/100;
(async()=>{
 fs.mkdirSync(shotDir,{recursive:true});
 const browser=await pw.chromium.launch({headless:true,args:['--no-sandbox']});
 const views=[];
 try{
  for(const [label,width] of [['desktop-'+desktopWidth,desktopWidth],['mobile-390',390]]){
   const page=await browser.newPage({viewport:{width,height:recipe.viewports[label].viewport.height},deviceScaleFactor:recipe.viewports[label].viewport.dpr||1});
   const errors=[];page.on('pageerror',e=>errors.push(e.message));
   const response=await page.goto(url,{waitUntil:'domcontentloaded',timeout:45000});
   await page.waitForTimeout(1500);
   // Wix wow-image lazy-loads below-fold sources. A missing currentSrc
   // before scrolling is NOT an asset failure; load each captured source
   // image using the actual browser before the native DOM/asset QA.
   for (const group of mappings) {
    for (const item of group.items) {
     const expected=item.source[label==='mobile-390'?'mobile':'desktop'];
     if (item.source.type!=='image'||item.nativeType==='SvgImage'||!expected) continue;
     const frame=page.locator('[id="'+item.wixId+'"]');
     if (await frame.count()!==1) continue;
     try {
      await frame.scrollIntoViewIfNeeded({timeout:8000});
      await page.waitForFunction(id=>{
       const img=document.getElementById(id)?.querySelector('img');
       return Boolean(img?.currentSrc&&img.naturalWidth>0);
      },item.wixId,{timeout:11000});
     } catch { /* The asset gate below records missing/broken images. */ }
    }
   }
   // Source background video is lazy in native Wix. Verify playback
   // WHILE the section is visible: Wix intentionally pauses offscreen video.
   // A pause after returning to page top is not an autoplay failure.
   const videoWhenVisible={};
   for(const [si,group] of mappings.entries()){
    const dynamic=recipe.sections[si].dynamicLayers||[];
    if(!dynamic.length)continue;
    const sec=page.locator('[id="'+group.wixId+'"]');
    try{
     await sec.scrollIntoViewIfNeeded({timeout:8000});
     const active=dynamic[0]?.[label==='mobile-390'?'mobile':'desktop'];
     if(active){
      await page.waitForFunction(id=>{
       const v=document.getElementById(id)?.querySelector('video');
       return Boolean(v&&v.readyState>=2&&v.videoWidth>0);
      },group.backgroundId,{timeout:16000});
      await page.waitForTimeout(500);
      videoWhenVisible[group.backgroundId]=await page.evaluate(id=>{
       const v=document.getElementById(id)?.querySelector('video');
       return v?{paused:v.paused,readyState:v.readyState,muted:v.muted,
          loop:v.loop,autoplay:v.autoplay,currentTime:v.currentTime}:null;
      },group.backgroundId);
     }
    }catch{ /* precise dynamic gate below marks the failure */ }
   }
   await page.evaluate(()=>window.scrollTo(0,0));
   await page.waitForTimeout(300);
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
       imageURL:img?.currentSrc||img?.src||null,vectorPresent:!!el.querySelector('svg'),
       naturalImageWidth:img?.naturalWidth||0});
     }
     const bkg=g.backgroundId?document.getElementById(g.backgroundId):null;
     const video=bkg?.querySelector('video')||null;
     const mediaLayer=bkg?.querySelector('[data-motion-part^="BG_MEDIA"]');
     const videoData={present:!!video,url:video?.currentSrc||null,readyState:video?.readyState||0,
       videoWidth:video?.videoWidth||0,muted:video?.muted,loop:video?.loop,autoplay:video?.autoplay,
       paused:video?.paused,mediaOpacity:Number(getComputedStyle(mediaLayer||bkg).opacity),
       sourceId:g.videoMediaId||null};
     rows.push({missing:false,section:s,items,video:videoData});
    }
    return {rows,clientWidth:document.documentElement.clientWidth,
     bannerHeight:document.getElementById('WIX_ADS')?.getBoundingClientRect().height||0};
   },mappings);
   let localPass=response?.status()===200&&errors.length===0,pagePass=true,assetsPass=true,dynamicPass=true;
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
    const dynamics=sec.dynamicLayers||[];
    if(dynamics.length){
     if(dynamics.length!==1||dynamics[0].type!=='video')dynamicPass=false;
     else{
      const expectedVideo=dynamics[0][bp];
      const actual=act.video||{};
      if(!actual.present||!actual.sourceId||!actual.url||!actual.url.includes(actual.sourceId)){
       dynamicPass=false;
      }else if(expectedVideo){
       if(actual.readyState<2||!actual.videoWidth||
          !videoWhenVisible[group.backgroundId]||
          videoWhenVisible[group.backgroundId].paused||
          actual.muted!==Boolean(expectedVideo.muted)||
          actual.loop!==Boolean(expectedVideo.loop)||
          actual.autoplay!==Boolean(expectedVideo.autoplay)||
          Math.abs(actual.mediaOpacity-Number(expectedVideo.opacity))>.015)dynamicPass=false;
      }else if(Math.abs(actual.mediaOpacity)>0.015)dynamicPass=false;
     }
    }
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
      // Wix serves some media (notably GIFs) by internal ID without the
      // original filename. The readback verifier independently checked
      // the source filename, so compare the actual Wix Media URI here.
      const mediaUri=mappings[i].items[j].mediaUri;
      if(mappings[i].items[j].nativeType==='SvgImage'){
       if(!mediaUri||(!got.vectorPresent&&
         !(got.imageURL&&decodeURIComponent(got.imageURL).includes(mediaUri))))assetsPass=false;
      }else if(!mediaUri||!got.imageURL||
         !decodeURIComponent(got.imageURL).includes(mediaUri)||
         !got.naturalImageWidth)assetsPass=false;
     }
     items.push({j,delta});
    }
    details.push({section:sec.sourceSelector,sectionHeightDelta:round(hdiff),items,
      ...(dynamics.length?{videoObserved:act.video,
        videoWhenVisible:videoWhenVisible[mappings[i].backgroundId]||null,
        videoSource:dynamics[0]}:{})});
   }
   const screenshot=path.join(shotDir,label+'.png');
   await page.screenshot({path:screenshot,fullPage:true});
   views.push({label,width,http:response?.status(),clientWidth:results.clientWidth,
    platformBannerPx:results.bannerHeight,localGeometry:localPass?'PASS':'FAIL',
    pageGeometry:pagePass?'PASS':'FAIL',assets:assetsPass?'PASS':'FAIL',
    dynamicMedia:dynamicPass?'PASS':'FAIL',
    errors,details,screenshot,visual:'NOT_ASSESSED',interactions:'NOT_ASSESSED'});
   await page.close();
  }
 }finally{await browser.close()}
 const pass=views.every(v=>v.localGeometry==='PASS'&&v.pageGeometry==='PASS'&&v.assets==='PASS'&&v.dynamicMedia==='PASS');
 console.log(JSON.stringify({schema:'localdesign.wix-full-browser-qa.v1',source:recipe.source,url,
  status:pass?'GEOMETRY_ASSETS_PASS':'BROWSER_QA_FAIL',views,
  visualPixelParity:'NOT_ASSESSED',published:false},null,2));
 if(!pass)process.exitCode=1;
})().catch(e=>{console.error('BLOCKED:',e.message);process.exitCode=2});
