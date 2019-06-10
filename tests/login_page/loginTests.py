from pages.login_page.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("class_setup")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login_user("test@email.com", "abcabc")

        result1 = self.lp.verifyTitle()         # Intentionally failing the test in login_page.py file
        self.ts.mark(result1, "Title was verified")

        result2 = self.lp.verifyValidLogin()
        self.ts.mark_final("Test_Valid_Login", result2, "Login was verified")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login_user("", "")       # Not passing username and password
        result = self.lp.verifyInvalidLogin()
        self.ts.mark(result, "Login was verified")
