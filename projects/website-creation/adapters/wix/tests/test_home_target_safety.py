#!/usr/bin/env python3
"""Safety regression: explicit Wix Origami (home) page target only."""
import importlib.util
import os
import pathlib
import subprocess
import tempfile
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('wix_full_page_compiler',ROOT/'compile_full_page.py')
mod=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

class HomeTargetSafety(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root=pathlib.Path(self.temp.name)/'packages/site-app/src/pages/(home)'
        root.mkdir(parents=True)
        for name in ('structure.jsx','layout.css','style.css','unmapped.json'):
            (root/name).write_text('<Page id="c1dmp"><Section id="test" /></Page>' if name=='structure.jsx' else '{}')
        self.page=root

    def test_home_disallowed_by_default(self):
        with self.assertRaises(mod.Blocked):
            mod.get_page(self.temp.name,'(home)')
        self.assertEqual(mod.get_page(self.temp.name,'(home)',allow_home=True),self.page)

    def test_explicit_home_must_be_actual_folder(self):
        for bad in ('home','../(home)','/tmp/(home)','(home)/../(home)'):
            with self.assertRaises(mod.Blocked):
                mod.get_page(self.temp.name,bad,allow_home=True)

    def test_wrong_page_id_blocks_without_mutation(self):
        before=self.page.joinpath('structure.jsx').read_text()
        recipe={'schema':mod.PAGE,'unsupported':[],'sections':[{}],
                'desktopWidth':1920,'viewports':{'desktop-1920':{},'mobile-390':{}}}
        with self.assertRaisesRegex(mod.Blocked,'page ID mismatch'):
            mod.compile_page(recipe,self.temp.name,'(home)','wrong-page-id',
                             True,allow_home=True)
        self.assertEqual(self.page.joinpath('structure.jsx').read_text(),before)

    def test_unknown_source_objects_block_before_home_mutation(self):
        before=self.page.joinpath('structure.jsx').read_text()
        recipe={'schema':mod.PAGE,'unsupported':[{'reason':'SOURCE_OBJECT_NOT_MAPPED_TO_NATIVE'}],
                'sections':[{}]}
        with self.assertRaisesRegex(mod.Blocked,'Source unsupported'):
            mod.compile_page(recipe,self.temp.name,'(home)','c1dmp',True,allow_home=True)
        self.assertEqual(self.page.joinpath('structure.jsx').read_text(),before)

    def test_bash_runner_requires_distinct_exact_home_authorization(self):
        env=os.environ.copy()
        env.update({'WIX_MODE':'full-page','WIX_SITE_ID':'7969ecbf-2525-43fd-9493-5670c637f351',
           'FINGERPRINT_ZIP':'/nonexistent/fingerprint.zip','WIX_TARGET_PAGE':'(home)',
           'WIX_TARGET_PAGE_ID':'c1dmp','PREVIEW_URL':'https://example.invalid/',
           'APPROVED_REPLACE_PAGE':'YES'})
        runner=str(ROOT/'run_wix_pipeline.sh')
        for approvals in ({},{'APPROVED_REPLACE_HOME':'YES','WIX_HOME_APPROVED_SITE_ID':'wrong-site'}):
            subenv={**env,**approvals}
            for key in ('APPROVED_REPLACE_HOME','WIX_HOME_APPROVED_SITE_ID'):
                if key not in approvals:subenv.pop(key,None)
            done=subprocess.run(['bash',runner],env=subenv,capture_output=True,text=True)
            self.assertEqual(done.returncode,3)
            self.assertIn('Home requires',done.stderr)

if __name__=='__main__':
    unittest.main()
