from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_base.base_page import BasePage


class SearchLocator(object):

    search_result_table = (By.XPATH, '//ul[@id="search-result"]')
    result_links = (By.CSS_SELECTOR, '#search-result>li>div>div>a')


class YandexSearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_search_result_table(self):
        return self.find_elem(SearchLocator.search_result_table, time=15)

    def get_result_links(self) -> list:
        return self.find_elems(SearchLocator.result_links)
