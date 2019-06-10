from utilities.test_status import TestStatus
from pages.courses_page.courses_page import CoursesPage
from ddt import ddt, data, unpack
import unittest
import pytest


@pytest.mark.usefixtures("class_setup")
@ddt
class CourseTestsMultipleDDT(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.cp = CoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @data(("5241930034983003", "09/23", "234", "India", "560037"),
          ("5241930034983003", "08/21", "555", "Nepal", "444444"))
    @unpack
    def test_enrollCourse(self, card_number, card_expiry_date, card_cvc, country, postal_code):
        self.cp.enroll_javascript_course(card_number, card_expiry_date, card_cvc, country, postal_code)
        result = self.cp.verify_error_presence()
        self.ts.mark_final("Enroll Course", result, "Course enrollment verified")


