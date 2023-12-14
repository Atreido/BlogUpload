from django import forms
from .models import Post, Comments  # импортируем нужный класс из текущего моделс
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("published_date", "user")  # Исключаем ненужный столбец в таблоице

class AddComment(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ("publish_date", "posted",  "user")

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']