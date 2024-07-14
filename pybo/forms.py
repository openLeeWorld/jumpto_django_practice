from django import forms
from pybo.models import Question, Answer
# form은 페이지 요청시 전달되는 파리미터들을 쉽게 관리하기 위한 클래스
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content'] 
        # widget속성을 지정하면 form-control과 같은 부트스트랩 클래스 추가
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        # QuestionForm에서 사용할 Question 모델의 속성
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }