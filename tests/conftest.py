from selenium import webdriver
import pytest
from pages.login_page.login_page import LoginPage
from base.webdriver_factory import get_browser_driver


@pytest.yield_fixture(scope="class")
def class_setup(request, browser, osType):      # Using the browser and osType fixtures here as arguments
    baseURL = "https://letskodeit.teachable.com/"
    driver = get_browser_driver(browser, osType)    # Using the browser and osType fixtures here as arguments
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    lp = LoginPage(driver)
    lp.login_user("test@email.com", "abcabc")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


@pytest.yield_fixture(scope="module")
def method_setup(request, browser, osType):      # Using the browser and osType fixtures here as arguments
    baseURL = "https://letskodeit.teachable.com/"
    driver = get_browser_driver(browser, osType)    # Using the browser and osType fixtures here as arguments
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    lp = LoginPage(driver)
    lp.login_user("test@email.com", "abcabc")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")