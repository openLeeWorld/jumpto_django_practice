# import environ # django-environ

from .base import *

ALLOWED_HOSTS = ['13.125.35.45'] # AWS lightsail public ip 
# 'pybo.kr'등 도메인을 구매해서 dns네임서버에 레코드 등록 후 위에다 넣어도 됨
STATIC_ROOT = BASE_DIR / 'static/' 
# /home/ubuntu/projects/mysite/static를 nginx 정적파일 위치로 등록
STATICFILES_DIRS = [] # base.py와 충돌 방지를 피하고자 override
DEBUG = False

# env = environ.ENV()
# environ.Env.read_env(BASE_DIR / '.env')
'''
DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2'
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '5432',
    }
}
''' 