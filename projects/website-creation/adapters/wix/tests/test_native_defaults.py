#!/usr/bin/env python3
"""Owner native Wix defaults: missing fonts/effects continue, real blockers stop."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("wix_native_defaults", ROOT/"apply_wix_native_defaults.py")
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class NativeDefaultsTests(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root=Path(temp.name)
        page=self.root/"packages/site-app/src/pages/(home)"
        theme=self.root/"packages/site-app/src/global/themes"
        page.mkdir(parents=True)
        theme.mkdir(parents=True)
        (theme/"theme.css").write_text("""
        :root {
         --wst-heading-1-font: normal normal 400 --spx(80)/1.14em georgia;
         --wst-heading-2-font: normal normal 400 --spx(74)/1.14em georgia;
         --wst-paragraph-1-font: normal normal 400 --spx(23)/1.14em arial;
        }
        """)
        (page/"structure.jsx").write_text(
            '<Page id="c1dmp"><WRichText id="ldv-e000-000"/></Page>')
        (page/"style.css").write_text("""
        .ldv-e000-000 { font-family:"Made Canvas Light"; font-size:100px; color:#fff; }
        @media (--variants-mqxfr2bo1) {
         .ldv-e000-000 { font-family:"Tenderness"; font-size:60px; color:#fff; }
        }
        """)
        self.recipe={
            "schema":mod.SCHEMA,"source":"https://example.org",
            "desktopWidth":1920,"unsupported":[],
            "sections":[{
                "sourceSelector":"div#hero",
                "elements":[{"sourceSelector":"div#hero > h1","type":"text",
                             "tag":"h1","text":"Hello",
                             "desktopStyle":{"fontFamily":"Made Canvas Light"},
                             "mobileStyle":{"fontFamily":"Tenderness"},
                             "desktop":{"x":120,"y":100,"w":500,"h":100},
                             "mobile":{"x":20,"y":50,"w":300,"h":60}}]
            }]
        }
        self.views={
            "desktop-1920":{"data":{"nodes":[{"selector":"div#hero > h1",
                "styles":{"animationName":"fadeIn","transform":"none"}}]}},
            "mobile-390":{"data":{"nodes":[{"selector":"div#hero > h1",
                "styles":{"filter":"blur(1px)"}}]}}
        }
        self.source={"source":"https://example.org"}
        self.cssfile=page/"style.css"

    def call(self):
        with patch.object(mod, "read_zip",return_value=(self.source,self.views)):
            return mod.apply_native_defaults(
                self.recipe,"source.zip",self.root,"(home)")

    def test_missing_fonts_use_native_theme_and_keep_exact_metrics(self):
        before=self.cssfile.read_text()
        result=self.call()
        after=self.cssfile.read_text()
        self.assertNotIn('Made Canvas Light',after)
        self.assertNotIn('Tenderness',after)
        self.assertEqual(after.count("font-family:georgia"),2)
        self.assertIn("font-size:100px",after)
        self.assertIn("font-size:60px",after)
        self.assertIn("color:#fff",after)
        self.assertEqual(result["sourceVisualParity"],"PARTIAL")
        self.assertEqual(len([x for x in result["nativeDefaults"]
            if x["reason"]=="ORIGINAL_FONT_NOT_IN_WIX_SITE_THEME"]),2)
        self.assertTrue((self.root.parent/"home-wix-native-defaults-report.json").is_file())
        self.assertEqual(result["remainingMandatoryBlockers"],0)
        self.assertNotEqual(before,after)

    def test_unsupported_effects_report_static_default_without_stop(self):
        r=self.call()
        effects=[x for x in r["nativeDefaults"]
                 if x["reason"]=="UNSUPPORTED_VISUAL_EFFECT_NATIVE_STATIC"]
        self.assertEqual({x["original"]["property"] for x in effects},
                         {"animationName","filter"})
        self.assertTrue(all(x["nativeBehavior"]=="WIX_STATIC_DEFAULT" for x in effects))

    def test_original_font_from_wix_theme_not_replaced(self):
        self.recipe["sections"][0]["elements"][0]["desktopStyle"]["fontFamily"]="georgia"
        self.recipe["sections"][0]["elements"][0]["mobileStyle"]["fontFamily"]="georgia"
        self.cssfile.write_text(self.cssfile.read_text().replace(
            '"Made Canvas Light"','georgia').replace('"Tenderness"','georgia'))
        result=self.call()
        self.assertFalse(any(x["reason"]=="ORIGINAL_FONT_NOT_IN_WIX_SITE_THEME"
                         for x in result["nativeDefaults"]))

    def test_true_source_blocker_never_downgraded(self):
        before=self.cssfile.read_text()
        self.recipe["unsupported"]=[{"selector":"div#hero > img",
                                    "reason":"SOURCE_OBJECT_NOT_MAPPED_TO_NATIVE"}]
        with self.assertRaisesRegex(mod.NativeDefaultsBlocked,
                                   "Mandatory source-native mappings"):
            self.call()
        self.assertEqual(self.cssfile.read_text(),before)

    def test_missing_or_wrong_wix_target_fails_closed(self):
        before=self.cssfile.read_text()
        with patch.object(mod,"read_zip",return_value=(self.source,self.views)):
            with self.assertRaises(mod.NativeDefaultsBlocked):
                mod.apply_native_defaults(self.recipe,"source.zip",self.root,"home")
        self.source["source"]="https://another.example"
        with self.assertRaises(mod.NativeDefaultsBlocked):
            self.call()
        self.assertEqual(before,self.cssfile.read_text())

    def test_css_provenance_mismatch_blocks_without_mutation(self):
        self.cssfile.write_text(self.cssfile.read_text().replace(
            '"Made Canvas Light"','georgia'))
        before=self.cssfile.read_text()
        with self.assertRaisesRegex(mod.NativeDefaultsBlocked,
                                   "Original font provenance"):
            self.call()
        self.assertEqual(before,self.cssfile.read_text())


if __name__=='__main__':
    unittest.main()
