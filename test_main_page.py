import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
from .pages.main_page import MainPage

# pytest -v --tb=line --language=en test_main_page.py
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# browser.get(link)
# login_link = browser.find_element_by_css_selector("#login_link")
# login_link.click()

# def test_espaniolLocation(browser,link):
#     browser.get(link)
#     time.sleep(30)
#     button = WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")))
#     assert button is not None, "Button not found"
#     assert (button.text=="Añadir al carrito")
