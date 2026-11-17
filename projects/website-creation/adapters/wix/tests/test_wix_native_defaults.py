#!/usr/bin/env python3
"""Existing PEOS Wix native default regression: editable text, no hidden source drops."""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
spec=importlib.util.spec_from_file_location('peos_native_defaults',ROOT/'apply_wix_native_defaults.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class NativeWixDefaults(unittest.TestCase):
    def setUp(self):
        tmp=tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root=Path(tmp.name)
        self.site=self.root/'export'
        self.page=self.site/'packages/site-app/src/pages/blank-2'
        self.page.mkdir(parents=True)
        self.theme=self.site/'packages/site-app/src/global/themes'
        self.theme.mkdir(parents=True)
        (self.theme/'theme.css').write_text(
            '--wst-heading-1-font: normal normal 400 --spx(30)/1.14em georgia;\n'
            '--wst-paragraph-1-font: normal normal 400 --spx(23)/1.14em arial;\n')
        self.source_selector='div#intro > p'
        self.struct='<Page id="test"><WRichText id="ldv-e000-000" className="ldv-e000-000" /></Page>'
        (self.page/'structure.jsx').write_text(self.struct)
        self.original_css=(
            '.ldv-e000-000 { font-family:"Made Canvas Light"; font-size:48px; color:rgb(1,2,3); }\n'
            '@media (--variants-viewport390) {\n'
            '.ldv-e000-000 { font-family:"Made Canvas Light"; font-size:20px; color:rgb(4,5,6); }\n}\n')
        (self.page/'style.css').write_text(self.original_css)
        (self.page/'layout.css').write_text(
            '.ldv-e000-000 { width:500px; height:500px; margin-left:120px; margin-top:340px; }\n')
        self.source='https://example.org/source'
        nodes=[{'selector':self.source_selector,'tag':'p','styles':{'animationName':'fadeUp',
            'filter':'none','transform':'none'},'rect':{'x':120,'y':340,'width':500,'height':500},
            'visible':True,'text':'ORIGINAL','assets':[]}]
        self.zipfile=self.root/'source.zip'
        with ZipFile(self.zipfile,'w') as z:
            z.writestr('site-fingerprint.json',json.dumps({
                'schema':'localdesign.site-fingerprint.v2.4','source':self.source,
                'pages':[{'views':{view:{'status':'observed','data':{'nodes':nodes,
                     'viewport':{'width':width,'height':900}}}
                     for view,width in [('desktop-1920',1920),('mobile-390',390)]}}]}))
        self.recipe={'schema':'localdesign.wix-page-recipe.v1','source':self.source,
            'desktopWidth':1920,'sourceObjectCoverage':{'mandatoryObjects':3},
            'sections':[{'sourceSelector':'div#intro','elements':[{
                'sourceSelector':self.source_selector,'type':'text','tag':'h1',
                'desktopStyle':{'fontFamily':'"Made Canvas Light"'},
                'mobileStyle':{'fontFamily':'"Made Canvas Light"'}}]}],
            'unsupported':[{'selector':'div#footer','reason':'DONOR_FOOTER_NATIVE_MAPPING_REQUIRED'},
                           {'selector':'svg#icon','reason':'SOURCE_OBJECT_NOT_MAPPED_TO_NATIVE'}]}

    def test_strict_path_does_not_modify_css_on_unmapped_source(self):
        with self.assertRaisesRegex(mod.NativeDefaultsBlocked,'partial-native-draft'):
            mod.apply_native_defaults(self.recipe,self.zipfile,self.site,'blank-2')
        self.assertEqual((self.page/'style.css').read_text(),self.original_css)

    def test_default_theme_retains_geometry_and_all_manual_rows(self):
        before_structure=(self.page/'structure.jsx').read_bytes()
        before_layout=(self.page/'layout.css').read_bytes()
        report=mod.apply_native_defaults(self.recipe,self.zipfile,self.site,'blank-2',
                                         allow_partial_draft=True)
        css=(self.page/'style.css').read_text()
        self.assertEqual(css.count('font-family:georgia'),2)
        self.assertNotIn('Made Canvas Light',css)
        self.assertIn('font-size:48px',css)
        self.assertIn('font-size:20px',css)
        self.assertEqual(before_structure,(self.page/'structure.jsx').read_bytes())
        self.assertEqual(before_layout,(self.page/'layout.css').read_bytes())
        self.assertEqual(report['remainingMandatoryBlockers'],2)
        self.assertEqual(report['sourceUnmapped'],self.recipe['unsupported'])
        self.assertEqual(report['nativeBuildStatus'],'DRAFT_WITH_UNMAPPED_SOURCE')
        self.assertEqual(report['sourceVisualParity'],'PARTIAL')
        self.assertEqual(report['sourceObjectCoverage']['mandatoryObjects'],3)
        self.assertEqual(report['nativeDefaultCount'],4) # 2 fonts + 2 observed animations
        self.assertEqual(sum(x['reason']=='UNSUPPORTED_VISUAL_EFFECT_NATIVE_STATIC'
                             for x in report['nativeDefaults']),2)

    def test_missing_original_font_does_not_block_mapped_source(self):
        self.recipe['unsupported']=[]
        report=mod.apply_native_defaults(self.recipe,self.zipfile,self.site,'blank-2')
        self.assertEqual(report['remainingMandatoryBlockers'],0)
        self.assertEqual(report['nativeBuildStatus'],'PASS_WITH_WIX_DEFAULTS')
        self.assertEqual(report['sourceVisualParity'],'PARTIAL')

    def test_invalid_target_and_mismatched_fingerprint_still_block(self):
        with self.assertRaises(mod.NativeDefaultsBlocked):
            mod.apply_native_defaults(self.recipe,self.zipfile,self.site,'home',
                                      allow_partial_draft=True)
        self.recipe['source']='https://other.example.org'
        with self.assertRaisesRegex(mod.NativeDefaultsBlocked,'source mismatch'):
            mod.apply_native_defaults(self.recipe,self.zipfile,self.site,'blank-2',
                                      allow_partial_draft=True)
        self.assertEqual((self.page/'style.css').read_text(),self.original_css)

if __name__=='__main__':
    unittest.main()
