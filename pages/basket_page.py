from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MSG), \
            "Empty basket message is not presented, but should be"

    def should_not_be_basket_formset(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), \
            "Basket formset is presented, but should not be"
