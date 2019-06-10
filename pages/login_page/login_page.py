from base.base_page import BasePage
import logging
import utilities.custom_logger as cl


class LoginPage(BasePage):

    log = cl.custom_logging(logging.DEBUG)

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)     # Passing the driver instance to parent/super class
        self.driver = driver

    # Locators
    _loginLink = "Login"
    _emailField = "user_email"
    _passwordField = "user_password"
    _loginButton = "commit"

    def clickLoginLink(self):
        self.clickElement(self._loginLink, "link")

    def enterEmail(self, email):
        self.sendKeys(email, self._emailField)

    def enterPassword(self, password):
        self.sendKeys(password, self._passwordField)

    def clickLoginButton(self):
        self.clickElement(self._loginButton, "name")

    def login_user(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyValidLogin(self):
        element_presence = self.isElementPresent("search-courses", locator_type="id")
        return element_presence

    def verifyInvalidLogin(self):
        element_presence = self.isElementPresent("//div[contains(text(), 'Invalid email or password.')]", locator_type="xpath")
        return element_presence

    def verifyTitle(self):
        if "Google" in self.getTitle():     # Intentionally failing the test by passing incorrect expected Title
            return False
        else:
            return True
