import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


# добавляем параметр --language --browser_name для pytest
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def get_login():
    return "dimatest@test.ru"


@pytest.fixture(scope="function")
def get_password():
    return "dimatest123"


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.maximize_window()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot('Screenshots/screenshot-%s.png' % now)
    print("\nquit browser..")
    browser.quit()