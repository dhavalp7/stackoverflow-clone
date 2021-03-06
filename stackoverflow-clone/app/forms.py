"""
Definition of forms.
"""

from django import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
        
class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = [
            'que_title',
            'que_desc',
            'que_tag',
        ]

class AnswerModelForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = [
            'ans_desc',
        ]

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = models.CommentOnAnswer
        fields = [
            'cmt_desc',
        ]
        
        



        
