from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


def extract_numeric_value(price_text):
    digits = ''.join(filter(str.isdigit, price_text))
    if not digits:
        raise ValueError(f"Unable to extract numeric value from price text: {price_text}")
    return int(digits)


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

    def verify_product_quantities(self):
        # Verify the quantities of the first and second products
        first_product_quantity = int(self.wait_until_element_is_visible(self.first_product_quantity).text)
        second_product_quantity = int(self.wait_until_element_is_visible(self.second_product_quantity).text)

        assert first_product_quantity > 0, f"Expected first product quantity to be positive, but found {first_product_quantity}"
        assert second_product_quantity > 0, f"Expected second product quantity to be positive, but found {second_product_quantity}"

    def verify_total_prices(self):
        # Get the prices of the first and second products from the CartPage
        first_product_price_text = self.wait_until_element_is_visible(self.first_product_price).text
        second_product_price_text = self.wait_until_element_is_visible(self.second_product_price).text

        # Extract numeric values from the product price strings
        try:
            first_product_price = extract_numeric_value(first_product_price_text)
            second_product_price = extract_numeric_value(second_product_price_text)
        except ValueError:
            assert False, f"Unable to extract numeric values from product prices"

        # Verify the total prices
        total_price_first_product = self.wait_until_element_is_visible(self.total_price_for_first_product).text
        total_price_second_product = self.wait_until_element_is_visible(self.total_price_for_second_product).text

        try:
            assert total_price_first_product == f"Rs. {first_product_price}", f"Expected total price for the first product to be {first_product_price}, but found {total_price_first_product}"
            assert total_price_second_product == f"Rs. {second_product_price}", f"Expected total price for the second product to be {second_product_price}, but found {total_price_second_product}"
        except ValueError:
            assert False, f"Unable to parse total prices from CartPage"
