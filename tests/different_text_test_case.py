# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from components.pages import AuthPage, CreatePage, TopicPage, BlogPage
import config


class DifferentTextTestCase(unittest.TestCase):
    def setUp(self):
        if config.browser == 'FIREFOX':
            self.driver = webdriver.Firefox()
        elif config.browser == 'CHROME':
            self.driver = webdriver.Chrome('./chromedriver')

        self.driver.implicitly_wait(2)

        auth_page = AuthPage(self.driver)
        auth_page.authorize()

        create_page = CreatePage(self.driver)
        create_page.open()
        self.create_form = create_page.get_form()
        self.create_form.blog_select_open()
        self.create_form.blog_select_set_option(config.blog)
        self.create_form.set_title(config.title)

        self.topic_page = TopicPage(self.driver)
        self.blog_page = BlogPage(self.driver)

    def tearDown(self):
        try:
            self.topic_page.get_topic().delete()
        except NoSuchElementException:
            pass
        finally:
            self.driver.quit()

    def test_bold(self):
        self.create_form.click_bold()
        self.assertTrue(self.create_form.bold_appear())
        self.create_form.send_text(config.topic_text)
        self.create_form.submit()

        is_strong = self.topic_page.get_topic().is_strong(config.topic_text)
        self.assertTrue(is_strong)

    def test_italic(self):
        self.create_form.click_italic()
        self.assertTrue(self.create_form.italic_appear())
        self.create_form.send_text(config.topic_text)
        self.create_form.submit()

        is_italic = self.topic_page.get_topic().is_italic(config.topic_text)
        self.assertTrue(is_italic)

    def test_quote(self):
        self.create_form.click_quote()
        self.assertTrue(self.create_form.quote_appear())
        self.create_form.send_text(config.topic_text)
        self.create_form.submit()

        has_quote = self.topic_page.get_topic().has_quote(config.topic_text)
        self.assertTrue(has_quote)

    def test_list(self):
        self.create_form.click_list()
        self.assertTrue(self.create_form.list_appear())
        self.create_form.send_text(config.topic_text)
        self.create_form.submit()

        has_list = self.topic_page.get_topic().has_list(config.topic_text)
        self.assertTrue(has_list)

    def test_check_ordered_list(self):
        self.create_form.click_ordered_list()
        self.assertTrue(self.create_form.ordered_list_appear())
        self.create_form.send_text(config.topic_text)
        self.create_form.submit()

        has_ordered_list = self.topic_page.get_topic().has_ordered_list(config.topic_text)
        self.assertTrue(has_ordered_list)

    # def test_link(self):
    #     link_name = u'Это ссылка'
    #
    #     self.create_form.click_link()
    #     popup = self.driver.switch_to.alert TODO не переключается!
    #     popup.send_keys(config.link)
    #     popup.accept()
    #     self.assertTrue(self.create_form.link_appear('', config.link))
    #     self.create_form.send_text(link_name)
    #     self.create_form.submit()
    #
    #     self.assertTrue(self.topic_page.get_topic().link_in_text(link_name, config.link))

    def test_add_img_from_pc(self):
        self.create_form.click_put_img()
        self.create_form.chose_img_from_pc(config.local_image_path)
        self.create_form.submit()

        # self.assertTrue(self.topic_page.get_topic().img_in_text(u'http://' + config.local_image_path)) TODO другой путь!

    def test_add_img_from_internet(self):
        self.create_form.click_put_img()
        self.create_form.chose_img_from_internet(config.image_url)
        self.create_form.submit()

        self.assertTrue(self.topic_page.get_topic().img_in_text(u'http://' + config.image_url))

    def test_add_user(self):
        last_name = config.username.split()[1]

        self.create_form.click_add_user()
        self.create_form.search_user(last_name)
        self.create_form.choose_user()
        user_appear = self.create_form.user_appear(config.username, config.user_url)
        self.assertTrue(user_appear)
        self.create_form.submit()

        is_link_in_text = self.topic_page.get_topic().link_in_text(config.username, config.user_url)
        self.assertTrue(is_link_in_text)
