import pytest
from playwright.sync_api import sync_playwright

# Fixture for setup and teardown of Playwright browser and page
@pytest.fixture(scope="session") 
def newBrowser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture(scope="function")
def newPage(newBrowser):
    context = newBrowser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()