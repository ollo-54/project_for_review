from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
#        assert True
        assert "/login/" in self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
#        assert True
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
#        assert True
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTR_FORM), "Login register form is not presented"

    def register_new_user(self, email, password):
        login_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        login_field.send_keys(email)

        pwd_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD)
        pwd_field.send_keys(password)
        pwd_confirm_field = self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD_FIELD)
        pwd_confirm_field.send_keys(password)

        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()	

    def should_be_login_link(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login URL is not presented"


