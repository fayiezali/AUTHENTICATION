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

# from django.contrib.auth.decorators import login_required
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

# class My_PasswordReset(PasswordResetView):
#     template_name = 'commons/my_password_reset.html'
#     subject_template_name = 'commons/password_reset_subject.txt'
#     success_url = reverse_lazy('My_password_reset_done_URL')
#     title = _('Password Reset')
# #
# #
# #
# #
# #
# #
# class My_PasswordResetDone(PasswordResetDoneView):
#     template_name = 'commons/my_password_reset_done.html'
#     title = _('Password Reset Sent')
# #
# #
# #
# #
# #
# #

# class My_PasswordResetConfirm(FormView):
#     # form_class = SetPasswordForm
#     # template_name = 'registration/my_password_reset_confirm.html'
#     post_reset_login = False
#     post_reset_login_backend = None
#     reset_url_token = 'set-password'
#     success_url = reverse_lazy('password_reset_complete')
#     template_name = 'commons/my_password_reset_confirm.html'
#     title = _('Enter new password')
#     token_generator = default_token_generator
# #
# #
# #
# #
# #
# #
# class My_PasswordResetComplete(PasswordResetCompleteView):
#     template_name = 'commons/my_password_reset_complete.html'
#     title = _('Password Reset Complete')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['My_Login_URL'] = resolve_url(settings.LOGIN_URL)
#         return context


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
#
#
#
#
# Log Out Of The System:
class My_Logout(LogoutView):
    template_name = 'registration/my_logout.html'
#
#
#
#
#
#
# Display Them About Page
class My_LogoutDone(TemplateView):
    template_name = 'registration/my_logout_done.html' # The Page HTML to Display
#
#
#
#
#
#
class My_PasswordChange(PasswordChangeView):
    template_name = 'registration/my_password_change.html' 
    success_url = reverse_lazy('My_PasswordChangeDone_URL')
#
# 
#
#
#
#
class My_PasswordChangeDone(TemplateView):
    template_name = 'registration/my_password_change_done.html'
    # title = ('password change successful')
