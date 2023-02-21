from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import Textarea

class ContactForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 300px;', 'class': 'form-control'}),max_length=100)
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 300px;', 'class': 'form-control'}),max_length=100)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write Something...', 'style': 'width: 300px;', 'class': 'form-control'}),max_length=1000)