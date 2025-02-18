from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from common.forms import UserForm
# Create your views here.

def logout_view(request):
    logout(request) # 로그아웃을 수행 후
    return redirect('index') # index 페이지로 리다이렉트

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user) # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def page_not_found(request, exception): # exception은 오류의 내용을 담음
    return render(request, 'common/404.html', {})
# DEBUG=TRUE인 개발 환경에서는 장고의 기본 404가 적용되므로 
# 사용자 404페이지는 운영환경에서만 보인다.