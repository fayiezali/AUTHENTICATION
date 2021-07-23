# 
from django.conf import settings
#
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login, 
    logout as auth_logout, update_session_auth_hash,
)
#
from django.contrib.auth.models import User # إستيراد اسم المستخدم
#
# Only a Logged In User can call this view
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin

from django.contrib.auth.decorators import login_required
#
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm , PasswordResetForm, SetPasswordForm,
)
#
from django.contrib.auth.views import LoginView , LogoutView , TemplateView , PasswordChangeView , PasswordResetView , PasswordResetDoneView , PasswordResetConfirmView , PasswordResetCompleteView
#
from django.utils import timezone
#
from django.views import generic
#
from django.views.generic import TemplateView , ListView ,DetailView , CreateView, DeleteView, UpdateView  , FormView
#
from accounts.forms import SignUpForm , ProfileUpdateForm
#
from django.contrib.auth.tokens import default_token_generator
#
from django.urls import reverse_lazy
#
from django.utils.translation import gettext_lazy as _
#
from django.shortcuts import resolve_url
#
#
#
#
#
#
#
# Log In The System
class My_Login(LoginView):
    template_name = 'registration/my_login.html'  # The Page HTML to Display
#
#
# Log Out Of The System:
class My_Logout(LogoutView):
    template_name = 'registration/my_logout.html'
#
#
# Display Them About Page
class My_LogoutDone(TemplateView):
    template_name = 'registration/my_logout_done.html' # The Page HTML to Display
#
#
# Confirm Checkout From System
class My_PasswordChange(PasswordChangeView):
    template_name = 'registration/my_password_change.html' 
    success_url = reverse_lazy('My_PasswordChangeDone_URL')
#
# 
#Confirm Password Change
class My_PasswordChangeDone(TemplateView):
    template_name = 'registration/my_password_change_done.html'
    # title = ('password change successful')
#
#
