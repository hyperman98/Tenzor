from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_base.base_page import BasePage


class HomeLocator(object):
    search_input_field = (By.XPATH, '//input[@id="text"]')
    suggest_table = (
        By.CSS_SELECTOR,
        'mini-suggest__item.mini-suggest__item_type_fulltext.mini-suggest__item_selected_yes'

    )
    images = (
        By.XPATH,
        '//a[@data-id="images"]'
    )

    button_images = (
        By.XPATH,
        '//a[@aria-label="Картинки"'
    )


class YandexHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.search_field = self.find_elem(HomeLocator.search_input_field)
        self.images = self.find_elem(HomeLocator.images)

    def enter_word(self, word: str):
        return self.search_field.send_keys(word)

    def press_enter(self):
        self.search_field.send_keys(Keys.ENTER)
        return self.search_field

    def get_search_field(self):
        return self.search_field

    def get_suggest_table(self):
        return self.find_elem(HomeLocator.suggest_table)

    def get_images_block(self):
        return self.images

    def get_button_image(self):
        return self.find_elem(HomeLocator.button_images)
