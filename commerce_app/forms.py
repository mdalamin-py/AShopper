from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from .models import NewsletterModel, Subscribe, AddressBook, OrderPlacedFormModel, FAQ
from django.contrib.auth import password_validation


class RegisterForm(UserCreationForm):
    username = UsernameField(label=('Username'), widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Your Username'}))
    first_name = forms.CharField(label=('First Name'), widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Your First Name'}))
    last_name = forms.CharField(label=('Last Name'), widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Your Last Name'}))
    email = forms.EmailField(label=('Email'), widget=forms.EmailInput(
        attrs={'class': 'form-input', 'placeholder': 'Your Email'}), required=True)
    password1 = forms.CharField(label=('Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Your Password'}), strip=False)
    password2 = forms.CharField(label=('Confirm Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Your Confirm Password'}), strip=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = UsernameField(label=_('Username'), widget=forms.TextInput(
        attrs={'class': 'input100', 'autofoucs': True}))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs={'class': 'input100'}), strip=False)


class ChangesPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'autocomplate': 'current-password'}), strip=False)
    new_password1 = forms.CharField(label=_('New Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'autocomplete': 'new password'}), strip=False, help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'autocomplete': 'confirm password'}), strip=False)


class ResetPassword(PasswordResetForm):
    email = forms.EmailField(label=('Email'), widget=forms.EmailInput(
        attrs={'class': 'form-input', 'placeholder': 'Your Email'}), required=True)


class PasswordResetConfirm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'autocomplete': 'new password'}), strip=False)
    new_password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'autocomplete': 'confirm password'}), strip=False)


# class SubscriberForm(forms.ModelForm):
#         class Meta:
#                 model = Subscribe
#                 fields = ['email']
#                 widgets = {'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'hello'})}

class SubscribeForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ['email']
                

class NewsletterForm(forms.ModelForm):
        class Meta:
                model = NewsletterModel
                fields = ['username', 'email']



class ContactForms(forms.ModelForm):
        class Meta:
                model = AddressBook
                fields = ['name', 'province', 'city', 'email', 'phone', 'area', 'address']
                widgets = {'name': forms.TextInput(attrs={'class': 'form-controls', 'type': 'text', 'placeholder': 'Please enter your name', 'border-radius': '10px'}), 'province': forms.Select(attrs={'class': 'form-controls'}), 'city': forms.Select(attrs={'class': 'form-controls'}), 'email': forms.EmailInput(attrs={'class': 'form-controls', 'type': 'email', 'placeholder': 'Please enter your email'}), 'phone': forms.TextInput(attrs={'class': 'form-controls', 'type': 'text', 'placeholder': 'Please enter your phone number'}) ,'area': forms.TextInput(attrs={'class': 'form-controls', 'placeholder': 'Please enter your area'}), 'address': forms.TextInput(attrs={'class': 'form-controls', 'placeholder': 'Please enter your address'})}
                


class OrderPlacedForm(forms.ModelForm):
        class Meta:
            model = OrderPlacedFormModel
            fields = [ 'cardholder_name','month', 'year', 'card_number', 'cvv_code', 'billing_address']
            widgets = {
                'cardholder_name' : forms.TextInput(attrs={'class': 'form-controls', 'type': 'text'}),
                'month': forms.Select(attrs={'class': 'form-controls','type': 'date'}),
                'year': forms.Select(attrs={'class': 'form-controls','type': 'date'}),
                'card_number' : forms.TextInput(attrs={'class': 'form-controls', 'type': 'text'}),
                'cvv_code' : forms.PasswordInput(attrs={'class': 'form-controls', 'type': 'text'}),
                'billing_address' : forms.TextInput(attrs={'class': 'form-controls', 'type': 'text'}),
            }
        

           
class FAQForms(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question_title', 'question_description']
        widgets = {'question_title': forms.TextInput(attrs={'class': 'form-controls', 'type': 'text'}),
                   'question_description': forms.Textarea(attrs={'class': 'form-controls', 'type': 'textarea'})}