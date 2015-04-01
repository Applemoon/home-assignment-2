# -*- coding: utf-8 -*-

import unittest
import urlparse
from selenium import webdriver
import os
from components.pages import AuthPage, CreatePage, TopicPage, BlogPage, Page


class DifferentTextTestCase(unittest.TestCase):
    def setUp(self):
        self.username = u'Дядя Миняй'
        self.blog = 'Флудилка'
        self.title = u'ЗаГоЛоВоК'
        short_text = u'Короткий текст, отображается в блогах!'
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
        self.create_form.set_short_text(short_text)

        self.topic_page = TopicPage(self.driver)
        self.blog_page = BlogPage(self.driver)

    def tearDown(self):
        self.topic_page.get_topic().delete()
        self.driver.quit()

    def test_bold(self):
        self.create_form.click_bold_for_main()
        self.assertTrue(self.create_form.bold_appear())
        self.create_form.send_text(self.main_text)
        self.create_form.submit()

        self.assertTrue(self.topic_page.get_topic().is_strong())

    def test_italic(self):
        self.create_form.click_italic_for_main()
        self.assertTrue(self.create_form.italic_appear())
        self.create_form.send_text(self.main_text)
        self.create_form.submit()

        self.assertTrue(self.topic_page.get_topic().is_italic())

    def test_quote(self):
        self.create_form.click_quote_for_main()
        self.assertTrue(self.create_form.quote_appear())
        self.create_form.send_text(self.main_text)
        self.create_form.submit()

        self.assertTrue(self.topic_page.get_topic().has_quote())

    def test_list(self):
        self.create_form.click_list_for_main()
        self.assertTrue(self.create_form.list_appear())
        self.create_form.send_text(self.main_text)
        self.create_form.submit()

        self.assertTrue(self.topic_page.get_topic().has_list())

    def test_check_ordered_list(self):
        self.create_form.click_ordered_list_for_main()
        self.assertTrue(self.create_form.ordered_list_appear())
        self.create_form.send_text(self.main_text)
        self.create_form.submit()

        self.assertTrue(self.topic_page.get_topic().has_ordered_list())

    def test_link(self):
        link_name = u'Это ссылка'
        url = 'http://ya.ru/'

        self.create_form.click_link_for_main()
        popup = self.driver.switch_to.alert
        popup.send_keys(url)
        popup.accept()
        self.assertTrue(self.create_form.link_appear('', url))
        self.create_form.send_text(link_name)
        self.create_form.submit()

        self.assertTrue(self.topic_page.get_topic().link_in_text(link_name, url))

    def test_put_img(self):
        url = 'http://static014.cmtt.ru/paper-media/mail-ru/5885d14c4be65ac30803.png'

        self.create_form.click_put_img_for_main()
        popup = self.driver.switch_to.alert
        popup.send_keys(url)
        popup.accept()
        self.assertTrue(self.create_form.img_link_appear(url))
        self.create_form.submit()

        self.assertTrue(self.topic_page.get_topic().img_in_text(url))

    @unittest.skip('not supported')  # TODO
    def test_check_upload_img(self):
        self.create_form.set_main_text(self.main_text)
        self.create_form.submit()

    def test_add_user(self):
        url = '/profile/d.minyaj/'
        last_name = self.username.split()[1]

        self.create_form.click_add_user_for_main()
        self.create_form.search_user(last_name)
        self.create_form.choose_user()
        self.assertTrue(self.create_form.link_appear(self.username, url))
        self.create_form.submit()

        right_link = urlparse.urljoin(Page.BASE_URL, url)
        is_link_in_text = self.topic_page.get_topic().link_in_text(self.username, right_link)
        self.assertTrue(is_link_in_text)

    @unittest.skip('not supported')  # TODO
    def test_check_preview(self):
        self.create_form.set_main_text(self.main_text)
        self.create_form.submit()