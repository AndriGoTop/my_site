from django import forms
from .models import News, Pictures


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'intro_text', 'content', 'intro_picture']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'intro_text': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'intro_pictures': forms.ImageField(),
        }
