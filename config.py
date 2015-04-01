# -*- coding: utf-8 -*-
import os

browser_environ = 'TTHA2BROWSER'
browser = os.environ.get(browser_environ, 'CHROME')

login = 'ftest10@tech-mail.ru'
password = os.environ['TTHA2PASSWORD']

username = u'Дядя Миняй'
user_url = '/profile/d.minyaj/'

blog = 'Флудилка'
title = u'Мой уникальный заголовок'
short_text = u'Короткий уникальный текст, отображается в блогах!'
main_text = u'Уникальный текст под катом! Отображается внутри топика!'

link = 'http://ya.ru/'
image_url = 'http://static014.cmtt.ru/paper-media/mail-ru/5885d14c4be65ac30803.png'
local_image_path = os.getcwdu() + '/smiley.png'