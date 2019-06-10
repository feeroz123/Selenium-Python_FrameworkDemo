from utilities.test_status import TestStatus
from pages.courses_page.courses_page import CoursesPage
from ddt import ddt, data, unpack
from utilities.csv_reader import get_csv_data
import unittest
import pytest


@ddt
class CourseTestsCSVReader(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.cp = CoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.usefixtures("method_setup")
    @data(*get_csv_data("tests/testdata.csv"))
    @unpack
    def test_enrollCourse(self, card_number, card_expiry_date, card_cvc, country, postal_code):
        self.cp.enroll_javascript_course(card_number, card_expiry_date, card_cvc, country, postal_code)
        result = self.cp.verify_error_presence()
        self.ts.mark_final("Enroll Course", result, "Course enrollment verified")


