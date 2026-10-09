/* Optional QA: Node + Playwright. No browser dependency is shipped to readers. */
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const base = process.argv[2] || 'http://localhost:8775/';
const output = process.env.QA_OUT;

(async () => {
  const browser = await chromium.launch({ headless: true, ...(process.env.QA_BROWSER_PATH ? {executablePath:process.env.QA_BROWSER_PATH} : {}) });
  const results = [];
  try {
    for (const width of [320,390,1280]) for (const colorScheme of ['light','dark']) {
      const context = await browser.newContext({ viewport:{width,height:900},colorScheme });
      const page = await context.newPage();
      const errors=[];
      page.on('pageerror', error => errors.push(error.message));
      page.on('response', response => { if (response.status()>=400 && !response.url().endsWith('favicon.ico')) errors.push(response.status()+' '+response.url()); });
      for (const route of ['changes/','changes/timeline.html','changes/methodology.html','practical-guides/']) {
        const response = await page.goto(new URL(route,base).href);
        assert.equal(response.status(),200);
        assert.equal(await page.locator('h1').count(),1);
        assert.equal(await page.locator('main').count(),1);
        assert.equal(await page.evaluate(() => document.documentElement.scrollWidth<=window.innerWidth),true,`${width} overflow ${route}`);
        assert.equal(await page.locator('.suite-skip').getAttribute('href'),'#main-content');
        if (output && width===390 && colorScheme==='light' && route==='changes/') await page.screenshot({path:path.join(output,'guide.png')});
        if (output && width===390 && colorScheme==='dark' && route==='changes/timeline.html') await page.screenshot({path:path.join(output,'timeline-dark.png')});
        results.push({width,colorScheme,route,overflow:false});
      }
      await context.close(); assert.deepEqual(errors,[]);
    }
    const context=await browser.newContext({viewport:{width:390,height:900}});
    const page=await context.newPage(); await page.goto(new URL('changes/timeline.html',base).href);
    await page.keyboard.press('Tab');
    assert.equal(await page.evaluate(()=>document.activeElement.className),'suite-skip');
    await page.keyboard.press('Enter'); assert.equal(new URL(page.url()).hash,'#main-content');
    assert.equal(await page.locator('.wc-event').count(),8);
    await page.getByLabel('Search entries',{exact:true}).fill('procurement');
    assert.equal(await page.locator('.wc-event:visible').count(),1);
    await page.getByLabel('Search entries',{exact:true}).fill('no such entry xyz');
    assert.equal(await page.locator('.wc-event:visible').count(),0);
    assert.equal(await page.locator('#timeline-empty').isVisible(),true);
    await page.getByRole('button',{name:'Clear filters'}).click();
    assert.equal(await page.locator('.wc-event:visible').count(),8);
    await page.getByLabel('Follow a history',{exact:true}).selectOption('fec-capacity');
    assert.equal(await page.locator('.wc-event:visible').count(),3);
    await page.goto(new URL('changes/timeline.html#us-az-birth-opinion-2026-source-opinion',base).href);
    assert.equal(await page.locator('#us-az-birth-opinion-2026-source-opinion').isVisible(),true);
    await context.close();
    const plain=await browser.newContext({javaScriptEnabled:false,viewport:{width:320,height:900}});
    const plainPage=await plain.newPage(); await plainPage.goto(new URL('changes/timeline.html',base).href);
    assert.equal(await plainPage.locator('.wc-event:visible').count(),8);
    assert.equal(await plainPage.locator('#timeline-filters').isVisible(),false);
    await plainPage.locator('#us-nyc-care-procurement-2026 summary').press('Enter');
    assert.equal(await plainPage.locator('#us-nyc-care-procurement-2026-source-notice').isVisible(),true);
    await plainPage.goto(new URL('changes/timeline.html#us-az-birth-opinion-2026-source-opinion',base).href);
    assert.equal(await plainPage.locator('#us-az-birth-opinion-2026-source-opinion').isVisible(),true);
    await plain.close();
    const summary={layouts:results.length,keyboard_skip:true,search:true,history_filter:true,no_results_clear:true,stable_source_anchor:true,no_javascript:true,resource_errors:0,layouts_checked:results};
    if(output) fs.writeFileSync(path.join(output,'browser.json'),JSON.stringify(summary,null,2)+'\n');
    console.log(JSON.stringify(summary,null,2));
  } finally { await browser.close(); }
})().catch(error=>{console.error(error);process.exitCode=1;});
