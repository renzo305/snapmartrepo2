import unittest
from snapmart_locator_dict import *
from selenium import webdriver
import time
from snapmart_test_keyword import Keywords
from selenium.webdriver.support import expected_conditions as EC



class createEmail(unittest.TestCase, Keywords):


    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.driver = webdriver.Chrome(executable_path=".\Chromedriver\chromedriver.exe", options=self.options)
        self.driver.maximize_window()


    def test_email_reg(self):

        self.driver.get("http://210.16.121.50:3000/")

        self.clickBtn(Login_Page.banner_dismiss)

        self.clickBtn(Login_Page.account_tab)

        self.clickBtn(Login_Page.account_login)

        ##self.checkElementPresence(Login_Page.login_page_check)

        self.clickBtn(Login_Page.register_first)

        self.inputText(Login_Page.register_email, "johnemail@test.com")

        self.inputText(Login_Page.register_password, "test1234")

        self.inputText(Login_Page.register_confirm_password, "test1234")

        self.clickBtn(Login_Page.register_security_question)

        self.clickBtn(Login_Page.register_submit)


    def test_shoppingMenu(self):
        self.driver.get("https://test.cuongnguyen.online")

        self.clickBtn(Login_Page.banner_dismiss)

        self.clickBtn(Login_Page.account_tab)

        self.clickBtn(Login_Page.account_login)

        self.inputText(Login_Page.login_email_box, "johnrenzo.aguila@gmail.com")

        self.inputText(Login_Page.login_password,"1234567890Ab!")

        self.clickBtn(Login_Page.login_submit)

        self.checkElementPresence(Shopping.shopping_homepage)

        self.chooseRandomElement(Shopping.shopping_homepage,"[{0}]/descendant::button", 5)

        #self.scrollUp(Shopping.shopping_homepage)

        self.clickBtn(Shopping.shopping_add_to_basket_header)

        self.checkElementPresence(Shopping.shopping_add_to_basket)

        self.clickBtn(Shopping.shopping_add_to_basket_checkout)

        self.clickBtn(Shopping.shopping_checkout_address)

        self.inputText(Shopping.address_country, "Philippines")

        self.inputText(Shopping.address_name, "John Smith")

        self.inputText(Shopping.address_mobile, "09456789123")

        self.inputText(Shopping.address_zipcode, "2892")

        self.inputText(Shopping.address_curraddress, "Sharksfin Subdivision, Brgy. Tibay, Siquijor")

        self.inputText(Shopping.address_city, "Laguna")

        self.inputText(Shopping.address_state, "Laguna")

        self.clickBtn(Shopping.address_submit_btn)

        self.takeScreen("Checkout")

    def test_shoppingMenu_existing_address(self):
        self.driver.get("https://test.cuongnguyen.online")

        self.clickBtn(Login_Page.banner_dismiss)

        self.clickBtn(Login_Page.login_close_cookie)

        self.clickBtn(Login_Page.account_tab)

        self.clickBtn(Login_Page.account_login)

        self.inputText(Login_Page.login_email_box, "johnrenzo.aguila@gmail.com")

        self.inputText(Login_Page.login_password,"1234567890Ab!")

        self.clickBtn(Login_Page.login_submit)

        self.checkElementPresence(Shopping.shopping_homepage)

        self.chooseRandomElement(Shopping.shopping_homepage,"[{0}]/descendant::button", 5)

        #self.scrollUp(Shopping.shopping_homepage)

        self.clickBtn(Shopping.shopping_add_to_basket_header)

        self.checkElementPresence(Shopping.shopping_add_to_basket)

        self.clickBtn(Shopping.shopping_add_to_basket_checkout)

        self.clickBtn(Shopping.address_choice)

        self.clickBtn(Shopping.continue_payment)

        self.clickRadioBtn(Shopping.shopping_delivery, ["One Day Delivery","Fast Delivery","Standard Delivery"])

        self.clickBtn(Shopping.shopping_proceed_to_delivery)

        self.clickBtn(Shopping.payment_add_card)

        time.sleep(5)

        self.inputText(Shopping.card_name, "John Morrison")

        self.takeScreen("Checkout")


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
