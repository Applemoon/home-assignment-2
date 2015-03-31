# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
import os
from components.pages import AuthPage, CreatePage, TopicPage, BlogPage, DraftPage


class DifferentTopicsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.username = u'Дядя Миняй'
        cls.blog = 'Флудилка'
        cls.title = u'ЗаГоЛоВоК'
        cls.short_text = u'Короткий текст, отображается в блогах!'
        cls.main_text = u'Текст под катом! Отображается внутри топика!'

    @classmethod
    def setUp(cls):
        browser_environ = 'TTHA2BROWSER'
        browser = os.environ.get(browser_environ, 'CHROME')
        if browser == 'FIREFOX':
            cls.driver = webdriver.Firefox()
        elif browser == 'CHROME':
            cls.driver = webdriver.Chrome('./chromedriver')

        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.authorize()

    def tearDown(self):
        self.driver.quit()

    def test_create_simple_topic(self):
        self.assertEqual(self.username, self.auth_page.get_top_menu().get_username())

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

    def test_create_topic_with_voting(self):
        answers = (u'Ответ1', u'Ответ2')
        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.get_form()
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.blog)
        create_form.set_title(self.title)
        create_form.set_short_text(self.short_text)
        create_form.set_main_text(self.main_text)
        create_form.mark_voting()
        create_form.set_voting(u'Текст вопроса', answers[0], answers[1])
        create_form.submit()

        topic_page = TopicPage(self.driver)
        page_answers = topic_page.get_topic().get_answers()
        self.assertEqual(answers, page_answers)

        topic_page.get_topic().open_blog()
        BlogPage(self.driver).get_topic().delete()

    def test_create_topic_without_comments(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.get_form()
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.blog)
        create_form.set_title(self.title)
        create_form.set_short_text(self.short_text)
        create_form.set_main_text(self.main_text)
        create_form.mark_without_comments()
        create_form.submit()

        topic_page = TopicPage(self.driver)
        self.assertFalse(topic_page.get_topic().has_comments())

        topic_page.get_topic().open_blog()
        blog_page = BlogPage(self.driver)
        blog_page.get_topic().delete()

    def test_create_unpublished_topic(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.get_form()
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.blog)
        create_form.set_title(self.title)
        create_form.set_short_text(self.short_text)
        create_form.set_main_text(self.main_text)
        create_form.unmark_publish()
        create_form.submit()

        topic_page = TopicPage(self.driver)
        title = topic_page.get_topic().get_title()
        self.assertEqual(self.title, title)
        text = topic_page.get_topic().get_text()
        self.assertEqual(self.main_text, text)

        topic_page.get_topic().open_blog()

        blog_page = BlogPage(self.driver)
        title = blog_page.get_topic().get_title()
        self.assertNotEqual(self.title, title)
        text = blog_page.get_topic().get_text()
        self.assertNotEqual(self.short_text, text)

        draft_page = DraftPage(self.driver)
        draft_page.open()
        title = draft_page.get_topic().get_title()
        self.assertEqual(self.title, title)
        text = draft_page.get_topic().get_text()
        self.assertEqual(self.short_text, text)

        draft_page.get_topic().delete()
