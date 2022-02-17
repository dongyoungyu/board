from django import forms
from pybo.models import Question, Answer, Comment, FileUpload

# from django.forms import ModelForm
# from .models import FileUpload


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['title', 'imgfile', 'content']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content', 'imgfile']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
            'imgfile': '첨부파일',
        } 

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

        