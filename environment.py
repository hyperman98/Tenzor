import unittest

from selenium import webdriver

import test_base.print_services as PServ


START_PAGE = 'https://ya.ru/'


class TestEnvironment(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(START_PAGE)
        self.driver.set_page_load_timeout(40)
        PServ.show_set_up_info('Chrome')
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        driver = self.driver
        if driver is not None:
            PServ.show_set_down_info()
            driver.close()
            driver.quit()
