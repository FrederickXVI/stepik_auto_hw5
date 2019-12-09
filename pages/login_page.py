from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        # находим поле ввода email для регистрации, передаем значение email
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        # находим поле ввода password для регистрации, передаем значение password
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        # находим поле ввода confirm password для регистрации, передаем значение password
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        # нажимаем кнопку "регистрация"
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "Current url is not login url"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"