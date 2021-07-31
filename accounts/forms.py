from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create/Signup Profile For User
# The model that is customized 
class SignUpForm(UserCreationForm):
    # Customization 3 fields In Form Signup.
    first_name    = forms.CharField(max_length=50   , required=False , widget=forms.TextInput()  , help_text='Optional') # 01
    last_name     = forms.CharField(max_length=50   , required=False , widget=forms.TextInput()  , help_text='Optional') # 03
    email         = forms.EmailField(max_length=150 , required=True  , widget=forms.EmailInput() , help_text='Required Field') # 03
    
    class Meta:
        model=User # Data Table
        fields = {'username','email','password1','password2'} # Table Fields
        labels = {'username': ('User Name')} # change the Field Title
        labels = {'Password1': ('Password')} # change the Field Title
        labels = {'password2': ('Confirm Passwoerd')} # change the Field Title
        help_texts = {'email': ('Please Enter a Valid Email.')} 
#
#
# 
# Profile Update
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User # Data Table
        fields = [ # Fields Table
            'username',
            'first_name', 
            'last_name', 
            'email',
            ]
#
#
#
# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(max_length=150)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
