from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word') # label = 서치폼 왼쪽에 나오는 글 , search_word는 필드에 대한 아이디로 구분하는데 씀
