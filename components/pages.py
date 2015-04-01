import os
import urlparse

from selenium.webdriver.support.wait import WebDriverWait

from components.page_components import AuthForm, CreateForm, Component, Topic
import config


class Page(object):
    BASE_URL = 'http://ftest.stud.tech-mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthPage(Page):
    PATH = ''

    def get_form(self):
        return AuthForm(self.driver)

    def get_top_menu(self):
        return TopMenu(self.driver)

    def authorize(self):
        self.open()
        auth_form = self.get_form()
        auth_form.open_form()
        auth_form.set_login(config.login)
        auth_form.set_password(config.password)
        auth_form.submit()


class TopMenu(Component):
    USERNAME = '//a[@class="username"]'

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )


class CreatePage(Page):
    PATH = '/blog/topic/create/'

    def get_form(self):
        return CreateForm(self.driver)


class TopicPage(Page):
    def get_topic(self):
        return Topic(self.driver)


class BlogPage(Page):
    def get_topic(self):
        return Topic(self.driver)


class DraftPage(Page):
    PATH = '/blog/topics/draft/'

    def get_topic(self):
        return Topic(self.driver)