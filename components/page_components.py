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
    TOPIC_TEXT_XPATH = '//textarea[@id="id_text"]'
    CREATE_BUTTON_XPATH = '//button[contains(text(),"Создать")]'
    VOTE_CHECKBOX_XPATH = '//input[@name="add_poll"]'
    NO_COMMENTS_CHECKBOX_XPATH = '//input[@id="id_forbid_comment"]'
    PUBLISH_CHECKBOX_XPATH = '//input[@id="id_publish"]'
    QUESTION_TEXT_XPATH = '//input[@name="question"]'
    ANSWER_1_XPATH = '//input[@id="id_form-0-answer"]'
    ANSWER_2_XPATH = '//input[@id="id_form-1-answer"]'

    BOLD_BTN_XPATH = '(//a[@title="жирный [Ctrl+B]"])[2]'
    ITALIC_BTN_XPATH = '(//a[@title="курсив [Ctrl+I]"])[2]'
    QUOTE_BTN_XPATH = '(//a[@title="цитировать [Ctrl+Q]"])[2]'
    LIST_BTN_XPATH = '(//a[@title="Список"])[3]'
    ORDERED_LIST_BTN_XPATH = '(//a[@title="Список"])[4]'
    LINK_BTN_XPATH = '(//a[@title="Ссылка [Ctrl+L]"])[2]'
    UPLOAD_FILE_XPATH = '(//*[@name="filedata"])[2]'

    BOLD_ELEMENT_XPATH = '//*[@class="cm-hr"]'
    ITALIC_ELEMENT_XPATH = '//*[@class="cm-strong"]'
    QUOTE_ELEMENT_XPATH = '//*[@class="cm-atom"]'
    LIST_ELEMENT_XPATH = '//*[@class="cm-variable-2"]'
    LINK_ELEMENT_XPATH = '//*[@class="cm-link"]'
    IMG_ELEMENT_XPATH = '//*[@class="cm-tag"]'
    STRING_ELEMENT_XPATH = '//*[@class="cm-string"]'

    PUT_IMG_BTN_XPATH = '(//a[@title="изображение [Ctrl+P]"])[2]'
    FROM_INTERNET_BTN_XPATH = '//a[text()="Из интернета"]'
    IMG_URL_INPUT_XPATH = '//input[@name="img_url"]'
    IMG_UPLOAD_LINK_BTN_XPATH = '//button[@id="submit-image-upload-link"]'
    IMG_UPLOAD_BTN_XPATH = '//button[@id="submit-image-upload"]'

    ADD_USER_BTN_XPATH = '(//*[@title="Пользователь"])[2]'
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

    def set_text(self, short_text):
        self.driver.find_element_by_xpath(self.TOPIC_TEXT_XPATH).send_keys(short_text)

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

    def click_bold(self):
        self.driver.find_element_by_xpath(self.BOLD_BTN_XPATH).click()

    def bold_appear(self):
        return self.is_topic_text_equal('<strong></strong>')

    def click_italic(self):
        self.driver.find_element_by_xpath(self.ITALIC_BTN_XPATH).click()

    def italic_appear(self):
        return self.is_topic_text_equal('<em></em>')

    def click_quote(self):
        self.driver.find_element_by_xpath(self.QUOTE_BTN_XPATH).click()

    def quote_appear(self):
        return self.is_topic_text_equal('<blockquote></blockquote>')

    def click_list(self):
        self.driver.find_element_by_xpath(self.LIST_BTN_XPATH).click()

    def list_appear(self):
        return self.is_topic_text_equal('<ul>\n    <li></li>\n</ul>')

    def click_ordered_list(self):
        self.driver.find_element_by_xpath(self.ORDERED_LIST_BTN_XPATH).click()

    def ordered_list_appear(self):
        return self.is_topic_text_equal('<ol>\n    <li></li>\n</ol>')

    def click_link(self):
        self.driver.find_element_by_xpath(self.LINK_BTN_XPATH).click()

    def link_appear(self, link_name, url):
        if link_name == '':
            return self.is_topic_text_equal('<a href="' + url + '">Введите адрес ссылки...</a>')

        return self.is_topic_text_equal('<a href="' + url + '" title="' + link_name + '">Введите адрес ссылки...</a>')

    def user_appear(self, username, url):
        return self.is_topic_text_equal(u'<a href="{}">{}</a>'.format(url, username))

    def click_put_img(self):
        self.driver.find_element_by_xpath(self.PUT_IMG_BTN_XPATH).click()

    def img_link_appear(self, url):
        return self.is_topic_text_equal(u'<img src="{}" align="" title="" />'.format(url))

    def click_add_user(self):
        self.driver.find_element_by_xpath(self.ADD_USER_BTN_XPATH).click()

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

    def chose_img_from_pc(self, path):
        element = self.driver.find_element_by_xpath(self.UPLOAD_FILE_XPATH)
        ActionChains(self.driver).send_keys_to_element(element, path).perform()
        self.driver.find_element_by_xpath(self.IMG_UPLOAD_BTN_XPATH).click()

    def chose_img_from_internet(self, path):
        self.driver.find_element_by_xpath(self.FROM_INTERNET_BTN_XPATH).click()
        self.driver.find_element_by_xpath(self.IMG_URL_INPUT_XPATH).send_keys(path)
        self.driver.find_element_by_xpath(self.IMG_UPLOAD_LINK_BTN_XPATH).click()

    def is_topic_text_equal(self, text):
        topic_text = self.driver.find_element_by_xpath(self.TOPIC_TEXT_XPATH).get_attribute("value")
        return topic_text == text


class Topic(Component):
    TITLE_XPATH = '//*[@class="topic-title"]/a'
    TEXT_XPATH = '//*[@class="topic-content text"]'
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
        return self.driver.find_element_by_xpath(self.TEXT_XPATH).text

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
        return self.is_attr_in_content(u'<blockquote></blockquote>{}'.format(text))

    def has_list(self, text):
        return self.is_attr_in_content(u'<ul><br>    <li>{}</li></ul>'.format(text))

    def has_ordered_list(self, text):
        return self.is_attr_in_content(u'<ol><br>    <li>{}</li></ol>'.format(text))

    def link_in_text(self, link_name, url):
        return self.is_attr_in_content(u'<a href="{}">{}</a>'.format(url, link_name))

    def img_in_text(self, url):
        return self.is_attr_in_content(u'<img align="" src="{}" title="">'.format(url))