import allure

from pages.basepage import BasePage
from pages.locators import YandexResultsPageLocators


class YandexSearchResultsPage(BasePage):

    @allure.step('Провекра количества результатов поиска')
    def count_of_results(self):
        list_links = []
        counter = 0
        tenz_links_count = 0
        results = self.browser.find_elements(*YandexResultsPageLocators.RESULTS)
        for result in results:
            if counter != 5:
                list_links.append(result.get_attribute("href"))
                counter = counter + 1
        for i in list_links:
            if i in "tenzor.ru":
                tenz_links_count = tenz_links_count + 1
        assert tenz_links_count == 5, "Не везде есть ссылка на tenzor"