from playwright.sync_api import sync_playwright


def screenshot(link, objID, objType):
  filename = 'screenshots/{}_{}.png'.format(objType, objID)

  with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    device = p.devices['iPhone X']
    page = browser.new_page(**device, color_scheme='light')
    link = link if 'https://www.reddit.com/' in link else 'https://www.reddit.com{}'.format(link)
    page.goto(link)
    page.wait_for_load_state('networkidle')

    locatorTag = 'shreddit-post' if objType == 'post' else 'shreddit-comment-tree'
    openInAppBar = 'shreddit-async-loader[bundlename="bottom_bar_xpromo"]'
    iPhonePrompt = 'shreddit-async-loader[bundlename="educational_deeplink_prompt_for_ios"]'

    if page.locator(locatorTag).first.is_visible():
      if page.locator(openInAppBar).is_visible():
        page.evaluate('''(openInAppBar) => document.querySelector(openInAppBar).remove()''', openInAppBar)
      elif page.locator(iPhonePrompt).is_visible():
        page.evaluate('''(iPhonePrompt) => document.querySelector(iPhonePrompt).remove()''', iPhonePrompt)
      if objType != 'post':
        page.evaluate('''(commentChildren) => document.querySelector(commentChildren).remove()''', '[slot="children"]')
        page.evaluate('''(commentTools) => document.querySelector(commentTools).remove()''', 'shreddit-comments-page-tools')
        if page.locator('button:has-text("Continue")').is_visible():
          page.locator('button:has-text("Continue")').click()
      page.locator(locatorTag).first.click()
      page.locator(locatorTag).first.screenshot(path=filename)
    browser.close()

  return filename