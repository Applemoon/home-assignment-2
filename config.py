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
topic_text = u'Это мой самый уникальный и оригинальный текст.'

link = 'http://ya.ru/'
image_url = 'static014.cmtt.ru/paper-media/mail-ru/5885d14c4be65ac30803.png'
local_image_path = os.getcwdu() + '/smiley.png'