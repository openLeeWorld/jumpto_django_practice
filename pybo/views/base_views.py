# 기본 관리 
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q # 검색 함수
from ..models import Question

import logging
logger = logging.getLogger('pybo') 
# pybo는 로거명 설정(base.py에 설정)

def index(request):
    logger.info("INFO 레벨로 출력")
    
    page = request.GET.get('page', 1) 
    kw = request.GET.get('kw', '') # 검색어
    question_list = Question.objects.order_by('-create_date')
    # create_date의 역순으로 정렬한다.
    if kw: # 검색어가 있다면(searchForm form의 GET요청 받음)
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # 제목 검색
            Q(content__icontains=kw) | # 내용 검색
            Q(answer__content__icontains=kw) | # 답변 내용 검색
            Q(author__username__icontains=kw) | # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct() # contains 대신 icontains를 쓰면 대소문자 상관없이 찾음
    paginator = Paginator(question_list, 10) # 페이지당 10개씩
    page_obj = paginator.get_page(page)
    # 장고 내부적으로 해당 페이지의 데이터만 조회하도록 쿼리
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context) 
    # 파이썬 데이터를 템플릿에 적용하여 html로 반환하는 함수
    # return HttpResponse("안녕하세요. pybo에 잘 오셨습니다.")
    
def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

