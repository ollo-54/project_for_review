from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_link()

    def should_be_basket_link(self):
        # реализуйте проверку на корректный url адрес
        assert "/basket" in self.browser.current_url, "It isn't basket url"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), "Backet isn't empty"

    def should_be_message_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY), "Message of empty isn't presented"

        message = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY).text
        assert message == "Your basket is empty. Continue shopping" or message == "Ваша корзина пуста Продолжить покупки", "Message about empty basket incorrect"