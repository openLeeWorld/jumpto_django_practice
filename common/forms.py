from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일") # 이메일 속성을 추가
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
        # 비밀번호1과 2가 일치하는지 대조, 생성 규칙에 맞는지 확인