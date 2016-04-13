from django import forms
from pagedown.widgets import PagedownWidget
from pagedown.widgets import AdminPagedownWidget
from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image"
        ]

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post
        fields = '__all__'
