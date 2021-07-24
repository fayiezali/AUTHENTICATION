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
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

UserModel = get_user_model()
from .forms import SignUpForm
from accounts.tokens import account_activation_token


def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')