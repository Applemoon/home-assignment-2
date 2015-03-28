# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from components.pages import AuthPage, CreatePage, TopicPage, BlogPage


class DifferentShortTextTestCase(unittest.TestCase):
    def setUp(self):
        self.username = u'Дядя Миняй'
        self.blog = 'Флудилка'
        self.title = u'ЗаГоЛоВоК'
        self.short_text = u'Короткий текст, отображается в блогах!'
        self.main_text = u'Текст под катом! Отображается внутри топика!'

        browser_environ = 'TTHA2BROWSER'
        browser = os.environ.get(browser_environ, 'CHROME')
        if browser == 'FIREFOX':
            self.driver = webdriver.Firefox()
        elif browser == 'CHROME':
            self.driver = webdriver.Chrome('./chromedriver')

        auth_page = AuthPage(self.driver)
        auth_page.authorize()

        create_page = CreatePage(self.driver)
        create_page.open()
        self.create_form = create_page.get_form()
        self.create_form.blog_select_open()
        self.create_form.blog_select_set_option(self.blog)
        self.create_form.set_title(self.title)
        self.create_form.set_main_text(self.main_text)

        self.topic_page = TopicPage(self.driver)
        self.blog_page = BlogPage(self.driver)

    def tearDown(self):
        # TODO если мы не на страницу блога
            # TODO открыть страницу блога
        self.blog_page.get_topic().delete()
        self.driver.quit()

    def test_check_headers_short_text(self):
        # TODO нажать H4
        # TODO проверить изменения в поле ввода
        self.create_form.set_short_text(self.short_text)
        self.create_form.set_short_text(Keys.ENTER)
        # TODO нажать H5
        # TODO проверить изменения в поле ввода
        self.create_form.set_short_text(self.short_text)
        self.create_form.set_short_text(Keys.ENTER)
        # TODO нажать H4
        # TODO проверить изменения в поле ввода
        self.create_form.set_short_text(self.short_text)
        self.create_form.submit()

        self.topic_page.get_topic().open_blog()

        topic_text = self.blog_page.get_topic().get_text()
        self.assertEqual(self.short_text, topic_text)  # TODO заменить на проверку сообщения

    def test_check_bold_and_italic_short_text(self):
        # TODO нажать B
        # TODO проверить изменения в поле ввода
        self.create_form.set_short_text(self.short_text)
        self.create_form.set_short_text(Keys.ENTER)
        # TODO нажать I
        # TODO проверить изменения в поле ввода
        self.create_form.set_short_text(self.short_text)
        self.create_form.submit()

        self.topic_page.get_topic().open_blog()

        topic_text = self.blog_page.get_topic().get_text()
        self.assertEqual(self.short_text, topic_text)  # TODO заменить на проверку сообщения

    def test_check_quote_short_text(self):
        # TODO нажать ""
        # TODO проверить изменения в поле ввода
        self.create_form.set_short_text(self.short_text)
        self.create_form.submit()

        self.topic_page.get_topic().open_blog()

        topic_text = self.blog_page.get_topic().get_text()
        self.assertEqual(self.short_text, topic_text)  # TODO заменить на проверку цитирования

    def test_check_code_short_text(self):
        # TODO нажать <>
        # TODO проверить изменения в поле ввода
        self.create_form.set_short_text(self.short_text)
        self.create_form.submit()

        self.topic_page.get_topic().open_blog()

        topic_text = self.blog_page.get_topic().get_text()
        self.assertEqual(self.short_text, topic_text)  # TODO заменить на проверку блока кода

    def test_check_list_short_text(self):
        # TODO нажать список
        # TODO проверить изменения в поле ввода
        self.create_form.set_short_text(self.short_text)
        self.create_form.set_short_text(Keys.ENTER)
        # TODO нажать нумерованный список
        # TODO проверить изменения в поле ввода
        self.create_form.set_short_text(self.short_text)
        self.create_form.submit()

        self.topic_page.get_topic().open_blog()

        topic_text = self.blog_page.get_topic().get_text()
        self.assertEqual(self.short_text, topic_text)  # TODO заменить на проверку списков

    def test_check_url_short_text(self):
        # TODO нажать url
        # TODO ввести url
        # TODO ввести текст
        # TODO проверить изменения в поле ввода
        # create_form.set_short_text(self.short_text)
        self.create_form.submit()

        self.topic_page.get_topic().open_blog()

        topic_text = self.blog_page.get_topic().get_text()
        self.assertEqual(self.short_text, topic_text)  # TODO заменить на проверку ссылки

    def test_check_user_short_text(self):
        # TODO нажать пользователя
        # TODO ввести имя пользователя
        # TODO проверить изменения в поле ввода
        # create_form.set_short_text(self.short_text)
        self.create_form.submit()

        self.topic_page.get_topic().open_blog()

        topic_text = self.blog_page.get_topic().get_text()
        self.assertEqual(self.short_text, topic_text)  # TODO заменить на проверку сообщения
