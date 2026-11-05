#!/usr/bin/env python3
"""Check the reconciled draft locally, including the GitHub Pages project prefix."""
import functools
import json
import os
import shutil
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PREFIX = '/How-to-Hear-a-Bully/'
class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if not self.path.startswith(PREFIX):
            self.send_error(404)
            return
        self.path = '/' + self.path[len(PREFIX):]
        super().do_GET()
    def log_message(self, *args):
        pass

def main():
    server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Handler, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f'http://127.0.0.1:{server.server_port}' + PREFIX
    routes = ('', 'notes.html', 'crisis/', 'crisis/notes.html', 'trust/', 'trust/notes.html',
              'trust/clara-tan.html', 'trust/clara-tan-sources.html', 'complain/',
              'complain/notes.html', 'complain/kmk.html', 'practical-guides/',
              'practical-guides/methods.html', 'pra-release-tracker.html')
    checked, errors, failed = [], [], []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=os.environ.get('H2HAB_CHROMIUM') or shutil.which('chromium'), args=['--no-sandbox'])
            for theme in ('light', 'dark'):
                for width in (320, 390, 1280):
                    page = browser.new_page(viewport={'width': width, 'height': 900}, color_scheme=theme)
                    page.on('pageerror', lambda e: errors.append(str(e)))
                    page.on('requestfailed', lambda r: failed.append(r.url))
                    for route in routes:
                        response = page.goto(base + route, wait_until='networkidle')
                        assert response.status == 200, (route, response.status)
                        assert page.locator('h1').count() == 1, route
                        assert page.locator('main').count() == 1, route
                        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'), (route, width, theme, 'overflow')
                        if route.startswith(('trust/', 'complain/', 'practical-guides/')):
                            page.keyboard.press('Tab')
                            assert page.locator(':focus').get_attribute('href') == '#main-content', route
                            page.keyboard.press('Enter')
                            assert page.evaluate('location.hash') == '#main-content'
                        checked.append({'route': route or '/', 'width': width, 'theme': theme})
                        if route in ('trust/clara-tan.html', 'trust/clara-tan-sources.html', 'practical-guides/', 'practical-guides/methods.html') and width in (390, 1280):
                            name = (route.strip('/') or 'index').replace('/', '-').replace('.html', '')
                            page.screenshot(path=f'/tmp/h2hab-{name}-{width}-{theme}.png', full_page=True)
                    page.close()
            page = browser.new_page(viewport={'width': 390, 'height': 844})
            for section, count in (('crisis', 9), ('trust', 7), ('complain', 13)):
                page.goto(base + section + '/')
                page.locator('.pg-toc summary').click()
                assert page.locator('.pg-toc').get_attribute('open') is not None
                for n in range(1, count + 1):
                    page.locator(f'#r{n}').click()
                    assert page.evaluate('location.pathname + location.hash') == PREFIX + f'{section}/notes.html#n{n}'
                    page.locator(f'a[href="index.html#r{n}"]').click()
                    assert page.evaluate('location.pathname + location.hash') == PREFIX + f'{section}/index.html#r{n}'
            page.goto(base + 'practical-guides/')
            assert page.locator('.pg-card').count() == 5
            page.get_by_role('link', name='Read the complete Complain or Constrain? guide', exact=True).click()
            assert page.evaluate('location.pathname') == PREFIX + 'complain/'
            page.goto(base + 'practical-guides/')
            page.locator('main a[href$="trust/clara-tan.html"]').click()
            assert page.evaluate('location.pathname') == PREFIX + 'trust/clara-tan.html'
            page.locator('.pg-endlinks a[href="clara-tan-sources.html"]').click()
            assert page.evaluate('location.pathname') == PREFIX + 'trust/clara-tan-sources.html'
            page.locator('.pg-endlinks a[href="clara-tan.html"]').click()
            assert page.evaluate('location.pathname') == PREFIX + 'trust/clara-tan.html'
            assert not errors and not failed, (errors, failed)
            browser.close()
        report = {'result': 'PASS', 'render_checks': checked, 'citation_round_trips': 29,
                  'collection_cards': 5, 'case_source_round_trip': True, 'project_prefix': PREFIX,
                  'page_errors': errors, 'failed_requests': failed,
                  'scope': 'Local draft only; no deployment or source currency verification'}
        (ROOT / 'docs/trust-guide/cases/INTEGRATION-BROWSER-2026-11-04.json').write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps({'render_checks': len(checked), 'citation_round_trips': 29, 'result': 'PASS'}))
    finally:
        server.shutdown()
        server.server_close()

if __name__ == '__main__':
    main()
