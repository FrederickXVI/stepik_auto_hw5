from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def login_button_click(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def register_button_click(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def register_new_user(self, email, password):
        # находим поле ввода email для регистрации, передаем значение email
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        # находим поле ввода password для регистрации, передаем значение password
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        # находим поле ввода confirm password для регистрации, передаем значение password
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        # нажимаем кнопку "регистрация"
        self.register_button_click()

    def remove_login_form_required_attribute(self):
        self.browser.execute_script("document.querySelector('#id_login-username').removeAttribute('required')")
        self.browser.execute_script("document.querySelector('#id_login-password').removeAttribute('required')")

    def remove_register_form_required_attribute(self):
        self.browser.execute_script("document.querySelector('#id_registration-email').removeAttribute('required')")
        self.browser.execute_script("document.querySelector('#id_registration-password1').removeAttribute('required')")
        self.browser.execute_script("document.querySelector('#id_registration-password2').removeAttribute('required')")

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

    def should_be_danger_msg_in_login_form(self):
        # проверка, что есть сообщение об ошибке на форме логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_DANGER_ALERT)

    def should_be_danger_msg_in_register_form(self):
        # проверка, что есть сообщение об ошибке на форме регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_DANGER_ALERT)
