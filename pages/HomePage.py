from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.ProductsPage import ProductsPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    products_tab = (By.XPATH, "//*[text()=' Products']")
    all_products_section = (By.XPATH, "//*[text()='All Products']")

    # Methods
    def verify_page_title(self):
        expected_title = "Automation Exercise"
        actual_title = self.title
        assert expected_title == actual_title, f"Expected title {expected_title}, but found {actual_title}"

    def close_google_vignette(self):
        # Locate the product button
        products_button = self.wait_until_element_is_visible(self.products_tab)
        # Click on the product button
        products_button.click()
        # Wait for a moment
        self._driver.implicitly_wait(1)
        # Blocking Google Ads using JavaScript
        script = "const elements = document.getElementsByClassName('adsbygoogle adsbygoogle-noablate'); while (elements.length > 0) elements[0].remove();"
        self._driver.execute_script(script)
        # Scroll the page
        # script = "window.scrollBy(0,350);"
        # self._driver.execute_script(script)

    def click_products_tab(self):
        self.click(self.products_tab)
        self.scroll_to_element(self.all_products_section)
        return ProductsPage(self._driver)

    def scroll_to_element(self, element):
        script = "arguments[0].scrollIntoView(true);"
        self._driver.execute_script(script, self.wait_until_element_is_visible(element))
