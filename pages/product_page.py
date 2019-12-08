from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        # записать в переменную название продукта
        current_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # записать в переменную стоимость продукта
        current_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # добавить товар в корзину
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
        # ответить на вопрос
        self.solve_quiz_and_get_code()
        # проверить, что название продукта равно жирному начертанию текста в сообщении успеха и
        # стоимость продукта равна жирному начертанию текста в сообщении инфо
        assert current_product_name == self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text \
            and current_product_price == self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text, \
            "Название или стоимость продукта не соотвествует добавленному"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be desappeared"