import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language',action = 'store', default = None,
                     help = "Choose language: ru or es")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('language')
    browser = None
    if browser_name == 'es':
        print('\nstart browser with es lang.')
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--language should be es or es)")
    yield browser
    print("\nquit browser..")
    browser.quit()