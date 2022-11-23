from playwright.sync_api import sync_playwright
from praw.models.reddit.submission import Submission
from praw.models.reddit.comment import Comment


def screenshot(link, objID, objType):
  with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    link = link if 'https://www.reddit.com/' in link else 'https://www.reddit.com{}'.format(link)
    page.goto(link)
    print(page.title())

    locatorTag = '[data-testid="post-container"]' if objType == 'post' else '.Comment'

    if page.locator(locatorTag).first.is_visible():
      page.locator(locatorTag).first.screenshot(path='screenshots/{}_{}.png'.format(objType, objID))
    
    browser.close()