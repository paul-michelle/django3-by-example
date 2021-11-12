from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email_from = forms.EmailField()
    email_to = forms.EmailField()
    comments = forms.CharField(max_length=155, required=False, widget=forms.Textarea)
