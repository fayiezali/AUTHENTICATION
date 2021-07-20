from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create/Signup Profile For User
# The model that is customized 
class SignUpForm(UserCreationForm):
    # Customization 3 fields In Form Signup.
    first_name    = forms.CharField(max_length=50  , required=False , widget=forms.TextInput()  , help_text='Optional') # 01
    last_name     = forms.CharField(max_length=50  , required=False , widget=forms.TextInput()  , help_text='Optional') # 03
    email         = forms.CharField(max_length=250 , required=True  , widget=forms.EmailInput() , help_text='Required Field') # 03
    
    class Meta:
        model=User # Data Table
        fields = {'username','email','password1','password2'} # Table Fields
        labels = {'username': ('User Name')} # change the Field Title
        labels = {'Password1': ('Password')} # change the Field Title
        labels = {'password2': ('Confirm Passwoerd')} # change the Field Title
#
#
#
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

        # help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).')} 
        

# class PasswordChangeForm(SetPasswordForm):
#     """
#     A form that lets a user change their password by entering their old
#     password.
#     """
#     error_messages = {
#         **SetPasswordForm.error_messages,
#         'password_incorrect': _("Your old password was entered incorrectly. Please enter it again."),
#     }
#     old_password = forms.CharField(
#         label=_("Old password"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
#     )

#     field_order = ['old_password', 'new_password1', 'new_password2']

#     def clean_old_password(self):
#         """
#         Validate that the old_password field is correct.
#         """
#         old_password = self.cleaned_data["old_password"]
#         if not self.user.check_password(old_password):
#             raise ValidationError(
#                 self.error_messages['password_incorrect'],
#                 code='password_incorrect',
#             )
#         return old_password