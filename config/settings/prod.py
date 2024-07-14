from .base import *

ALLOWED_HOSTS = ['13.125.35.45'] # AWS lightsail public ip 
STATIC_ROOT = BASE_DIR / 'static/' 
# /home/ubuntu/projects/mysite/static를 nginx 정적파일 위치로 등록
STATICFILES_DIRS = [] # base.py와 충돌 방지를 피하고자 override