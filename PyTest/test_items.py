import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_button_add_to_basket_is_visible(browser, language):
    link = "http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(language)
    browser.get(link)
    # x = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    # assert x is not None, 'Btn element not found'
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")), "No add to cart button on page")
    # assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
