"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from.models import Comment
from.models import Blog

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


class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=50)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=50)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    gender = forms.ChoiceField(label="Ваш пол", 
                               choices=[('1', 'Мужской'), ('2', 'Женский')],
                               widget=forms.RadioSelect, initial=1)
    feedback = forms.ChoiceField(label='Выберите категорию',
                               choices=(('1', 'Пожелание по улучшению сайта'),
                               ('2', 'Отзыв о магазине'),
                               ('3', 'Отзыв о товаре')), initial=1)
    title = forms.CharField(label='Заголовок', max_length=50)
    message = forms.CharField(label='Сообщение',
                              widget=forms.Textarea(attrs={'rows':12, 'cols': 50}))
    notice = forms.BooleanField(label='Получать новости сайта на e-mail?',
                                required=False)


class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок",
                  'description': "Краткое содержание",
                  'content': "Полное содержание",
                  'image': "Картинка"
                  }