#!/usr/bin/env python3
"""No-Wix regression tests for the existing LocalDesign full-page normalizer.

Run: python3 -m unittest discover -s projects/website-creation/adapters/wix/tests -v
Optional real owner ZIP regression:
  LOCALDESIGN_VESPER_ZIP=/path/to/site.zip python3 -m unittest discover ...
"""
import importlib.util
import os
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("full_page_recipe",ROOT/"full_page_recipe.py")
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def node(selector,tag="div",text="",assets=None,x=0,y=0,w=1265,h=100,
         visible=True,background="rgba(0, 0, 0, 0)"):
    return {"selector":selector,"tag":tag,"text":text,"assets":assets or [],
            "visible":visible,"rect":{"x":x,"y":y,"width":w,"height":h},
            "styles":{"backgroundColor":background,"backgroundImage":"none",
                      "position":"static","fontSize":"16px","color":"rgb(1, 2, 3)"}}

def fixture():
    # Footer gallery is a detached *sibling* root, not a descendant of footer.
    desktop=[
      node("div#root",y=0,h=2500),
      node("div#alpha",y=0,h=500),
      node("div#alpha > div:nth-of-type(1)",y=0,h=500,background="rgb(247, 245, 242)"),
      node("div#alpha > p",tag="p",text="Example",x=100,y=80,w=200,h=30),
      node("div#beta",y=500,h=500),
      node("div#beta > div > img",tag="img",assets=["https://example.org/bio.jpg"],
           x=200,y=530,w=200,h=250),
      node("div#footer_0",x=0,y=700,w=1265,h=300),
      node("div#footer_0 > div > img",tag="img",assets=["https://example.org/gallery.jpg"],
           x=650,y=750,w=200,h=210),
    ]
    mobile=[
      node("div#root",y=0,w=390,h=1300),
      node("div#alpha",y=0,w=390,h=650),
      node("div#alpha > div:nth-of-type(1)",y=0,w=390,h=650,background="rgb(247, 245, 242)"),
      node("div#alpha > p",tag="p",text="Example",x=10,y=60,w=250,h=45),
      node("div#beta",y=650,w=390,h=650),
      node("div#beta > div > img",tag="img",assets=["https://example.org/bio.jpg"],
           x=20,y=700,w=150,h=200),
      node("div#footer_0",x=0,y=950,w=390,h=350),
      node("div#footer_0 > div > img",tag="img",assets=["https://example.org/gallery.jpg"],
           x=30,y=960,w=180,h=200)
    ]
    views={
      "desktop-1280":{"status":"observed","data":{"viewport":{"width":1280,"height":911},
                     "nodes":desktop}},
      "mobile-390":{"status":"observed","data":{"viewport":{"width":390,"height":844},
                     "nodes":mobile}}
    }
    return {"schema":mod.CAPTURE,"source":"https://example.org/about",
            "pages":[{"views":views}]}, views

class FullPageNormalizerTests(unittest.TestCase):
    def test_detached_gallery_and_real_painted_background(self):
        fp,views=fixture()
        output=mod.normalize(fp,views,None)
        self.assertEqual([s["sourceSelector"] for s in output["sections"]],
                         ["div#alpha","div#beta"])
        alpha,beta=output["sections"]
        self.assertEqual(alpha["desktopBackground"]["status"],"OBSERVED")
        self.assertIn("gallery.jpg",[e["asset"].split("/")[-1] for e in beta["elements"]
                                    if e["type"]=="image"])
        self.assertEqual(len(beta["attachedVisualLayers"]),1)
        self.assertEqual(output["unsupported"],[])
    def test_mobile_independent_geometry(self):
        fp,views=fixture()
        output=mod.normalize(fp,views,None)
        text=next(e for e in output["sections"][0]["elements"] if e["type"]=="text")
        self.assertAlmostEqual(text["desktop"]["centerX"],100-1265/2)
        self.assertEqual(text["desktop"]["y"],80)
        self.assertEqual(text["mobile"]["x"],10)
        self.assertEqual(text["mobile"]["y"],60)
        self.assertEqual(text["mobile"]["w"],250)
    def test_duplicate_desktop_selector_fails_closed(self):
        fp,views=fixture()
        views["desktop-1280"]["data"]["nodes"].append(views["desktop-1280"]["data"]["nodes"][0])
        with self.assertRaises(mod.Blocked):
            mod.normalize(fp,views,None)
    def test_exact_source_asset_ambiguity_is_not_silently_replaced(self):
        fp,views=fixture()
        target=views["desktop-1280"]["data"]["nodes"][5]
        target["assets"].append("https://example.org/other.jpg")
        result=mod.normalize(fp,views,None)
        self.assertTrue(any("multiple source asset" in e["reason"] for e in result["unsupported"]))

    def test_nested_background_is_not_its_own_section(self):
        fp,views=fixture()
        parent=views["desktop-1280"]["data"]["nodes"][1]
        bg=node("div#alpha_canvas-background-photo",y=0,h=500)
        bg["relations"]={"parentSelector":"div#alpha"}
        views["desktop-1280"]["data"]["nodes"].insert(2,bg)
        recipe=mod.normalize(fp,views,None)
        self.assertEqual([s["sourceSelector"] for s in recipe["sections"]],
                         ["div#alpha","div#beta"])

    def test_visible_video_inherits_mp4_from_invisible_source_child(self):
        fp,views=fixture()
        video=node("div#beta > video",tag="video",x=0,y=550,w=1265,h=300)
        video["styles"]["objectFit"]="cover"
        video["imageEvidence"]={"autoplay":True,"loop":True,"muted":True}
        src=node("div#beta > video > source",tag="source",
                 assets=["https://example.org/real.mp4"],x=0,y=0,w=0,h=0,
                 visible=False)
        views["desktop-1280"]["data"]["nodes"].extend([video,src])
        recipe=mod.normalize(fp,views,None)
        layer=recipe["sections"][1]["dynamicLayers"][0]
        self.assertEqual(layer["sourceUrl"],"https://example.org/real.mp4")
        self.assertTrue(layer["desktop"]["autoplay"])
        self.assertTrue(layer["desktop"]["loop"])
        self.assertTrue(layer["desktop"]["muted"])
        self.assertIsNone(layer["mobile"])
        self.assertFalse(any(e["asset"]=="https://example.org/real.mp4"
                             for s in recipe["sections"] for e in s["elements"]))

    def test_origami_source_contract_candidate_validation(self):
        fp,views=fixture()
        fp["_origamiSourceContract"]={"schema":"localdesign.origami-source-contract.v1",
            "pages":[{"byViewport":{
                "desktop-1280":{"sectionCandidates":[
                    {"sourceSelector":"div#alpha"},{"sourceSelector":"div#beta"}],
                    "measuredNodes":len(views["desktop-1280"]["data"]["nodes"])},
                "mobile-390":{"sectionCandidates":[],
                    "measuredNodes":len(views["mobile-390"]["data"]["nodes"])}}}]}
        recipe=mod.normalize(fp,views,None)
        self.assertEqual([s["sourceSelector"] for s in recipe["sections"]],
                         ["div#alpha","div#beta"])
        self.assertTrue(any(x["reason"]=="SOURCE_OBJECT_LEDGER_MISSING_RECAPTURE_V2_5_4"
                            for x in recipe["unsupported"]))
        fp["_origamiSourceContract"]["pages"][0]["byViewport"]["desktop-1280"]["sectionCandidates"].append({"sourceSelector":"div#missing"})
        with self.assertRaises(mod.Blocked):
            mod.normalize(fp,views,None)

    def test_strict_object_ledger_unmapped_link_vector_fail_closed(self):
        fp,views=fixture()
        width=lambda view:len(views[view]["data"]["nodes"])
        ledger=[]
        for view in ("desktop-1280","mobile-390"):
            for name in ("div#alpha > p","div#beta > div > img",
                         "div#footer_0 > div > img"):
                ledger.append({"view":view,"sourceSelector":name,
                   "ownerKind":"flow-section",
                   "status":"SOURCE_CAPTURED_TARGET_MAPPING_REQUIRED",
                   "reason":None,"href":None})
        contract={"schema":"localdesign.origami-source-contract.v1",
          "pages":[{"byViewport":{
            "desktop-1280":{"sectionCandidates":[
              {"sourceSelector":"div#alpha"},{"sourceSelector":"div#beta"}],
              "measuredNodes":width("desktop-1280")},
            "mobile-390":{"sectionCandidates":[],
              "measuredNodes":width("mobile-390")}},
            "objectLedger":ledger,"coverage":{"mandatoryObjects":len(ledger)}}]}
        fp["_origamiSourceContract"]=contract
        clean=mod.normalize(fp,views,None)
        self.assertEqual(clean["unsupported"],[])
        self.assertEqual(clean["sourceObjectCoverage"]["mandatoryObjects"],6)
        # A native text element without a verified target link remains blocked.
        ledger[0]["href"]="https://example.org/contact"
        links=mod.normalize(fp,views,None)
        self.assertTrue(any(x["reason"]=="NATIVE_LINK_MAPPING_UNVERIFIED"
                            for x in links["unsupported"]))
        ledger[0]["href"]=None
        # Original SVG does not prove native Wix SvgImage upload/readback.
        svg=node("div#alpha > svg",tag="svg",x=10,y=25,w=40,h=35)
        views["desktop-1280"]["data"]["nodes"].append(svg)
        contract["pages"][0]["byViewport"]["desktop-1280"]["measuredNodes"]=width("desktop-1280")
        ledger.append({"view":"desktop-1280","sourceSelector":"div#alpha > svg",
           "ownerKind":"flow-section","status":"BLOCKED_TARGET_CAPABILITY",
           "reason":"SVG_NATIVE_VECTORART_UPLOAD_REQUIRED","href":None})
        contract["pages"][0]["coverage"]["mandatoryObjects"]=len(ledger)
        blocked=mod.normalize(fp,views,None)
        reasons={x["reason"] for x in blocked["unsupported"]}
        self.assertIn("SVG_NATIVE_VECTORART_UPLOAD_REQUIRED",reasons)
        self.assertIn("SOURCE_OBJECT_NOT_MAPPED_TO_NATIVE",reasons)

    def test_donor_navigation_and_overlay_are_not_silently_omitted(self):
        fp,views=fixture()
        ledger=[]
        contract={"schema":"localdesign.origami-source-contract.v1",
          "pages":[{"byViewport":{
            "desktop-1280":{"sectionCandidates":[{"sourceSelector":"div#alpha"},
                             {"sourceSelector":"div#beta"}],
                             "measuredNodes":len(views["desktop-1280"]["data"]["nodes"]),
                             "navigationCandidates":[{"sourceSelector":"div#menu"}],
                             "overlayCandidates":[{"sourceSelector":"div#sticky-banner"}]},
            "mobile-390":{"sectionCandidates":[],
                          "measuredNodes":len(views["mobile-390"]["data"]["nodes"]),
                          "navigationCandidates":[{"sourceSelector":"div#mobile-menu"}]}},
            "objectLedger":ledger,"coverage":{"mandatoryObjects":0}}]}
        fp["_origamiSourceContract"]=contract
        recipe=mod.normalize(fp,views,None)
        blockers={(x.get("selector"),x["reason"]) for x in recipe["unsupported"]}
        self.assertIn(("div#menu","DONOR_NAVIGATION_NATIVE_MAPPING_REQUIRED"),blockers)
        self.assertIn(("div#mobile-menu","DONOR_NAVIGATION_NATIVE_MAPPING_REQUIRED"),blockers)
        self.assertIn(("div#sticky-banner","DONOR_OVERLAY_NATIVE_MAPPING_REQUIRED"),blockers)
        self.assertNotEqual(recipe["acceptance"],"WIX_IMPORTED")

    @unittest.skipUnless(os.getenv("LOCALDESIGN_VESPER_ZIP"),
                         "set LOCALDESIGN_VESPER_ZIP to rerun actual owner-file regression")
    def test_actual_vesper_bio_missing_asset_regression(self):
        fp,views=mod.read_zip(os.environ["LOCALDESIGN_VESPER_ZIP"])
        recipe=mod.normalize(fp,views,None)
        images=[e["asset"].split("/")[-1] for s in recipe["sections"]
                for e in s["elements"] if e["type"]=="image"]
        self.assertIn("pexels-olya-kobruseva-4551044.jpg",images)
        self.assertGreaterEqual(len(images),18)
        self.assertGreaterEqual(len(recipe["sections"]),11)

if __name__=="__main__":
    unittest.main()
