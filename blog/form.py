from django import forms
from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ('author',)
    



class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields = ['text']



