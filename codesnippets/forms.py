from django import forms

class CodeForm(forms.Form): #creating a form with validation

    snippet = forms.CharField(label='Code Snippet', widget=forms.Textarea(attrs={'class': 'form-control'}))
    