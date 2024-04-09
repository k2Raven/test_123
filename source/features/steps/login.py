from behave import given, when, then
from selenium.webdriver.common.by import By


@given(u'Я открыл страницу "Входа"')
def open_login_page(context):
    context.browser.get('http://localhost:8000/accounts/login/')


@when(u'Я ввожу текст "{text}" в поле "{name}"')
def enter_text(context, text, name):
    context.browser.find_element(By.NAME, name).send_keys(text)


@when(u'Я отправляю форму')
def submit_form(context):
    form = context.browser.find_element(By.CSS_SELECTOR, 'form')
    form.submit()


@then(u'Я должен быть на главной странице')
def should_be_at_main(context):
    assert context.browser.current_url == 'http://localhost:8000/'


@then(u"Я должен быть на странице входа")
def should_be_at_login(context):
    assert context.browser.current_url == 'http://localhost:8000/accounts/login/'


@then(u'Я должен видеть сообщение об ошибке с текстом "{text}"')
def see_error_with_text(context, text):
    error = context.browser.find_element(By.CLASS_NAME, 'text-danger')
    assert error.text == text
