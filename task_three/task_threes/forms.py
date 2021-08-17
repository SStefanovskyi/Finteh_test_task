from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {'title': forms.Textarea(attrs={'cols': 1}),
                   'content': forms.Textarea(attrs={'cols': 80}),
                   'image': forms.ImageField}