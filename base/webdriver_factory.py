from selenium import webdriver
import pytest


def get_browser_driver(browser, osType):
    if browser == "chrome":
        return webdriver.Chrome()
    else:
        print("Default browser = Firefox")
        return webdriver.Firefox()

    if osType == "Windows":
        print("Running tests on Windows")
    else:
        print("Running tests on Linux")
