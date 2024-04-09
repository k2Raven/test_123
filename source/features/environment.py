from behave import fixture, use_fixture
from selenium.webdriver import Chrome, ChromeOptions


@fixture
def browser_chrome(context):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("headless")
    context.browser = Chrome(options=chrome_options)
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(browser_chrome, context)