import pytest as pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()   # открываем страницу
    page.should_not_be_success_message()
    page.test_guest_can_add_product_to_basket()


@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    #Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    #Добавляем товар в корзину
    page.test_guest_can_add_product_to_basket()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    #Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    #Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    #Добавляем товар в корзину
    page.test_guest_can_add_product_to_basket()
    #Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.success_message_is_disappeared()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    basket_page.should_not_be_basket_formset()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открываем страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        # регистрируем нового пользователя
        LoginPage.register_new_user(page, email=str(time.time()) + "@fakemail.org", password="fakepassword123")
        # проверяем, что пользователь зарегистрирован
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        # Открываем страницу товара
        page = ProductPage(browser, link)
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()  # открываем страницу
        page.test_guest_can_add_product_to_basket()