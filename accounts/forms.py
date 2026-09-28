from django import forms
from django.contrib.auth import get_user_model


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='İstifadəçi adı',
        max_length=100,
        min_length=3,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "İstifadəçi adı buraya",
        })
    )
    email = forms.EmailField(
        label='Elektron poçt',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Email buraya. Məsələn: someone@some.com",
        })
    )
    password = forms.CharField(
        label='Şifrə',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': "Şifrə",
        })
    )
    confirm_password = forms.CharField(
        label='Şifrənin təsdiqi',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': "Şifrənin təkrarı",
        })
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        User = get_user_model()
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Bu istifadəçi adı artıq mövcuddur.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        User = get_user_model()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Bu email artıq qeydiyyatdan keçib.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Şifrələr uyğun deyil.")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        label='İstifadəçi adı',
        max_length=100,
        min_length=3,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "İstifadəçi adı buraya",
        })
    )
    password = forms.CharField(
        label='Şifrə',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
