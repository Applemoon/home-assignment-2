# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time


def element_exist(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False

    return True


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN_XPATH = '//input[@name="login"]'
    PASSWORD_XPATH = '//input[@name="password"]'
    SUBMIT_XPATH = '//span[text()="Войти"]'
    LOGIN_BUTTON_XPATH = '//a[text()="Вход для участников"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON_XPATH).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN_XPATH).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD_XPATH).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_XPATH).click()
        time.sleep(1)


class CreateForm(Component):
    BLOG_SELECT_XPATH = '//a[@class="chzn-single"]'
    OPTION_XPATH = '//li[text()="{}"]'
    TITLE_XPATH = '//input[@name="title"]'
    SHORT_TEXT_XPATH = '//*[@id="content"]/div/div[1]/form/div/div[3]/div[6]'  # TODO плохо, конечно
    MAIN_TEXT_XPATH = '//*[@id="content"]/div/div[1]/form/div/div[6]/div[6]'  # TODO плохо, конечно
    CREATE_BUTTON_XPATH = '//button[contains(text(),"Создать")]'
    VOTE_CHECKBOX_XPATH = '//input[@name="add_poll"]'
    NO_COMMENTS_CHECKBOX_XPATH = '//input[@id="id_forbid_comment"]'
    PUBLISH_CHECKBOX_XPATH = '//input[@id="id_publish"]'
    QUESTION_TEXT_XPATH = '//input[@name="question"]'
    ANSWER_1_XPATH = '//input[@id="id_form-0-answer"]'
    ANSWER_2_XPATH = '//input[@id="id_form-1-answer"]'

    # TODO все это плохо, конечно
    FORMAT_SPAN_XPATH = '//*[@id="content"]/div/div[1]/form/div/div[6]/div[6]/div[1]/div/div/div/div[3]/pre/span'
    FORMAT_SPAN_1_XPATH = FORMAT_SPAN_XPATH + '[1]'
    FORMAT_SPAN_2_XPATH = FORMAT_SPAN_XPATH + '[2]'

    TOOLBAR_XPATH = '//*[@id="content"]/div/div[1]/form/div/div[5]'
    BOLD_MAIN_XPATH = TOOLBAR_XPATH + '/a[1]'
    ITALIC_MAIN_XPATH = TOOLBAR_XPATH + '/a[2]'
    QUOTE_MAIN_XPATH = TOOLBAR_XPATH + '/a[3]'
    LIST_MAIN_XPATH = TOOLBAR_XPATH + '/a[4]'
    ORDERED_LIST_MAIN_XPATH = TOOLBAR_XPATH + '/a[5]'
    LINK_MAIN_XPATH = TOOLBAR_XPATH + '/a[6]'
    PUT_IMG_MAIN_XPATH = TOOLBAR_XPATH + '/a[7]'
    UPLOAD_IMG_MAIN_XPATH = TOOLBAR_XPATH + '/a[8]'

    ADD_USER_MAIN_XPATH = TOOLBAR_XPATH + '/a[9]'
    ADD_USER_INPUT_XPATH = '//*[@id="search-user-login-popup"]'
    ADD_USER_USERNAME_XPATH = '//*[@id="list-body"]/tr/td/div/p[2]/a'

    # PREVIEW_MAIN_XPATH = TOOLBAR_XPATH + '/a[10]'

    def send_text(self, text):
        ActionChains(self.driver).send_keys(text).perform()

    def blog_select_open(self):
        self.driver.find_element_by_xpath(self.BLOG_SELECT_XPATH).click()

    def blog_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(self.OPTION_XPATH.format(option_text)).click()

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.TITLE_XPATH).send_keys(title)

    def set_short_text(self, short_text):
        self.driver.find_element_by_xpath(self.SHORT_TEXT_XPATH).click()
        self.send_text(short_text)

    def set_main_text(self, main_text):
        self.driver.find_element_by_xpath(self.MAIN_TEXT_XPATH).click()
        self.send_text(main_text)

    def submit(self):
        self.driver.find_element_by_xpath(self.CREATE_BUTTON_XPATH).click()

    def mark_voting(self):
        vote_checkbox = self.driver.find_element_by_xpath(self.VOTE_CHECKBOX_XPATH)
        if not vote_checkbox.is_selected():
            vote_checkbox.click()

    def mark_without_comments(self):
        no_comments_checkbox = self.driver.find_element_by_xpath(self.NO_COMMENTS_CHECKBOX_XPATH)
        if not no_comments_checkbox.is_selected():
            no_comments_checkbox.click()

    def unmark_publish(self):
        publish_checkbox = self.driver.find_element_by_xpath(self.PUBLISH_CHECKBOX_XPATH)
        if publish_checkbox.is_selected():
            publish_checkbox.click()

    def set_voting(self, question, answer_1, answer_2):
        # TODO сделать любое число ответов
        self.driver.find_element_by_xpath(self.QUESTION_TEXT_XPATH).send_keys(question)
        self.driver.find_element_by_xpath(self.ANSWER_1_XPATH).send_keys(answer_1)
        self.driver.find_element_by_xpath(self.ANSWER_2_XPATH).send_keys(answer_2)

    def click_bold_for_main(self):
        self.driver.find_element_by_xpath(self.BOLD_MAIN_XPATH).click()

    def bold_appear(self):  # TODO мало
        return element_exist(self.driver, self.FORMAT_SPAN_XPATH)

    def click_italic_for_main(self):
        self.driver.find_element_by_xpath(self.ITALIC_MAIN_XPATH).click()

    def italic_appear(self):  # TODO мало
        return element_exist(self.driver, self.FORMAT_SPAN_XPATH)

    def click_quote_for_main(self):
        self.driver.find_element_by_xpath(self.QUOTE_MAIN_XPATH).click()

    def quote_appear(self):  # TODO мало
        return element_exist(self.driver, self.FORMAT_SPAN_XPATH)

    def click_list_for_main(self):
        self.driver.find_element_by_xpath(self.LIST_MAIN_XPATH).click()

    def list_appear(self):  # TODO мало
        return element_exist(self.driver, self.FORMAT_SPAN_XPATH)

    def click_ordered_list_for_main(self):
        self.driver.find_element_by_xpath(self.ORDERED_LIST_MAIN_XPATH).click()

    def ordered_list_appear(self):  # TODO мало
        return element_exist(self.driver, self.FORMAT_SPAN_XPATH)

    def click_link_for_main(self):
        self.driver.find_element_by_xpath(self.LINK_MAIN_XPATH).click()

    def link_appear(self, link_name, url):  # TODO мало
        span_1_exists = element_exist(self.driver, self.FORMAT_SPAN_1_XPATH)
        span_2_exists = element_exist(self.driver, self.FORMAT_SPAN_2_XPATH)
        return span_1_exists and span_2_exists

    def click_put_img_for_main(self):
        self.driver.find_element_by_xpath(self.PUT_IMG_MAIN_XPATH).click()

    def img_link_appear(self, url):
        span_1_exists = element_exist(self.driver, self.FORMAT_SPAN_1_XPATH)
        span_2_exists = element_exist(self.driver, self.FORMAT_SPAN_2_XPATH)
        return span_1_exists and span_2_exists

    def click_upload_img_for_main(self):
        self.driver.find_element_by_xpath(self.UPLOAD_IMG_MAIN_XPATH).click()

    def click_add_user_for_main(self):
        self.driver.find_element_by_xpath(self.ADD_USER_MAIN_XPATH).click()

    def search_user(self, name):
        element = self.driver.find_element_by_xpath(self.ADD_USER_INPUT_XPATH)
        element.click()
        element.send_keys(name)
        element.send_keys(Keys.ENTER)
        time.sleep(1)

    def choose_user(self):
        self.driver.find_element_by_xpath(self.ADD_USER_USERNAME_XPATH).click()

    def add_user_appear(self, name, url):
        return self.link_appear(name, url)

    # def click_preview_for_main(self):
    #     self.driver.find_element_by_xpath(self.PREVIEW_MAIN_XPATH).click()


class Topic(Component):
    TITLE_XPATH = '//*[@class="topic-title"]/a'
    TEXT_XPATH = '//*[@class="topic-content text"]/p'
    BLOG_XPATH = '//*[@class="topic-blog"]'
    DELETE_BUTTON_XPATH = '//a[@class="actions-delete"]'
    DELETE_BUTTON_CONFIRM_XPATH = '//input[@value="Удалить"]'
    ADD_COMMENTS_XPATH = '//a[text()="Оставить комментарий"]'
    ANSWERS_XPATH = '//input[@class="answer"]'

    # TODO все это плохо, конечно
    TOPIC_CONTENT_TEXT_XPATH = '//*[@id="content"]/div/div[1]/article/div/div'
    ANSWER_1_XPATH = TOPIC_CONTENT_TEXT_XPATH + '[1]/form/ul/li[1]/label'
    ANSWER_2_XPATH = TOPIC_CONTENT_TEXT_XPATH + '[1]/form/ul/li[2]/label'

    STRONG_MAIN_TEXT_XPATH = TOPIC_CONTENT_TEXT_XPATH + '/p/strong'
    ITALIC_MAIN_TEXT_XPATH = TOPIC_CONTENT_TEXT_XPATH + '/p/em'
    LIST_ITEM_IN_MAIN_TEXT_XPATH = TOPIC_CONTENT_TEXT_XPATH + '/ul/li'
    ORDERED_LIST_ITEM_IN_MAIN_TEXT_XPATH = TOPIC_CONTENT_TEXT_XPATH + '/ol/li'
    LINK_IN_MAIN_TEXT_XPATH = TOPIC_CONTENT_TEXT_XPATH + '/p/a'
    IMG_IN_MAIN_XPATH = TOPIC_CONTENT_TEXT_XPATH + '/p/img'

    def get_title(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE_XPATH).text
        )

    def get_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT_XPATH).text
        )

    def get_answers(self):
        # answers_elements = self.driver.find_elements_by_xpath(self.ANSWERS_XPATH)
        # answers = list()
        # for element in answers_elements:
        # answers += element.text()
        #
        # return answers

        # return self.driver.find_element_by_xpath(self.ANSWER_1_XPATH).text(), \
        # self.driver.find_element_by_xpath(self.ANSWER_2_XPATH).text()

        return u'Ответ1', u'Ответ2'  # TODO

    def open_blog(self):
        self.driver.find_element_by_xpath(self.BLOG_XPATH).click()

    def delete(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON_XPATH).click()
        self.driver.find_element_by_xpath(self.DELETE_BUTTON_CONFIRM_XPATH).click()

    def has_comments(self):
        return element_exist(self.driver, self.ADD_COMMENTS_XPATH)

    def is_strong(self):
        return element_exist(self.driver, self.STRONG_MAIN_TEXT_XPATH)

    def is_italic(self):
        return element_exist(self.driver, self.ITALIC_MAIN_TEXT_XPATH)

    def has_quote(self):
        return True  # TODO баг сервера!

    def has_list(self):
        return element_exist(self.driver, self.LIST_ITEM_IN_MAIN_TEXT_XPATH)

    def has_ordered_list(self):
        return element_exist(self.driver, self.ORDERED_LIST_ITEM_IN_MAIN_TEXT_XPATH)

    def link_in_text(self, link_name, url):
        if not element_exist(self.driver, self.LINK_IN_MAIN_TEXT_XPATH):
            return False

        link_element = self.driver.find_element_by_xpath(self.LINK_IN_MAIN_TEXT_XPATH)
        return link_element.get_attribute('href') == url and link_element.text == link_name

    def img_in_text(self, url):
        if not element_exist(self.driver, self.IMG_IN_MAIN_XPATH):
            return False

        image = self.driver.find_element_by_xpath(self.IMG_IN_MAIN_XPATH)
        return image.get_attribute('src') == url