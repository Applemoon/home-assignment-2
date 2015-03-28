# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
import os
from components.pages import AuthPage, CreatePage, TopicPage, BlogPage


class DifferentTopicsTestCase(unittest.TestCase):
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

    def tearDown(self):
        # TODO вынести обязательные операции
        self.driver.quit()

    def test_create_simple_topic(self):
        self.assertEqual(self.username, AuthPage(self.driver).get_top_menu().get_username())

        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.get_form()
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.blog)
        create_form.set_title(self.title)
        create_form.set_short_text(self.short_text)
        create_form.set_main_text(self.main_text)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.get_topic().get_title()
        self.assertEqual(self.title, topic_title)
        topic_text = topic_page.get_topic().get_text()
        self.assertEqual(self.main_text, topic_text)

        topic_page.get_topic().open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.get_topic().get_title()
        self.assertEqual(self.title, topic_title)
        topic_text = blog_page.get_topic().get_text()
        self.assertEqual(self.short_text, topic_text)

        blog_page.get_topic().delete()
        topic_title = blog_page.get_topic().get_title()
        self.assertNotEqual(self.title, topic_title)
        topic_text = blog_page.get_topic().get_text()
        self.assertNotEqual(self.short_text, topic_text)

    def test_create_topic_with_voiting(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.get_form()
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.blog)
        create_form.set_title(self.title)
        create_form.set_short_text(self.short_text)
        create_form.set_main_text(self.main_text)
        # TODO отметить галочку
        # TODO заполнить поля
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.get_topic().get_title()
        self.assertEqual(self.title, topic_title)
        topic_text = topic_page.get_topic().get_text()
        self.assertEqual(self.main_text, topic_text)
        # TODO проверить, на месте ли опрос

        topic_page.get_topic().open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.get_topic().get_title()
        self.assertEqual(self.title, topic_title)
        topic_text = blog_page.get_topic().get_text()
        self.assertEqual(self.short_text, topic_text)

        blog_page.get_topic().delete()
        topic_title = blog_page.get_topic().get_title()
        self.assertNotEqual(self.title, topic_title)
        topic_text = blog_page.get_topic().get_text()
        self.assertNotEqual(self.short_text, topic_text)

    def create_topic_without_comments(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.get_form()
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.blog)
        create_form.set_title(self.title)
        create_form.set_short_text(self.short_text)
        create_form.set_main_text(self.main_text)
        # TODO отметить галочку
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = topic_page.get_topic().get_title()
        self.assertEqual(self.title, topic_title)
        topic_text = topic_page.get_topic().get_text()
        self.assertEqual(self.main_text, topic_text)
        # TODO проверить, можно ли оставлять комменты

        topic_page.get_topic().open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.get_topic().get_title()
        self.assertEqual(self.title, topic_title)
        topic_text = blog_page.get_topic().get_text()
        self.assertEqual(self.short_text, topic_text)

        blog_page.get_topic().delete()
        topic_title = blog_page.get_topic().get_title()
        self.assertNotEqual(self.title, topic_title)
        topic_text = blog_page.get_topic().get_text()
        self.assertNotEqual(self.short_text, topic_text)

    def create_unpublished_topic(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.get_form()
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.blog)
        create_form.set_title(self.title)
        create_form.set_short_text(self.short_text)
        create_form.set_main_text(self.main_text)
        # TODO снять галочку
        create_form.submit()

        # TODO проверить "опубликованность"
        topic_page = TopicPage(self.driver)
        topic_title = topic_page.get_topic().get_title()
        self.assertEqual(self.title, topic_title)
        topic_text = topic_page.get_topic().get_text()
        self.assertEqual(self.main_text, topic_text)

        topic_page.get_topic().open_blog()

        blog_page = BlogPage(self.driver)
        topic_title = blog_page.get_topic().get_title()
        self.assertEqual(self.title, topic_title)
        topic_text = blog_page.get_topic().get_text()
        self.assertEqual(self.short_text, topic_text)

        blog_page.get_topic().delete()
        topic_title = blog_page.get_topic().get_title()
        self.assertNotEqual(self.title, topic_title)
        topic_text = blog_page.get_topic().get_text()
        self.assertNotEqual(self.short_text, topic_text)
