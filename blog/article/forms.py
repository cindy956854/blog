from django import forms
from article.models import Article

class NameForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=30)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='標題', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ['title', 'content']