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

        auth_page = AuthPage(self.driver)
        auth_page.authorize()

        create_page = CreatePage(self.driver)
        create_page.open()
        self.create_form = create_page.get_form()
        self.create_form.blog_select_open()
        self.create_form.blog_select_set_option(config.blog)
        self.create_form.set_title(config.title)
        self.create_form.set_short_text(config.short_text)

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
        self.create_form.click_bold_for_main()
        self.assertTrue(self.create_form.bold_appear())
        self.create_form.send_text(config.main_text)
        self.create_form.submit()

        is_strong = self.topic_page.get_topic().is_strong(config.main_text)
        self.assertTrue(is_strong)

    def test_italic(self):
        self.create_form.click_italic_for_main()
        self.assertTrue(self.create_form.italic_appear())
        self.create_form.send_text(config.main_text)
        self.create_form.submit()

        is_italic = self.topic_page.get_topic().is_italic(config.main_text)
        self.assertTrue(is_italic)

    def test_quote(self):
        self.create_form.click_quote_for_main()
        self.assertTrue(self.create_form.quote_appear())
        self.create_form.send_text(config.main_text)
        self.create_form.submit()

        has_quote = self.topic_page.get_topic().has_quote(config.main_text)
        self.assertTrue(has_quote)

    def test_list(self):
        self.create_form.click_list_for_main()
        self.assertTrue(self.create_form.list_appear())
        self.create_form.send_text(config.main_text)
        self.create_form.submit()

        has_list = self.topic_page.get_topic().has_list(config.main_text)
        self.assertTrue(has_list)

    def test_check_ordered_list(self):
        self.create_form.click_ordered_list_for_main()
        self.assertTrue(self.create_form.ordered_list_appear())
        self.create_form.send_text(config.main_text)
        self.create_form.submit()

        has_ordered_list = self.topic_page.get_topic().has_ordered_list(config.main_text)
        self.assertTrue(has_ordered_list)

    def test_link(self):
        link_name = u'Это ссылка'

        self.create_form.click_link_for_main()
        popup = self.driver.switch_to.alert
        popup.send_keys(config.link)
        popup.accept()
        self.assertTrue(self.create_form.link_appear('', config.link))
        self.create_form.send_text(link_name)
        self.create_form.submit()

        self.assertTrue(self.topic_page.get_topic().link_in_text(link_name, config.link))

    def test_put_img(self):
        self.create_form.click_put_img_for_main()
        popup = self.driver.switch_to.alert
        popup.send_keys(config.image_url)
        popup.accept()
        self.assertTrue(self.create_form.img_link_appear(config.image_url))
        self.create_form.submit()

        self.assertTrue(self.topic_page.get_topic().img_in_text(config.image_url))

    def test_check_upload_img(self):
        url = self.create_form.upload_img(config.local_image_path)
        self.assertTrue(self.create_form.img_link_appear(url))
        self.create_form.submit()

        self.assertTrue(self.topic_page.get_topic().img_in_text(url))

    def test_add_user(self):
        last_name = config.username.split()[1]

        self.create_form.click_add_user_for_main()
        self.create_form.search_user(last_name)
        self.create_form.choose_user()
        self.assertTrue(self.create_form.link_appear(config.username, config.user_url))
        self.create_form.submit()

        is_link_in_text = self.topic_page.get_topic().link_in_text(config.username, config.user_url)
        self.assertTrue(is_link_in_text)
