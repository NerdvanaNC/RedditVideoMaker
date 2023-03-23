from playwright.sync_api import sync_playwright


def screenshot(link, objID, objType):
  filename = 'screenshots/{}_{}.png'.format(objType, objID)

  with sync_playwright() as p:
    browser = p.chromium.launch() # Device manipulation only seems to work correctly in Chrome.
    page = browser.new_page()
    device = p.devices['iPhone X'] # We want screenshots to look like they were taken from a mobile device.
    page = browser.new_page(**device, color_scheme='light') # Light mode screenshots work better for reels.
    link = link if 'https://www.reddit.com/' in link else 'https://www.reddit.com{}'.format(link)

    page.goto(link)
    page.wait_for_load_state('networkidle')

    locatorTag = 'shreddit-post' if objType == 'post' else 'shreddit-comment-tree'

    # page.evaluate() is perfect for running arbitrary JS on the page.
    # The evaluation statement takes a function with one argument, and the value of the second argument of the Python function is
    # passed in as that argument to the JS function when it runs.
    if page.locator(locatorTag).first.is_visible():
      if page.locator('shreddit-async-loader[bundlename="bottom_bar_xpromo"]').is_visible():
        page.evaluate('''(openInAppBar) => document.querySelector(openInAppBar).remove()''', 'shreddit-async-loader[bundlename="bottom_bar_xpromo"]')
      elif page.locator('shreddit-async-loader[bundlename="educational_deeplink_prompt_for_ios"]').is_visible():
        page.evaluate('''(iPhonePrompt) => document.querySelector(iPhonePrompt).remove()''', 'shreddit-async-loader[bundlename="educational_deeplink_prompt_for_ios"]')

      if objType != 'post':
        if page.locator('[slot="children"]').first.is_visible():
          page.evaluate('''(commentChildren) => document.querySelector(commentChildren).remove()''', '[slot="children"]')
        if page.locator('shreddit-comments-page-tools').first.is_visible():
          page.evaluate('''(commentTools) => document.querySelector(commentTools).remove()''', 'shreddit-comments-page-tools')
        if page.locator('button:has-text("Continue")').is_visible(): # This 'Continue' button doesn't appear on Post pages, only Comment pages.
          page.locator('button:has-text("Continue")').click()

      page.locator(locatorTag).first.screenshot(path=filename)
      
    browser.close()

  return filename