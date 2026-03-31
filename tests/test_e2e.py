from playwright.sync_api import sync_playwright

def test_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Retry logic add chestham
        page.goto("http://127.0.0.1:8000", timeout=60000)

        content = page.content()
        assert "Calculator API" in content

        browser.close()