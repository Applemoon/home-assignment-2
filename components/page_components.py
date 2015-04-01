# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import title_contains, text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait


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
        WebDriverWait(self.driver, 30, 0.1).until_not(title_contains(u'Главная'))


class CreateForm(Component):
    BLOG_SELECT_XPATH = '//a[@class="chzn-single"]'
    OPTION_XPATH = '//li[text()="{}"]'
    TITLE_XPATH = '//input[@name="title"]'
    SHORT_TEXT_XPATH = '(//div[@class="CodeMirror-scroll"])[1]'
    MAIN_TEXT_XPATH = '(//div[@class="CodeMirror-scroll"])[2]'
    CREATE_BUTTON_XPATH = '//button[contains(text(),"Создать")]'
    VOTE_CHECKBOX_XPATH = '//input[@name="add_poll"]'
    NO_COMMENTS_CHECKBOX_XPATH = '//input[@id="id_forbid_comment"]'
    PUBLISH_CHECKBOX_XPATH = '//input[@id="id_publish"]'
    QUESTION_TEXT_XPATH = '//input[@name="question"]'
    ANSWER_1_XPATH = '//input[@id="id_form-0-answer"]'
    ANSWER_2_XPATH = '//input[@id="id_form-1-answer"]'

    BOLD_BTN_MAIN_XPATH = '(//*[@title="Жирный"])[2]'
    ITALIC_BTN_MAIN_XPATH = '(//*[@title="Курсив"])[2]'
    QUOTE_BTN_MAIN_XPATH = '(//*[@title="Цитировать"])[2]'
    LIST_BTN_MAIN_XPATH = '(//*[@title="Список"])[2]'
    ORDERED_LIST_BTN_MAIN_XPATH = '(//*[@title="Список с нумерацией"])[2]'
    LINK_BTN_MAIN_XPATH = '(//*[@title="Вставить ссылку"])[2]'
    PUT_IMG_BTN_MAIN_XPATH = '(//*[@title="Вставить изображение"])[2]'
    UPLOAD_IMG_BTN_MAIN_XPATH = '(//*[@title="Загрузить изображение"])[2]'
    UPLOAD_FILE_MAIN_XPATH = '(//*[@name="filedata"])[2]'

    BOLD_ELEMENT_XPATH = '//*[@class="cm-hr"]'
    ITALIC_ELEMENT_XPATH = '//*[@class="cm-strong"]'
    QUOTE_ELEMENT_XPATH = '//*[@class="cm-atom"]'
    LIST_ELEMENT_XPATH = '//*[@class="cm-variable-2"]'
    LINK_ELEMENT_XPATH = '//*[@class="cm-link"]'
    IMG_ELEMENT_XPATH = '//*[@class="cm-tag"]'
    STRING_ELEMENT_XPATH = '//*[@class="cm-string"]'

    ADD_USER_BTN_MAIN_XPATH = '(//*[@title="Добавить пользователя"])[2]'
    ADD_USER_INPUT_XPATH = '//*[@id="search-user-login-popup"]'
    ADD_USER_USERNAME_XPATH = '//a[@class="user_profile_path"][text()="Дядя Миняй"]'

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
        self.driver.find_element_by_xpath(self.QUESTION_TEXT_XPATH).send_keys(question)
        self.driver.find_element_by_xpath(self.ANSWER_1_XPATH).send_keys(answer_1)
        self.driver.find_element_by_xpath(self.ANSWER_2_XPATH).send_keys(answer_2)

    def click_bold_for_main(self):
        self.driver.find_element_by_xpath(self.BOLD_BTN_MAIN_XPATH).click()

    def bold_appear(self):
        return element_exist(self.driver, self.BOLD_ELEMENT_XPATH)

    def click_italic_for_main(self):
        self.driver.find_element_by_xpath(self.ITALIC_BTN_MAIN_XPATH).click()

    def italic_appear(self):
        return element_exist(self.driver, self.ITALIC_ELEMENT_XPATH)

    def click_quote_for_main(self):
        self.driver.find_element_by_xpath(self.QUOTE_BTN_MAIN_XPATH).click()

    def quote_appear(self):
        return element_exist(self.driver, self.QUOTE_ELEMENT_XPATH)

    def click_list_for_main(self):
        self.driver.find_element_by_xpath(self.LIST_BTN_MAIN_XPATH).click()

    def list_appear(self):
        return element_exist(self.driver, self.LIST_ELEMENT_XPATH)

    def click_ordered_list_for_main(self):
        self.driver.find_element_by_xpath(self.ORDERED_LIST_BTN_MAIN_XPATH).click()

    def ordered_list_appear(self):
        return element_exist(self.driver, self.LIST_ELEMENT_XPATH)

    def click_link_for_main(self):
        self.driver.find_element_by_xpath(self.LINK_BTN_MAIN_XPATH).click()

    def link_appear(self, link_name, url):
        link_element_exists = element_exist(self.driver, self.LINK_ELEMENT_XPATH)
        string_element_exists = element_exist(self.driver, self.STRING_ELEMENT_XPATH)
        if not link_element_exists or not string_element_exists:
            return False

        link_element_ok = self.driver.find_element_by_xpath(self.LINK_ELEMENT_XPATH).text == u'[{}]'.format(link_name)
        string_element_ok = self.driver.find_element_by_xpath(self.STRING_ELEMENT_XPATH).text == u'({})'.format(
            url)

        return link_element_ok and string_element_ok

    def click_put_img_for_main(self):
        self.driver.find_element_by_xpath(self.PUT_IMG_BTN_MAIN_XPATH).click()

    def img_link_appear(self, url=None):
        img_element_exists = element_exist(self.driver, self.IMG_ELEMENT_XPATH)
        string_element_exists = element_exist(self.driver, self.STRING_ELEMENT_XPATH)
        if not img_element_exists or not string_element_exists:
            return False

        img_element_ok = self.driver.find_element_by_xpath(self.IMG_ELEMENT_XPATH).text == u'![]'
        string_element_ok = self.driver.find_element_by_xpath(self.STRING_ELEMENT_XPATH).text == u'({})'.format(
            url)

        return img_element_ok and string_element_ok

    def click_upload_img_for_main(self):
        self.driver.find_element_by_xpath(self.UPLOAD_IMG_BTN_MAIN_XPATH).click()

    def click_add_user_for_main(self):
        self.driver.find_element_by_xpath(self.ADD_USER_BTN_MAIN_XPATH).click()

    def search_user(self, name):
        element = self.driver.find_element_by_xpath(self.ADD_USER_INPUT_XPATH)
        element.click()
        element.send_keys(name)
        element.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 30, 0.1).until(
            text_to_be_present_in_element((By.XPATH, self.ADD_USER_USERNAME_XPATH), name)
        )

    def choose_user(self):
        self.driver.find_element_by_xpath(self.ADD_USER_USERNAME_XPATH).click()

    def add_user_appear(self, name, url):
        return self.link_appear(name, url)

    def upload_img(self, path):
        self.driver.execute_script('$(".markdown-upload-photo-container").show()')
        element = self.driver.find_element_by_xpath(self.UPLOAD_FILE_MAIN_XPATH)
        ActionChains(self.driver).send_keys_to_element(element, path).perform()
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.STRING_ELEMENT_XPATH).text[1:-1]
        )


class Topic(Component):
    TITLE_XPATH = '//*[@class="topic-title"]/a'
    TEXT_XPATH = '//*[@class="topic-content text"]/p'
    BLOG_XPATH = '//*[@class="topic-blog"]'
    DELETE_BUTTON_XPATH = '//a[@class="actions-delete"]'
    DELETE_BUTTON_CONFIRM_XPATH = '//input[@value="Удалить"]'
    ADD_COMMENTS_XPATH = '//a[text()="Оставить комментарий"]'

    ANSWER_1_XPATH = '(//input[@class="answer"])[1]'
    ANSWER_2_XPATH = '(//input[@class="answer"])[2]'

    TOPIC_CONTENT_TEXT_XPATH = '//div[@class="topic-content text"]'
    ANSWERS_CONTENT_XPATH = '//ul[@class="poll-vote"]'

    def get_title(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE_XPATH).text
        )

    def get_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT_XPATH).text
        )

    def get_answers(self):
        answer_1 = self.driver.find_element_by_xpath(self.ANSWER_1_XPATH).text
        answer_2 = self.driver.find_element_by_xpath(self.ANSWER_2_XPATH).text
        return answer_1, answer_2

    def open_blog(self):
        self.driver.find_element_by_xpath(self.BLOG_XPATH).click()

    def delete(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON_XPATH).click()
        self.driver.find_element_by_xpath(self.DELETE_BUTTON_CONFIRM_XPATH).click()

    def has_comments(self):
        return element_exist(self.driver, self.ADD_COMMENTS_XPATH)

    def is_attr_in_content(self, attr):
        content = self.driver.find_element_by_xpath(self.TOPIC_CONTENT_TEXT_XPATH).get_attribute('innerHTML')
        return attr in content

    def has_answers(self, answer_1, answer_2):
        content = self.driver.find_element_by_xpath(self.ANSWERS_CONTENT_XPATH).get_attribute('innerHTML')
        return answer_1 in content and answer_2 in content

    def is_strong(self, text):
        return self.is_attr_in_content(u'<strong>{}</strong>'.format(text))

    def is_italic(self, text):
        return self.is_attr_in_content(u'<em>{}</em>'.format(text))

    def has_quote(self, text):
        return self.is_attr_in_content(u'&gt; {}'.format(text))

    def has_list(self, text):
        return self.is_attr_in_content(u'<ul>\n<li>{}</li>\n</ul>'.format(text))

    def has_ordered_list(self, text):
        return self.is_attr_in_content(u'<ol>\n<li>{}</li>\n</ol>'.format(text))

    def link_in_text(self, link_name, url):
        return self.is_attr_in_content(u'<a href="{}">{}</a>'.format(url, link_name))

    def img_in_text(self, url):
        return self.is_attr_in_content(u'<img alt="" src="{}">'.format(url))