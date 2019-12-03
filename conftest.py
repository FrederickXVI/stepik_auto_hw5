import pytest
from selenium import webdriver


# добавляем параметр --language для pytest
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language")


# возвращаем значение параметра --language
@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("--language")


@pytest.fixture(scope="class")
def get_login():
    return "dimatest@test.ru"


@pytest.fixture(scope="class")
def get_password():
    return "dimatest123"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()