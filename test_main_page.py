from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest as pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)         # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                            # открываем страницу
        page.go_to_login_page()                # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    basket_page.should_not_be_basket_formset()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket_message()


# по логике эти тесты должны относиться к тест сьюту test_login_page,
# поэтому они были размещены в отдельный класс
@pytest.mark.need_review_custom_scenarios
class TestActionsInLoginPageWithEmptyData():
    def test_guest_cant_login_with_empty_data(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
        page.remove_login_form_required_attribute()
        page.login_button_click()
        page.should_be_danger_msg_in_login_form()

    def test_guest_cant_register_with_empty_data(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
        page.remove_register_form_required_attribute()
        page.register_button_click()
        page.should_be_danger_msg_in_register_form()