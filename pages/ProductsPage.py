from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.CartPage import CartPage


class ProductsPage(BasePage):
    # Locators
    first_product = (By.XPATH, "(//a[@class='btn btn-default add-to-cart'])[1]")
    first_product_price = (By.XPATH, "(//div[@class='productinfo text-center']//h2)[1]")
    second_product = (By.XPATH, "(//a[@class='btn btn-default add-to-cart'])[3]")
    second_product_price = (By.XPATH, "(//div[@class='productinfo text-center']//h2)[2]")
    first_product_add_cart_button = (By.XPATH, "(//*[text()='Add to cart'])[1]")
    second_product_add_cart_button = (By.XPATH, "(//*[text()='Add to cart'])[3]")
    continue_shopping_button = (By.XPATH, "//*[text()='Continue Shopping']")
    view_cart_button = (By.XPATH, "//*[text()='View Cart']")

    # Methods
    def hover_over_product(self, index):
        #  Use the appropriate locator based on the index
        if index == 1:
            product_link = self.wait_until_element_is_visible(self.first_product)
        elif index == 2:
            product_link = self.wait_until_element_is_visible(self.second_product)
        else:
            raise ValueError(f"Unsupported index: {index}")

        # Hover over the element
        ActionChains(self._driver).move_to_element(product_link).perform()
        return self  # Return the ProductsPage instance for method chaining

    def click_add_to_cart_button(self, index):
        # Use the appropriate locator based on the index
        if index == 1:
            add_to_cart_button = self.wait_until_element_is_visible(self.first_product_add_cart_button)
        elif index == 2:
            add_to_cart_button = self.wait_until_element_is_visible(self.second_product_add_cart_button)
        else:
            raise ValueError(f"Unsupported index: {index}")

        # Click the Add to Cart button
        add_to_cart_button.click()
        return self  # Return the ProductsPage instance for method chaining

    def click_continue_shopping_button(self):
        self.click(self.continue_shopping_button)

    def click_view_cart_button(self):
        self.click(self.view_cart_button)
        return CartPage(self._driver)

    def get_first_product_price(self):

        first_product_price = self.wait_until_element_is_visible(self.first_product_price).text
        return first_product_price

    def get_second_product_price(self):
        second_product_price = self.wait_until_element_is_visible(self.second_product_price).text
        return second_product_price
