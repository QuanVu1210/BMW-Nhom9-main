from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from user.models import UserProfile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Nhập tên đăng nhập của bạn', label= 'Tên đăng nhập')
    email = forms.EmailField(max_length=200, help_text='Nhập email của bạn', label= 'Email')
    first_name = forms.CharField(max_length=100, help_text='Nhập họ của bạn',label= 'Họ')
    last_name = forms.CharField(max_length=100, help_text='Nhập tên của bạn',label= 'Họ tên')

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )



class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ( 'username','email','first_name','last_name')
        widgets = {
            'username'  : TextInput(attrs={'class': 'input','placeholder':'username'}),
            'email'     : EmailInput(attrs={'class': 'input','placeholder':'email'}),
            'first_name': TextInput(attrs={'class': 'input','placeholder':'first_name'}),
            'last_name' : TextInput(attrs={'class': 'input','placeholder':'last_name' }),
        }

CITY = [
    ('Hà Nội', 'Hà Nội'),
    ('HCM', 'HCM'),
    ('Đà Nẵng', 'Đà Nẵng'),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city','country','image')
        widgets = {
            'phone'     : TextInput(attrs={'class': 'input','placeholder':'phone'}),
            'address'   : TextInput(attrs={'class': 'input','placeholder':'address'}),
            'city'      : Select(attrs={'class': 'input','placeholder':'city'},choices=CITY),
            'country'   : TextInput(attrs={'class': 'input','placeholder':'country' }),
            'image'     : FileInput(attrs={'class': 'input', 'placeholder': 'image', }),
        }
