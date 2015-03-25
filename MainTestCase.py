import unittest
from selenium import webdriver
import os


class MainTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.test_url = 'http://ftest.stud.tech-mail.ru'
        cls.login = 'ftest10@tech-mail.ru'
        password_environ = 'TTHA2PASSWORD'
        try:
            cls.password = os.environ[password_environ]
        except KeyError:
            print 'Environment variable "%s" is not defined!' % password_environ

    def test_temp(self):
        self.driver.get(self.test_url)

        button_login = self.driver.find_element_by_css_selector('.button-login')
        button_login.click()

        login_input = self.driver.find_element_by_name('login')
        login_input.send_keys(self.login)

        password_input = self.driver.find_element_by_name('password')
        password_input.send_keys(self.password)

        submit_login_button = self.driver.find_element_by_name('submit_login')
        submit_login_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
