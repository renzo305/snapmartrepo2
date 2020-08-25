class Login_Page:

    loginXPath = {
            "home_welcome_dismiss": "//button[contains(@aria-label, 'Close')]",
            "tab_account": "//button[contains(@id, 'Account')]",
            "tab_account_login": "//button[contains(@id, 'Login')]",
            "login_email": "//input[contains(@id, 'email')]",
            "login_password": "//input[contains(@id, 'password')]",
            "create_email_btn": "//button[contains(@id, 'loginButton')]",
            "dismiss_cookie": "//a[contains(text(), 'Me want it!')]"
        }
    banner_dismiss = loginXPath.get("home_welcome_dismiss")
    account_tab = loginXPath.get("tab_account")
    account_login = loginXPath.get("tab_account_login")
    login_email_box = loginXPath.get("login_email")
    login_password = loginXPath.get("login_password")
    login_submit = loginXPath.get("create_email_btn")
    login_close_cookie = loginXPath.get("dismiss_cookie")

    registerXPath = {
        "new_customer": "//a[contains(text(), 'Not yet a customer')]",
        "reg_email": "//input[contains(@id, 'email')]",
        "reg_password": "//input[contains(@id, 'password')]",
        "reg_repeat_password": "//input[contains(@id, 'repeatPassword')]",
        "create_email_btn": "//button[contains(@id, 'loginButton')]",
        "reg_security_question": "//div[contains(@class, 'mat-select-arrow')]"
    }

    register_first = registerXPath.get("new_customer")
    register_email = registerXPath.get("reg_email")
    register_password = registerXPath.get("reg_password")
    register_confirm_password = registerXPath.get("reg_repeat_password")
    register_security_question = registerXPath.get("reg_security_question")
    register_submit = registerXPath.get("create_email_btn")

class Shopping:
    shopItemsXPath = {
        "home_customer_page": "//div[@class='ng-star-inserted']/mat-grid-list[@class='mat-grid-list']/div/mat-grid-tile",
        "tab_add_to_cart": "//button[aria-label='Show the shopping cart']",
        "add_to_basket_tab": "//span[contains(text(), 'Your Basket')]",
        "basket_checkout": "//button[contains(@id, 'checkout')]",
        "basket_address": "//button[@aria-label='Add a new address']",
        "pay_choices": "//mat-cell[contains(text(), '{0}')]/preceding::mat-radio-button[1]",
        "proceed_option": "//button[contains(@aria-label, 'Proceed')]"
    }

    shopping_homepage = shopItemsXPath.get("home_customer_page")
    shopping_add_to_basket = shopItemsXPath.get("tab_add_to_cart")
    shopping_add_to_basket_header = shopItemsXPath.get("add_to_basket_tab")
    shopping_add_to_basket_checkout = shopItemsXPath.get("basket_checkout")
    shopping_checkout_address = shopItemsXPath.get("basket_address")
    shopping_delivery = shopItemsXPath.get("pay_choices")
    shopping_proceed_to_delivery = shopItemsXPath.get("proceed_option")

    addressXPath = {
        "address_h1": "//h1[contains(text(), 'Add New Address')]",
        "address_country": "//input[contains(@placeholder, 'country')]",
        "address_name": "//input[contains(@placeholder, 'name')]",
        "address_mobile": "//input[contains(@placeholder, 'mobile')]",
        "address_zipcode": "//input[contains(@placeholder, 'ZIP')]",
        "address_curraddress": "//textarea[contains(@placeholder, 'address')]",
        "address_city": "//input[contains(@placeholder, 'city')]",
        "address_state": "//input[contains(@placeholder, 'state')]",
        "address_submit": "//button[contains(@id, 'submit')]",
        "address_select": "//mat-cell[contains(text(), 'Siquijor')]/preceding::mat-radio-button[1]",
        "continue_payment": "//button[contains(@aria-label, 'payment')]"##"//span[contains(text(), 'Continue')]/ancestor::button"
    }

    address_header = addressXPath.get("address_h1")
    address_country = addressXPath.get("address_country")
    address_name = addressXPath.get("address_name")
    address_mobile = addressXPath.get("address_mobile")
    address_zipcode = addressXPath.get("address_zipcode")
    address_curraddress = addressXPath.get("address_curraddress")
    address_city = addressXPath.get("address_city")
    address_state = addressXPath.get("address_state")
    address_submit_btn = addressXPath.get("address_submit")
    address_choice = addressXPath.get("address_select")
    continue_payment = addressXPath.get("continue_payment")

    paymentOptionsXpath = {
        "payment_add_card": "//mat-expansion-panel-header/span/mat-panel-description[contains(text(), 'Add')]",
        "card_name": "mat-label[contains(text(), 'Name')]/preceding::input[contains(@id, 'mat-input')]"
    }

    payment_add_card = paymentOptionsXpath.get("payment_add_card")
    card_name = paymentOptionsXpath.get("card_name")