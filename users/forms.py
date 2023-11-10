from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"id":"username", "name":"username", "label":"username",
                                                             "maxlength":"100", 'autofocus': True}) )
    password = forms.CharField(widget=forms.PasswordInput(attrs={"id":"password", "name":"password", "label":"password",
                                                             "maxlength":"100"}) )
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"id":"remember_me"}))

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"id":"username", "name":"username", "maxlength":"100", 
                                                             }) )
    first_name = forms.CharField(label="First Name", required=False, widget=forms.TextInput(attrs={"id":"first_name", "name":"first_name", "maxlength":"100",
                                                              'placeholder': 'Jane'}) )
    last_name = forms.CharField(label="Last Name", required=False, widget=forms.TextInput(attrs={"id":"last_name", "name":"last_name", "maxlength":"100", 
                                                               'placeholder': 'Doe'}) )
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"id":"password", "name":"password", "maxlength":"100"}) )
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"id":"confirm_password", "name":"confirm_password", 
                                                                  "maxlength":"100"}) )
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"placeholder":"example@gmail.com"}))

    height = forms.DecimalField(label="Height", max_digits=2, required=False, widget=forms.TextInput(attrs={'placeholder': '70', "class":"numbers"}))

    weight = forms.DecimalField(label="Weight", max_digits=5, required=False, widget=forms.TextInput(attrs={'placeholder': '180', "class":"numbers"}))

    age = forms.IntegerField(label="Age", required=False, 
                             widget=forms.TextInput(attrs={'placeholder': '30', "class":"numbers"}))
    
    