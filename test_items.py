from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
"""button.btn:nth-child(3)"""
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.btn:nth-child(3)')