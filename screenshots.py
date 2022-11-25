from playwright.sync_api import sync_playwright
from praw.models.reddit.submission import Submission
from praw.models.reddit.comment import Comment


def screenshot(link, objID, objType):
  filename = 'screenshots/{}_{}.png'.format(objType, objID)

  with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    link = link if 'https://www.reddit.com/' in link else 'https://www.reddit.com{}'.format(link)
    page.goto(link)

    locatorTag = '[data-testid="post-container"]' if objType == 'post' else '.Comment'

    if page.locator(locatorTag).first.is_visible():
      page.locator(locatorTag).first.screenshot(path=filename)
    
    browser.close()

  return filename