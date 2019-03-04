from django import forms
from .models import Post, Comment, Document
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import re


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('author', 'text',)


class RegistrationForm(forms.Form):
    username = forms.CharField(label='User', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Input password again', widget=forms.PasswordInput)

    def clean_password(self):
        if password1 == password2 and password1:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError('Password is incorrect')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username has special characters')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username has existed')
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'],
                                 password=self.cleaned_data['password1'])


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document',)

