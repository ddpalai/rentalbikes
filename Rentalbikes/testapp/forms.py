from django import forms
from testapp.models import UserRegistration

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['name', 'mobile_number', 'age', 'driving_license_number','vehicle_name','aadhar_card','address']

