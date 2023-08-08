import allure
from selenium.webdriver.common.keys import Keys
from pages.basepage import BasePage
from pages.locators import YandexMainPagesLocators
from pages.yandex_results_page import YandexSearchResultsPage
from pages.yandex_images_page import YandexImagesPage


class YandexMainPage(BasePage):

    @allure.step('Проверка октрытия страницы Яндекс')
    def should_be_yandex_main_page(self):
        self.should_be_yandex_url()

    def should_be_yandex_url(self):
        assert self.browser.current_url == "https://yandex.ru/"

    @allure.step('Поисковая строка и слово тензор')
    def search_in_input_field(self):
        input_field = self.browser.find_element(*YandexMainPagesLocators.INPUT_FIELD)
        input_field.click()
        with allure.step('Ввод в поисковую строку'):
            input_field.send_keys("тензор")
        with allure.step('Проверка suggest'):
            self.should_be_pop_up()
        input_field.send_keys(Keys.RETURN)
        return YandexSearchResultsPage(browser=self.browser, url=self.browser.current_url)

    def should_be_pop_up(self):
        assert self.is_element_present(*YandexMainPagesLocators.POPUP), "Suggest отсутствует"

    @allure.step('Проверка url страницы с категориями')
    def should_be_images_link(self):
        assert self.is_element_present(*YandexMainPagesLocators.IMAGES_LINK)

    @allure.step('Переход на страницу категорий')
    def going_to_images_page(self):
        images_link = self.browser.find_element(*YandexMainPagesLocators.IMAGES_LINK)
        images_link.click()
        return YandexImagesPage(browser=self.browser, url=self.browser.current_url)