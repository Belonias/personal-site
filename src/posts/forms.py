from django import forms
from pagedown.widgets import PagedownWidget

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image"
        ]
