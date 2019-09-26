import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage(object):
#    @pytest.mark.need_review
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, test_browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(test_browser, link)
        login_page.open()
        login_page.go_to_login_page()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, test_browser):
        page = ProductPage(test_browser, link)
        page.open()
        page.add_to_basket_user()
        page.should_be_message_about_adding_user()

    def test_user_cant_see_success_message(self, test_browser):
        page = ProductPage(test_browser, link)
        page.open()
        page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(test_browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(test_browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(test_browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(test_browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(test_browser):
    page = ProductPage(test_browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_basket_total()
    time.sleep(5) 

'''
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
#@pytest.mark.xfail
@pytest.mark.parametrize('link', urls)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(test_browser, link):
    page = ProductPage(test_browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_basket_total()
'''

@pytest.mark.need_review@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(test_browser):
    page = ProductPage(test_browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(test_browser):
    page = ProductPage(test_browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_dissapeared_after_adding_product_to_basket(test_browser):
    page = ProductPage(test_browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_success_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(test_browser):
    page = ProductPage(test_browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(test_browser, test_browser.current_url)
    basket_page.should_be_basket_link()
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty()

