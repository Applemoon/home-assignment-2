# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time


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
    SHORT_TEXT_XPATH = '//*[@id="content"]/div/div[1]/form/div/div[3]/div[6]'
    MAIN_TEXT_XPATH = '//*[@id="content"]/div/div[1]/form/div/div[6]/div[6]'
    CREATE_BUTTON_XPATH = '//button[contains(text(),"Создать")]'
    VOTE_CHECKBOX_XPATH = '//input[@name="add_poll"]'
    NO_COMMENTS_CHECKBOX_XPATH = '//input[@id="id_forbid_comment"]'
    PUBLISH_CHECKBOX_XPATH = '//input[@id="id_publish"]'
    QUESTION_TEXT_XPATH = '//input[@name="question"]'
    ANSWER_1_XPATH = '//input[@id="id_form-0-answer"]'
    ANSWER_2_XPATH = '//input[@id="id_form-1-answer"]'

    def send_text(self, text):
        ActionChains(self.driver).send_keys(text).perform()

    def blog_select_open(self):
        self.driver.find_element_by_xpath(self.BLOG_SELECT_XPATH).click()  # TODO! падает

    def blog_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(self.OPTION_XPATH.format(option_text)).click()

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.TITLE_XPATH).send_keys(title)

    def set_short_text_without_click(self, short_text):
        self.send_text(short_text)

    def set_short_text(self, short_text):
        self.driver.find_element_by_xpath(self.SHORT_TEXT_XPATH).click()
        self.set_short_text_without_click(short_text)

    def set_main_text_without_click(self, main_text):
        self.send_text(main_text)

    def set_main_text(self, main_text):
        self.driver.find_element_by_xpath(self.MAIN_TEXT_XPATH).click()
        self.set_main_text_without_click(main_text)

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


class Topic(Component):
    TITLE_XPATH = '//*[@class="topic-title"]/a'
    TEXT_XPATH = '//*[@class="topic-content text"]/p'
    BLOG_XPATH = '//*[@class="topic-blog"]'
    DELETE_BUTTON_XPATH = '//a[@class="actions-delete"]'
    DELETE_BUTTON_CONFIRM_XPATH = '//input[@value="Удалить"]'
    ADD_COMMENTS_XPATH = '//a[text()="Оставить комментарий"]'
    ANSWERS_XPATH = '//input[@class="answer"]'
    ANSWER_1_XPATH = '//*[@id="content"]/div/div[1]/article/div/div[1]/form/ul/li[1]/label'
    ANSWER_2_XPATH = '//*[@id="content"]/div/div[1]/article/div/div[1]/form/ul/li[2]/label'

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
        #     answers += element.text()
        #
        # return answers

        # return self.driver.find_element_by_xpath(self.ANSWER_1_XPATH).text(), \
        #        self.driver.find_element_by_xpath(self.ANSWER_2_XPATH).text()

        return u'Ответ1', u'Ответ2' # TODO

    def open_blog(self):
        self.driver.find_element_by_xpath(self.BLOG_XPATH).click()

    def delete(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON_XPATH).click()
        self.driver.find_element_by_xpath(self.DELETE_BUTTON_CONFIRM_XPATH).click()

    def has_comments(self):
        try:
            self.driver.find_element_by_xpath(self.ADD_COMMENTS_XPATH)
        except NoSuchElementException:
            return False

        return True