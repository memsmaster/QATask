from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CartPage(BasePage):
    # Locators
    products_list = (By.CSS_SELECTOR, "#cart_info_table > tbody > tr")
    # product_prices = (By.CSS_SELECTOR, "#cart_info_table > tbody > tr > td:nth-child(3)")
    first_product_price = (By.XPATH, "(//table[@id='cart_info_table']/tbody/tr/td[3]/p)[1]")
    second_product_price = (By.XPATH, "(//table[@id='cart_info_table']/tbody/tr/td[3]/p)[2]")
    first_product_quantity = (By.XPATH, "(//table[@id='cart_info_table']/tbody/tr/td[4]/button)[1]")
    second_product_quantity = (By.XPATH, "(//table[@id='cart_info_table']/tbody/tr/td[4]/button)[2]")
    # product_quantity = (By.CSS_SELECTOR, "#cart_info_table > tbody > tr > td:nth-child(4) input")
    total_price_for_first_product = (By.XPATH, "(//table[@id='cart_info_table']/tbody/tr/td[5]/p)[1]")
    total_price_for_second_product = (By.XPATH, "(//table[@id='cart_info_table']/tbody/tr/td[5]/p)[2]")

    # Methods
    def verify_products_in_cart(self):
        # Verify that products are in the cart
        products = self.wait_until_all_elements_are_visible(self.products_list)
        assert len(products) == 2, f"Expected 2 products in the cart, but found {len(products)}"

    def verify_product_prices(self):
        # Verify the prices of the first and second products
        first_product_price_text = self.wait_until_element_is_visible(self.first_product_price).text
        second_product_price_text = self.wait_until_element_is_visible(self.second_product_price).text

        # Extract numeric values from the product price strings
        first_product_price = int(''.join(filter(str.isdigit, first_product_price_text)))
        second_product_price = int(''.join(filter(str.isdigit, second_product_price_text)))

        assert first_product_price > 0, f"Expected a positive numeric value for the first product price, but found {first_product_price_text}"
        assert second_product_price > 0, f"Expected a positive numeric value for the second product price, but found {second_product_price_text}"
        # Create an instance of ProductsPage to use its methods
        # from pages.ProductsPage import ProductsPage
        # products_page = ProductsPage(self._driver)
        #
        # # Get the prices of the first and second products from the ProductsPage
        # expected_first_product_price = products_page.get_first_product_price()
        # expected_second_product_price = products_page.get_second_product_price()
        #
        # # Get the prices of the first and second products from the CartPage
        # actual_first_product_price_text = self.wait_until_element_is_visible(self.first_product_price).text
        # actual_second_product_price_text = self.wait_until_element_is_visible(self.second_product_price).text
        #
        # # Extract numeric values from the product price strings or handle exceptions
        # # actual_first_product_price = self.extract_numeric_value(actual_first_product_price_text)
        # # actual_second_product_price = self.extract_numeric_value(actual_second_product_price_text)
        #
        # # Verify that the prices match
        # assert actual_first_product_price_text == expected_first_product_price, f"Expected the first product price to be {expected_first_product_price}, but found {actual_first_product_price}"
        # assert actual_second_product_price_text == expected_second_product_price, f"Expected the second product price to be {expected_second_product_price}, but found {actual_second_product_price}"

    def verify_product_quantities(self):
        # Verify the quantities of the first and second products
        first_product_quantity = int(self.wait_until_element_is_visible(self.first_product_quantity).text)
        second_product_quantity = int(self.wait_until_element_is_visible(self.second_product_quantity).text)

        assert first_product_quantity > 0, f"Expected first product quantity to be positive, but found {first_product_quantity}"
        assert second_product_quantity > 0, f"Expected second product quantity to be positive, but found {second_product_quantity}"

    def verify_total_prices(self):
        # Verify the total prices of the first and second products
        total_price_first_product = self.wait_until_element_is_visible(self.total_price_for_first_product).text
        total_price_second_product = self.wait_until_element_is_visible(self.total_price_for_second_product).text

        assert total_price_first_product == 'Rs. 500', f"Expected total price for the first product to be a number, but found {total_price_first_product}"
        assert total_price_second_product == 'Rs. 400', f"Expected total price for the second product to be a number, but found {total_price_second_product}"
