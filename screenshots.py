from playwright.sync_api import sync_playwright


def screenshot(link, objID, objType):
  filename = 'screenshots/{}_{}.png'.format(objType, objID)

  with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    device = p.devices['iPhone 12']
    page = browser.new_page(**device, color_scheme='light')
    link = link if 'https://www.reddit.com/' in link else 'https://www.reddit.com{}'.format(link)
    page.goto(link)
    page.wait_for_load_state('networkidle')

    locatorTag = 'shreddit-post' if objType == 'post' else 'shreddit-comment-tree'
    continueButtonTag = 'button#secondary-button.continue'

    if page.locator(locatorTag).first.is_visible():
      page.locator(continueButtonTag).click()
      if objType != 'post':
        page.evaluate('''(commentChildren) => document.querySelector(commentChildren).remove()''', '[slot="children"]')
        page.evaluate('''(commentTools) => document.querySelector(commentTools).remove()''', 'shreddit-comments-page-tools')
      page.locator(locatorTag).first.screenshot(path=filename)
    
    browser.close()

  return filename