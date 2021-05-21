"""
Django settings for DjangoBlog project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#!kkqdbp3&lgnsjltv*6c7u*b*!uyum+j=bp5)v4hssjzr=u_7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'password_reset',
    'article',
    'userprofile',
    'comment',
    'home',
    'taggit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [f"BASE_DIR / 'templates'"]
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoBlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库的类型
        'NAME': 'django_blog',  # 所使用的的数据库的名字
        'USER': 'root',  # 数据库服务器的用户
        'PASSWORD': 'Jyj2018jyjy',  # 密码
        'HOST': '127.0.0.1',  # 主机
        'PORT': '3306',  # 端口
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
# 静态文件收集目录
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

# SMTP服务器
EMAIL_HOST = 'smtp.163.com'
# 邮箱名
EMAIL_HOST_USER = 'jyj1519691288@163.com'
# 授权码
EMAIL_HOST_PASSWORD = 'DOUQDJBJSSLPIEGA'
# 发送邮件的端口
EMAIL_PORT = 465
# 是否使用 TLS
EMAIL_USE_SSL = True
# 默认的发件人
DEFAULT_FROM_EMAIL = 'jyj的博客 <jyj1519691288@163.com>'

# 媒体文件地址
MEDIA_URL = '/media/'  # 用户上传文件访问位置
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  # 用户上传文件保存位置

# CKEDITOR_CONFIGS = {
#     # django-ckeditor默认使用default配置
#     'default': {
#         # 编辑器宽度自适应
#         'width':'auto',
#         'height':'250px',
#         # tab键转换空格数
#         'tabSpaces': 4,
#         # 工具栏风格
#         'toolbar': 'Custom',
#         # 工具栏按钮
#         'toolbar_Custom': [
#             # 表情 代码块
#             ['Smiley', 'CodeSnippet'],
#             # 字体风格
#             ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
#             # 字体颜色
#             ['TextColor', 'BGColor'],
#             # 链接
#             ['Link', 'Unlink'],
#             # 列表
#             ['NumberedList', 'BulletedList'],
#             # 最大化
#             ['Maximize']
#         ],
#         # 加入代码块插件
#         'extraPlugins': ','.join(['codesnippet', 'prism', 'widget', 'lineutils']),
#     }
# }
