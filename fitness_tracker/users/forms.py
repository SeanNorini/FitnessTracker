from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"id":"username", "name":"username", "label":"username",
                                                             "maxlength":"100", 'autofocus': True}) )
    password = forms.CharField(widget=forms.TextInput(attrs={"id":"password", "name":"password", "label":"password",
                                                             "maxlength":"100"}) )
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"id":"remember_me"}))