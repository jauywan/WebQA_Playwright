"""
This module contains "Category" (カテゴリーからさがす):
The page objects for the category selection on the search bar.
"""

from playwright.sync_api import Page

class CategoryPage:

    # カテゴリ ページ間の移動に使用されるロケーターとセレクターが含まれています。 / Contains the locators and selectors used for navigating through Category pages.
    def __init__(self,page: Page) -> None:
        self.page = page
        # Locators
        self.tier1_btn = self.page.locator("//a[@href='/categories?category_id=5']")
        self.tier2_btn = self.page.locator("//a[@href='/categories?category_id=72']")
        self.tier3_btn = self.page.locator("//a[@href='/search?category_id=674']")
        # Selectors
        self.categ_selector = "select[class='merInputNode select__da4764db medium__da4764db']"
     
    # カテゴリを選択するためのページ アクションが含まれています: コンピュータ・IT / Contains page action for selecting the category: コンピュータ・IT
    def selectCategory(self) -> None:
        self.tier1_btn.click()
        self.tier2_btn.click()
        self.tier3_btn.click()
        self.page.wait_for_selector(self.categ_selector)

    # 左側のフィルターがロードされるまで待ちます / Wait for Left Hand Side Filters to load
    def waitForCategoryToLoad(self) -> None:
        self.page.wait_for_selector(self.categ_selector)