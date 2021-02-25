from django import forms
from markdownx.fields import MarkdownxFormField
from django.contrib.auth.models import User

class MyForm(forms.Form):
    Content = MarkdownxFormField(max_length=255)

class AddArticle(forms.Form):

    Title = forms.CharField(
        label="標題",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    Content = MarkdownxFormField(
        label="內文",
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('Title', 'Content')