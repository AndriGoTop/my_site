from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'intro_text', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'intro_text': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-3'}),

        }
