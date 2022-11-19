from playwright.sync_api import sync_playwright

with sync_playwright() as p:
  browser = p.firefox.launch()
  page = browser.new_page()
  page.goto('https://www.reddit.com/r/AskReddit/comments/yyz6ox/you_wake_up_as_joe_biden_whats_your_first_move/')
  print(page.title())
  if page.locator('[data-test-id="post-content"]').is_visible():
    page.locator('[data-test-id="post-content"]').screenshot(path='screenshots/post.png')
  browser.close()