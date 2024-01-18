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

    def click_products_tab(self):
        self.click(self.products_tab)
        self.scroll_to_element(self.all_products_section)
        return ProductsPage(self._driver)

    def scroll_to_element(self, element):
        script = "arguments[0].scrollIntoView(true);"
        self._driver.execute_script(script, self.wait_until_element_is_visible(element))
