from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")
    
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "input#id_registration-email")
    REG_PASSWORD_FIELD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REG_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "input#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form button.btn")

class ProductPageLocators(object):
    BUTTON_ADD_TO_BACKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    BTN_USER_ADD_TO_BACKET = (By.CSS_SELECTOR, "#promotions > section:nth-child(3) > ul > li:nth-child(1) > article > div.product_price > form > button")
    MESSAGE_ABOUT_ADDING_USER = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators(object):
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
