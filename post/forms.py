from django import forms
from .models import Comment, Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-input',
                'placeholder' : 'Введите заголовок...'
            }),
            'content' : forms.Textarea(attrs={
                'class' : 'form-input',
                'placeholder' : 'содержание поста...'
            }),
        }
        labels = {
            'title' : 'Заголовок',
            'content' : 'Содержание'
        }
        
class ComentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['text']
        widgets = {
            'text' : forms.Textarea(attrs={
                'class' : 'form-input',
                'placeholder' : 'Текст комментария...'
            }),
        }
        labels = {
            'text' : 'Текст',
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите заголовок...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Введите текст поста...'
            }),
        }

