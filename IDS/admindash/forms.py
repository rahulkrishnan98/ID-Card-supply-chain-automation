from django.forms import ModelForm
from .models import ClientDetail, OrderDetail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ClientDetailForm(ModelForm):
    class Meta:
        model = ClientDetail
        fields = ['company', 'email', 'fname', 'lname','phonenum', 'address', 'city', 'country', 'pincode']
    def __init__(self, *args, **kwargs):
        super(ClientDetailForm, self).__init__(*args, **kwargs)
        self.fields['company'].widget.attrs['class'] = 'form-control border-input'
        self.fields['email'].widget.attrs['class'] = 'form-control border-input'
        self.fields['fname'].widget.attrs['class'] = 'form-control border-input'
        self.fields['lname'].widget.attrs['class'] = 'form-control border-input'
        self.fields['phonenum'].widget.attrs['class'] = 'form-control border-input'
        self.fields['address'].widget.attrs['class'] = 'form-control border-input'
        self.fields['city'].widget.attrs['class'] = 'form-control border-input'
        self.fields['country'].widget.attrs['class'] = 'form-control border-input'
        self.fields['pincode'].widget.attrs['class'] = 'form-control border-input'


class RegisterUser(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterOrder, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control border-input'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter the order'
        self.fields['password1'].widget.attrs['class'] = 'form-control border-input'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control border-input'
