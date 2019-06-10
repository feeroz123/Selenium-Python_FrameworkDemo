from base.base_page import BasePage
from utilities import custom_logger as cl
from traceback import print_stack
import logging


class CoursesPage(BasePage):

    log = cl.custom_logging(logging.INFO)

    # Locators in Courses Page
    _find_course_field = "search-courses"
    _search_course_button = "search-course-button"
    _javascript_course_link = "//div[@class='course-listing-title' and contains(text(), 'JavaScript for beginners')]"
    _enroll_course_button = "enroll-button"
    _cr_num_iframe = "__privateStripeFrame5"
    _cr_num_field = "cardnumber"
    _expiry_date_iframe = "__privateStripeFrame6"
    _expiry_date_field = "exp-date"
    _cvc_iframe = "__privateStripeFrame7"
    _cvc_field = "cvc"
    _country_code_dropdown = "country_code_credit_card-cc"
    _postal_code_iframe = "__privateStripeFrame8"
    _postal_code_field = "postal"
    _save_payment_details_checkbox = "save-payment-details"
    _terms_checkbox = "agreed_to_terms_checkbox"
    _final_enroll_button = "confirm-purchase"
    _error_message = "//div[contains(text(),'The card was declined.')]"

    def __init__(self, driver):
        self.driver = driver
        super(CoursesPage, self).__init__(driver)

    def search_course(self, course_name):
        self.sendKeys(course_name, self._find_course_field)
        self.clickElement(self._search_course_button)
        self.log.info("Searched for course: " + course_name)

    def select_javascript_course(self, course_name):
        if course_name.lower() in "javascript for beginners":
            self.clickElement(self._javascript_course_link, locator_type="xpath")
            self.log.info("Selected the course: 'JavaScript for beginners'")

    def click_enroll_course(self):
        self.scrollPage("down")
        self.clickElement(self._enroll_course_button)
        self.log.info("Clicked on Enroll Course button")

    def enter_card_num(self, card_number):
        self.switch_to_frame(self._cr_num_iframe)
        self.sendKeys(card_number, self._cr_num_field, locator_type="name")
        self.switch_default_content()
        self.log.debug("Entered Card Number")

    def enter_expiry_date(self, exp_date):
        """
        Enter the Expiry Date in MM/YY format
        :param exp_date:
        :return: None
        """
        self.switch_to_frame(self._expiry_date_iframe)
        self.sendKeys(exp_date, self._expiry_date_field, locator_type="name")
        self.switch_default_content()
        self.log.debug("Entered Card Expiry Date")

    def enter_cvc_code(self, cvc_code):
        self.switch_to_frame(self._cvc_iframe)
        self.sendKeys(cvc_code, self._cvc_field, locator_type="name")
        self.switch_default_content()
        self.log.debug("Entered CVC Code")

    def choose_country(self, country_name):
        self.select_dropdown_value(dropdown_locator=self._country_code_dropdown, dropdown_value=country_name)
        self.log.debug("Selected Country")

    def enter_postal_code(self, postal_code):
        self.switch_to_frame(self._postal_code_iframe)
        self.sendKeys(postal_code, self._postal_code_field, locator_type="name")
        self.switch_default_content()
        self.log.debug("Entered Postal Code")

    def disable_save_payment_details(self):
        self.clickElement(self._save_payment_details_checkbox)
        self.log.debug("Disabled saving payment details")

    def accept_terms(self):
        self.clickElement(self._terms_checkbox)
        self.log.debug("Accepted Terms and Conditions")

    def submit_payment(self):
        self.clickElement(self._final_enroll_button)
        self.log.info("Submitted Payment Details")

    def enter_payment_details(self, card_num, card_exp_date, cvc_num, country_name, pin_code):
        try:
            self.enter_card_num(card_num)
            self.enter_expiry_date(card_exp_date)
            self.enter_cvc_code(cvc_num)
            self.choose_country(country_name)
            self.enter_postal_code(pin_code)
            self.log.info("Entered Payment details.")
        except:
            self.log.error("*** Exception occurred during entering payment details.")
            print_stack()

    def enroll_javascript_course(self, card_num, card_exp_date, cvc_num, country, pin_code):
        self.search_course("JavaScript for beginners")
        self.select_javascript_course("JavaScript for beginners")
        self.click_enroll_course()
        self.scrollPage("half-down")
        self.enter_payment_details(card_num, card_exp_date, cvc_num, country, pin_code)
        self.disable_save_payment_details()
        self.accept_terms()
        self.submit_payment()
        self.log.info("Enrolled for course.")

    def verify_error_presence(self):
        try:
            error_present = self.isElementPresent(self._error_message, "xpath")

            if error_present is not None:
                self.log.info("Error Message is present")
                return True
            else:
                self.log.error("*** Error Message was Not present")
                return False
        except:
            self.log.error("*** Exception occurred while checking for Error Message")
            print_stack()
            return False





