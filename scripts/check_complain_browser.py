#!/usr/bin/env python3
"""Exercise the complete guide, notes and discovery pages in Chromium."""
import json
from pathlib import Path
import subprocess
import time
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / 'docs/complain-guide'
server = subprocess.Popen(['python3', '-m', 'http.server', '8765', '--bind', '127.0.0.1'], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    time.sleep(1)
    checked = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for theme in ('light', 'dark'):
            for width in (320, 390, 1280):
                page = browser.new_page(viewport={'width': width, 'height': 900}, color_scheme=theme)
                for route in ('complain/', 'complain/notes.html', 'complain/kmk.html', 'practical-guides/', 'practical-guides/methods.html'):
                    response = page.goto('http://127.0.0.1:8765/' + route, wait_until='networkidle')
                    assert response.status == 200, (route, response.status)
                    assert page.locator('h1').count() == 1, route
                    assert page.locator('main').count() == 1, route
                    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 1'), (route, width, theme, 'overflow')
                    page.keyboard.press('Tab')
                    assert page.locator(':focus').get_attribute('href') == '#main-content', route
                    page.keyboard.press('Enter')
                    assert page.evaluate('location.hash') == '#main-content', route
                    checked.append({'route': route, 'width': width, 'theme': theme, 'http': 200, 'no_horizontal_overflow': True, 'skip_link': True})
                page.close()
        page = browser.new_page(viewport={'width': 390, 'height': 844})
        page.goto('http://127.0.0.1:8765/complain/')
        page.locator('.pg-toc summary').click()
        assert page.locator('.pg-toc').get_attribute('open') is not None
        for n in range(1, 14):
            page.locator(f'#r{n}').click()
            assert page.evaluate('location.pathname + location.hash') == f'/complain/notes.html#n{n}'
            page.locator(f'a[href="index.html#r{n}"]').click()
            assert page.evaluate('location.pathname + location.hash') == f'/complain/index.html#r{n}'
        page.goto('http://127.0.0.1:8765/practical-guides/')
        assert page.locator('.pg-card').count() == 5
        page.get_by_role('link', name='Read the complete Complain or Constrain? guide', exact=True).click()
        assert page.evaluate('location.pathname') == '/complain/'
        page.screenshot(path='/tmp/complain-mobile.png', full_page=True)
        page.set_viewport_size({'width': 1280, 'height': 900})
        page.screenshot(path='/tmp/complain-desktop.png', full_page=True)
        browser.close()
    report = {'render_checks': checked, 'guide_note_round_trips': 13, 'contents_menu': True, 'collection_navigation': True, 'screenshot_manual_review': False}
    (EVIDENCE / 'BROWSER-CHECK-2026-11-02.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'browser_checks': len(checked), 'citation_round_trips': 13, 'result': 'PASS'}))
finally:
    server.terminate()
    server.wait(timeout=10)
