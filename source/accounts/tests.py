# from django.test import TestCase
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
# from django.shortcuts import reverse
# import time
#
# path = 'http://127.0.0.1:8000'
#
#
# class LoginTest(TestCase):
#     def setUp(self):
#         self.driver = Chrome()
#
#     def tearDown(self):
#         self.driver.close()
#
#     def test_log_in_as_admin(self):
#         self.driver.get(path + reverse('accounts:login'))
#         self.driver.find_element(By.NAME, 'username').send_keys('admin')
#         self.driver.find_element(By.NAME, 'password').send_keys('admin')
#         self.driver.find_element(By.XPATH, '/html/body/div/form/button').click()
#         assert self.driver.current_url == path + reverse('index')
#         # self.assertEqual(self.driver.current_url, path + reverse('index'))
#
#     def test_login_error(self):
#         self.driver.get(path + reverse('accounts:login'))
#         self.driver.find_element(By.XPATH, '/html/body/div/form/button').click()
#         error = self.driver.find_element(By.CSS_SELECTOR, '.text-danger')
#         assert error.text == 'Неверное имя пользователя или пароль.'