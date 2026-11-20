"""Regression: measured source Footer cannot be clipped by zero-height Wix page grid."""
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('wix_native_compiler',ROOT/'compile_full_page.py')
compiler=importlib.util.module_from_spec(spec)
spec.loader.exec_module(compiler)


class FooterGridFlow(unittest.TestCase):
    def source(self):
        return {'sourceChrome':{
            'desktop-1920':[{'role':'footer','rect':{'height':700}}],
            'mobile-390':[{'role':'footer','rect':{'height':789.75}}]
        }}

    def test_original_desktop_mobile_measurements(self):
        self.assertEqual(compiler.measured_footer_height(self.source(),'desktop-1920'),700)
        self.assertEqual(compiler.measured_footer_height(self.source(),'mobile-390'),789.75)

    def test_native_grid_never_zero_with_captured_footer(self):
        css='.home { grid-template-rows: 0px 10px 0px; }\n.footer { grid-row: 3 / 4; }'
        desktop=compiler.update_page_grid(css,'home','footer',[911,1251],
             footer_height=compiler.measured_footer_height(self.source(),'desktop-1920'))
        mobile=compiler.update_page_grid(css,'home','footer',[509.44,1039.59],
             footer_height=compiler.measured_footer_height(self.source(),'mobile-390'))
        self.assertIn('0px 911px 1251px 700px',desktop)
        self.assertIn('0px 509.44px 1039.59px 789.75px',mobile)
        self.assertIn('grid-row: 4 / 5',desktop)

    def test_missing_or_duplicate_or_zero_footer_blocks(self):
        for rows in ([],[{'role':'footer','rect':{'height':0}}],
                     [{'role':'footer','rect':{'height':700}},
                      {'role':'footer','rect':{'height':700}}]):
            source=self.source();source['sourceChrome']['desktop-1920']=rows
            with self.assertRaises(compiler.Blocked):
                compiler.measured_footer_height(source,'desktop-1920')
        with self.assertRaises(compiler.Blocked):
            compiler.measured_footer_height(self.source(),'desktop-1280')
        with self.assertRaises(compiler.Blocked):
            compiler.update_page_grid('.p { grid-template-rows:0px; }','.p','f',[100],footer_height=0)

if __name__=='__main__':
    unittest.main()
