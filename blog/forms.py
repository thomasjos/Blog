from django import forms
from .models import Post, Author, Comment

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
