"""
These tests will cover Scenario 2a and 2b.
To run the tests, input the following on the terminal:
"pytest -s Maintest.py"
"""

from Pages.Category import CategoryPage
from Pages.MainPage import MainPage
from playwright.sync_api import expect

# シナリオ 1 - 検索条件が正しく設定されています。 / Scenario 1 - Search conditions are set correctly.
def test_Scenario2a(
    newPage) -> None:

    main_page = MainPage(newPage)
    category_page = CategoryPage(newPage)
    
    main_page.navigateToPage()
    main_page.navigateToCategory()
    category_page.selectCategory()

    # 選択したカテゴリが左側のサイドバーに表示されるかどうかを確認します / Verify if categories selected are displayed on left sidebar
    expect(main_page.tier1_category).to_have_text('本・雑誌・漫画')
    expect(main_page.tier2_category).to_have_text('本')
    expect(main_page.tier3_category).to_be_checked()

    main_page.page.wait_for_timeout(5000) # テストケースが終了する前に少し休憩します / Little pause before the test case ends


# シナリオ 2 - 最新の閲覧履歴から検索条件が正しく設定されている。 / Scenario 2 - Search conditions are set correctly from the latest browsing history.
def test_Scenario2b(
    newPage) -> None:

    main_page = MainPage(newPage)
    category_page = CategoryPage(newPage)

    # 前提条件: 2 つの閲覧履歴エンティティの作成 / Pre-requisite: Creation of 2 browsing history entities
    main_page.navigateToPage()
    main_page.inputSearchText('ポケモン')
    main_page.removeSearchCategory()
    main_page.navigateToCategory()
    category_page.selectCategory()
    main_page.navigateToMain()
    main_page.clickSearchBar()

    searchCount = main_page.getSearchHistoryCount()

    # 最新の閲覧履歴が「コンピュータ・IT」であることを確認します。/ Verify if latest browsing history is 'コンピュータ・IT'.
    if searchCount == 2:
        expect(main_page.first_history).to_have_text('コンピュータ・IT')
        main_page.clickLatestSearchHistory()
        category_page.waitForCategoryToLoad()
        expect(main_page.tier1_category).to_have_text('本・雑誌・漫画')
        expect(main_page.tier2_category).to_have_text('本')
        expect(main_page.tier3_category).to_be_checked()

    # 検索バーに新しいキーワードとして「JavaScript」と入力します / Input 'Javascript' on search bar as new keyword
    main_page.inputSearchText('javascript')
    main_page.navigateToMain()
    main_page.clickSearchBar()

    searchCount = main_page.getSearchHistoryCount()

    # 最新の3 つの閲覧履歴すべてを確認する。/ Verify all three browsing histories.
    if searchCount == 3:
        expect(main_page.first_history).to_have_text('javascript, コンピュータ・IT')
        expect(main_page.second_history).to_have_text('コンピュータ・IT')
        expect(main_page.third_history).to_have_text('ポケモン')

    main_page.page.wait_for_timeout(5000) # テストケースが終了する前に少し休憩します / Little pause before the test case ends