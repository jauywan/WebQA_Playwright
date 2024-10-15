"""
This module contains "Main Page" (Landing Page, Search Results):
The page objects for the landing page, and the search results.
"""

from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

class MainPage:

    # Page Definition
    URL = "https://jp.mercari.com/"

    # ランディング ページと検索結果ページを移動するために使用されるロケーターとセレクターが含まれています。
    # Contains the locators and selectors used for navigating through the Landing Page and Search Result pages.
    def __init__(self, page: Page) -> None:
        self.page = page
        # ロケーター / Locators
        self.main_logo = self.page.locator("//div[@data-testid='mercari-logo']")
        # 検索バーのロケーター / Search Bar Locators
        self.search_bar = self.page.locator("//input[@aria-label='検索キーワードを入力']")
        self.category_btn = self.page.locator("//a[@href='/categories']/p")
        self.removesearch_btn = self.page.locator("//button[@aria-label='検索キーワードを削除']")
        self.search_history = self.page.locator("//section[@data-testid='search-history']/descendant::p")

        # 検索結果/カテゴリ検証ロケーター / Search Results/Category Validation Locator
        self.tier1_category = self.page.locator("//option[@value='5']")
        self.tier2_category = self.page.locator("//option[@value='72']")
        self.tier3_category = self.page.locator("//input[@value='674']")

        # 検索履歴検証ロケーター / Search History Validation Locator
        self.first_history = self.page.locator("//section[@data-testid='search-history']/descendant::p[1]")
        self.second_history = self.page.locator("//section[@data-testid='search-history']/descendant::p[2]")
        self.third_history = self.page.locator("//section[@data-testid='search-history']/descendant::p[3]")

        # 検索履歴セレクター / Search History Selector
        self.shistory_selector = "li[data-testid='exclude_keyword']"

    # URLに移動 / Navigate to URL
    def navigateToPage(self) -> None:
        self.page.goto(self.URL)

    # ランディングページに移動します / Navigates to Landing Page
    def navigateToMain(self) -> None:
        self.main_logo.click()
        self.page.wait_for_load_state()

    # カテゴリに移動します / Navigate to Category
    def navigateToCategory(self) -> None:
        self.search_bar.click()
        self.category_btn.click()

    # 検索バーにテキストを入力 / Input Text on Search Bar
    def inputSearchText(self, txtStr = str) -> None:
        self.search_bar.click()
        self.search_bar.type(txtStr)
        self.page.keyboard.press('Enter')
        self.page.wait_for_selector(self.shistory_selector)

    # 検索バーの検索キーワードを削除する / Remove Search Keywords on Search Bar
    def removeSearchCategory(self) -> None:
        self.search_bar.click()
        self.removesearch_btn.click()

    # 検索履歴数の取得 / Get Search History Count
    def getSearchHistoryCount(self) -> int:
        return self.search_history.count()
    
    # 検索バーをクリックします / Click Search Bar
    def clickSearchBar(self) -> None:
        self.search_bar.click()

    # 最新の検索履歴を選択 / Select Latest Search History
    def clickLatestSearchHistory(self) -> None:
        self.search_bar.click()
        self.first_history.click()