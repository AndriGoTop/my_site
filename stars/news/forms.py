from django import forms


class NewsForm(forms.Form):
    title = forms.CharField(max_length=250)
    content = forms.CharField()
    is_published = forms.BooleanField()
