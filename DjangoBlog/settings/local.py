"""
Django settings for DjangoBlog project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库的类型
        'NAME': 'django_blog',  # 所使用的的数据库的名字
        'USER': 'root',  # 数据库服务器的用户
        'PASSWORD': DATABASE_PASSWORD,  # 密码
        'HOST': '127.0.0.1',  # 主机
        'PORT': '3306',  # 端口
    }
}

# SMTP服务器
EMAIL_HOST = 'smtp.163.com'
# 邮箱名
EMAIL_HOST_USER = 'jyj1519691288@163.com'
# 授权码
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
# 发送邮件的端口
EMAIL_PORT = 465
# 是否使用 TLS
EMAIL_USE_SSL = True
# 默认的发件人
DEFAULT_FROM_EMAIL = 'jyj的博客 <jyj1519691288@163.com>'