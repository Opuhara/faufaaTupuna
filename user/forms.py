# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AppUser


class AppUserCreationForm(UserCreationForm):
	class Meta:
		model = AppUser
		fields = ('username', 'email', 'bio', 'birth_date')


class AppUserChangeForm(UserChangeForm):
	class Meta:
		model = AppUser
		fields = ('username', 'email', 'bio', 'birth_date')


class AppUserSignUpForm(UserCreationForm):
	email = forms.EmailField(required=True,
							 widget=forms.EmailInput(attrs={'class': 'uk-input', 'placeholder': 'Email'}))

	class Meta:
		model = AppUser
		fields = ('username', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(AppUserSignUpForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class AppUserProfileForm(forms.ModelForm):
	class Meta:
		model = AppUser
		fields = ['first_name', 'last_name', 'email']  # Ajoute les champs de ton modèle

	def __init__(self, *args, **kwargs):
		super(AppUserProfileForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'uk-input'
			})
		self.fields['email'].widget.attrs.update({
			'class': 'uk-input uk-form-danger',
			'placeholder': 'Email'
		})
