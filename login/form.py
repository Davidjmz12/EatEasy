from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from location_field.forms.plain import PlainLocationField

from login.models import User, Restaurant


class RestaurantRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="A valid email address, please.", required=False)
    avatar = forms.ImageField(allow_empty_file=True, help_text='Avatar image', required=False)

    web_page = forms.URLField(required=False)
    precise_location = forms.CharField()
    city = forms.CharField()
    phone_number = forms.IntegerField(help_text="+00 000 00 00 00 format")
    description = forms.CharField(max_length=200)
    rest_name = forms.CharField(max_length=50)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RestaurantRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = User.Role.RESTAURANT
        user.avatar = self.cleaned_data['avatar']
        cleaned = [self.cleaned_data[item] for item in ["web_page", "precise_location", "city",
                                                        "phone_number", "description", "rest_name"]]
        restaurant = Restaurant(user=user, web_page=cleaned[0], precise_location=cleaned[1], city=cleaned[2],
                                phone_number=cleaned[3], description=cleaned[4], rest_name=cleaned[5])
        if commit:
            user.save()
            restaurant.save()

        return user


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text="A valid email address, please.", required=False,
                             widget=forms.TextInput(attrs={'class': 'input-text'}))
    avatar = forms.ImageField(allow_empty_file=True, help_text='Avatar image', required=False)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = User.Role.CLIENT
        user.avatar = self.cleaned_data['avatar']
        if commit:
            user.save()

        return user
