from utilities.test_status import TestStatus
from pages.courses_page.courses_page import CoursesPage
import unittest
import pytest


@pytest.mark.usefixtures("class_setup")
class CourseTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.cp = CoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    def test_enrollCourse(self):
        self.cp.enroll_javascript_course("5241930034983003", "09/23", "234", "India", "560037")
        result = self.cp.verify_error_presence()
        self.ts.mark_final("Enroll Course", result, "Course enrollment verified")


