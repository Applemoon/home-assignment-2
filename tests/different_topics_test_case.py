# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver

from components.pages import AuthPage, CreatePage, TopicPage, BlogPage, DraftPage
import config


class DifferentTopicsTestCase(unittest.TestCase):
    def setUp(self):
        if config.browser == 'FIREFOX':
            self.driver = webdriver.Firefox()
        elif config.browser == 'CHROME':
            self.driver = webdriver.Chrome('./chromedriver')

        self.auth_page = AuthPage(self.driver)
        self.auth_page.authorize()

        self.topic_page = TopicPage(self.driver)
        self.blog_page = BlogPage(self.driver)
        self.draft_page = DraftPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_create_simple_topic(self):
        self.assertEqual(config.username, self.auth_page.get_top_menu().get_username())

        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.get_form()
        create_form.blog_select_open()
        create_form.blog_select_set_option(config.blog)
        create_form.set_title(config.title)
        create_form.set_short_text(config.short_text)
        create_form.set_main_text(config.main_text)
        create_form.submit()

        topic_title = self.topic_page.get_topic().get_title()
        topic_text = self.topic_page.get_topic().get_text()
        try:
            self.assertEqual(config.title, topic_title)
            self.assertEqual(config.main_text, topic_text)
        except AssertionError:
            self.topic_page.get_topic().delete()
            raise AssertionError

        self.topic_page.get_topic().open_blog()

        topic_title = self.blog_page.get_topic().get_title()
        topic_text = self.blog_page.get_topic().get_text()
        try:
            self.assertEqual(config.title, topic_title)
            self.assertEqual(config.short_text, topic_text)
        except AssertionError:
            self.blog_page.get_topic().delete()
            raise AssertionError

        self.blog_page.get_topic().delete()

        topic_title = self.blog_page.get_topic().get_title()
        topic_text = self.blog_page.get_topic().get_text()
        self.assertNotEqual(config.title, topic_title)
        self.assertNotEqual(config.short_text, topic_text)

    def test_create_topic_with_voting(self):
        answers = (u'Ответ1', u'Ответ2')
        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.get_form()
        create_form.blog_select_open()
        create_form.blog_select_set_option(config.blog)
        create_form.set_title(config.title)
        create_form.set_short_text(config.short_text)
        create_form.set_main_text(config.main_text)
        create_form.mark_voting()
        create_form.set_voting(u'Текст вопроса', answers[0], answers[1])
        create_form.submit()

        has_answers = self.topic_page.get_topic().has_answers(answers[0], answers[1])
        try:
            self.assertTrue(has_answers)
        except AssertionError:
            self.topic_page.get_topic().delete()
            raise AssertionError

        self.topic_page.get_topic().delete()

    def test_create_topic_without_comments(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.get_form()
        create_form.blog_select_open()
        create_form.blog_select_set_option(config.blog)
        create_form.set_title(config.title)
        create_form.set_short_text(config.short_text)
        create_form.set_main_text(config.main_text)
        create_form.mark_without_comments()
        create_form.submit()

        try:
            self.assertFalse(self.topic_page.get_topic().has_comments())
        except AssertionError:
            self.topic_page.get_topic().delete()
            raise AssertionError

        self.topic_page.get_topic().delete()

    def test_create_unpublished_topic(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        create_form = create_page.get_form()
        create_form.blog_select_open()
        create_form.blog_select_set_option(config.blog)
        create_form.set_title(config.title)
        create_form.set_short_text(config.short_text)
        create_form.set_main_text(config.main_text)
        create_form.unmark_publish()
        create_form.submit()

        title = self.topic_page.get_topic().get_title()
        text = self.topic_page.get_topic().get_text()
        try:
            self.assertEqual(config.title, title)
            self.assertEqual(config.main_text, text)
        except AssertionError:
            self.topic_page.get_topic().delete()
            raise AssertionError

        self.draft_page.open()

        title = self.draft_page.get_topic().get_title()
        text = self.draft_page.get_topic().get_text()
        try:
            self.assertEqual(config.title, title)
            self.assertEqual(config.short_text, text)
        except AssertionError:
            self.draft_page.get_topic().delete()
            raise AssertionError

        self.draft_page.get_topic().open_blog()

        blog_page = BlogPage(self.driver)
        title = blog_page.get_topic().get_title()
        text = blog_page.get_topic().get_text()
        try:
            self.assertNotEqual(config.title, title)
            self.assertNotEqual(config.short_text, text)
        except AssertionError:
            blog_page.get_topic().delete()
            raise AssertionError

        blog_page.get_topic().delete()