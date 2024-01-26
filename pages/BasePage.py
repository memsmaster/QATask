from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self._driver = driver

    def wait_until_element_is_visible(self, locator: tuple):
        # print(f"Waiting for element with locator {locator} to be visible...")
        return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(locator))

    def wait_until_all_elements_are_visible(self, locator: tuple):
        return WebDriverWait(self._driver, 30).until((EC.visibility_of_all_elements_located(locator)))

    def click(self, locator: tuple):
        self.wait_until_element_is_visible(locator).click()

    def is_element_present(self, locator: tuple, timeout=30):
        try:
            WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
