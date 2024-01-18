import unittest
from selenium import webdriver
from pages.HomePage import HomePage


class TestAddProductsToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://automationexercise.com')
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_products_to_cart(self):
        # Create instances of page objects
        products_page = self.home_page.click_products_tab()

        # Hover over and click 'Add to cart' for the first product
        products_page.hover_over_product(1).click_add_to_cart_button(1)

        # Click 'Continue Shopping' button
        products_page.click_continue_shopping_button()

        # Hover over and click 'Add to cart' for the second product
        products_page.hover_over_product(2).click_add_to_cart_button(2)

        # Click 'View Cart' button
        cart_page = products_page.click_view_cart_button()

        # Verify both products are added to Cart
        cart_page.verify_products_in_cart()

        # Verify their prices, quantity and total price
        cart_page.verify_product_prices()
        cart_page.verify_product_quantities()
        cart_page.verify_total_prices()


if __name__ == '__main__':
    unittest.main()
