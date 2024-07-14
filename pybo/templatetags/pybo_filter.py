from django import template
# 장고의 템플릿 필터 함수를 만들기
import markdown
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter # 템플릿에서 해당 함수를 필터로 사용할 수 있게 함
def sub(value, arg):
    return value - arg

@register.filter
def mark(value): # 입력 문자열을 HTML로 변환하는 필더 함수
    extensions = ["nl2br", "fenced_code"] 
    # 줄바꿈 문자를 <br>로 바꿈, 마크다운의 소스 코드 표현을 위해 필요
    return mark_safe(markdown.markdown(value, extensions=extensions))