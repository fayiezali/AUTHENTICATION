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
from django.views.generic import TemplateView , ListView ,DetailView , DeleteView, UpdateView  , FormView
#
from accounts.forms import SignUpForm 
#
from django.contrib.auth.tokens import default_token_generator
#
from django.urls import reverse_lazy
#
#
from django.shortcuts import resolve_url
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import json
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group, Permission
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render
from django.views import View
# from guardian.conf import settings as guardian_settings
# from guardian.mixins import PermissionRequiredMixin
# from guardian.shortcuts import assign_perm, get_objects_for_user
from .tokens import user_tokenizer
# from accounts.forms import RegistrationForm
UserModel = get_user_model()
from .forms import SignUpForm
from accounts.tokens import account_activation_token
#
#
#
# Log In The System
class My_Login(LoginView):
    template_name = 'registration/my_login.html'  # The Page HTML to Display
#
#
#
# Log Out Of The System:
class My_Logout(LogoutView):
    template_name = 'registration/my_logout.html'# The Page HTML to Display
#
#
#
# Display Them About Page
class My_LogoutDone(TemplateView):
    template_name = 'registration/my_logout_done.html' # The Page HTML to Display
#
#
#
# Confirm Checkout From System
class My_PasswordChange(PasswordChangeView):
    template_name = 'registration/my_password_change.html' # The Page HTML to Display
    success_url = reverse_lazy('My_PasswordChangeDone_URL') # Go to This Page After Successful Operation
#
#
#
#Confirm Password Change
class My_PasswordChangeDone(TemplateView):
    template_name = 'registration/my_password_change_done.html'# The Page HTML to Display
    # title = ('password change successful')
#
#
#
# Register On The site And Create a Profile
class My_Signup(View):
    # (1) View Data
    def get(self , request):
        # Show User Registration Form
        return render(request, 'registration/my_signup.html', {'form': SignUpForm})
    # (2) Save Data
    def post(self, request):  
        if request.method == 'GET':
            return render(request, 'registration/my_signup.html')
        if request.method == 'POST':
            form = SignUpForm(request.POST)#Save The User Request In The Variable
            # print(form.errors.as_data())
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Please Activate Your Account.'
                message = render_to_string('registration/accounts_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user), })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()# Send Email
                # Show User Confirm Email Registration Form
                return render(request, 'registration/confirm_email_registration.html', {'message': f'A confirmation email has been sent to {user.email}. Please confirm to finish registering'})
#
#
#
class Activate(View):
    def get(self, request, uidb64  , token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True # User Activation
            user.save() # Data Save
            # Show Confirm Email Registration Form And Dysplay Message For Successful Operation 
            return render(request, 'registration/confirm_email_registration_done.html', {'message': f'A confirmation email has been sent to {user.email}. Please confirm to finish registering'})
        else:
            # Show Activation Link Invalid Form For Unsuccessful Operation
            return render(request, 'registration/Activation_link_invalid.html')
#
#
#
# Display List Record
class my_profile_list(LoginRequiredMixin , ListView):
    model = User # Data Table
    paginate_by = 4  # if pagination is desired
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now() # Data To Be Sent To Page HTML
        return context # Send This Data To The Required Page HTML
    template_name = 'registration/my_profile_list.html'# The Page HTML to Display
#
#
#
# Display Detail Record By: Slug
class My_Profile_Detail_Slug(LoginRequiredMixin ,  DetailView):
    model = User # Data Table
    slug_field = 'ASS_Slug' # Filter Field Use 'Slug'
    context_object_name = 'My_Object' # Data To Be Sent To Page HTML
    template_name = 'registration/my_profile_detail_slug.html'# The Page HTML to Display
#
#
#
## Display Detail Record By: ID
class My_Profile_Detail_ID(LoginRequiredMixin , DetailView):
    model = User # Data Table
    slug_field = 'pk' # Filter Field Use 'PK"
    context_object_name = 'My_Object' # Data To Be Sent To Page HTML
    template_name = 'registration/my_profile_detail_ID.html'# The Page HTML to Display
#
#
#
# Update Profile.
class My_ProfileUpdate(UpdateView):
        model = User # Data Table
        fields = [ # Fields Table
            'last_login',
            'is_superuser', 
            'username', 
            'last_name',
            'email',
            'is_staff', 
            'is_active', 
            'date_joined',
            'first_name',
            ]
        template_name = 'registration/My_ProfileUpdate.html'# The Page HTML to Display
        success_url = reverse_lazy('Index_URL')# Go to This Page After Successful Operation
#
#
#
# Delete Record.
class My_ProfileDelete(LoginRequiredMixin  , DeleteView):
    model = User # Data Table
    template_name = 'registration/my_profile_confirm_delete.html' # The Page HTML to Display
    success_url = reverse_lazy('Index_URL') # Go to This Page After Successful Operation
#
#
#
#
#
#
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Send Email From
def My_ProfileContactUs(request):
	if request.method == 'POST':
		subject = request.POST['subject']
		message = request.POST['message']
		send_to = request.POST['send_to']
		send_mail(subject,
		message, 
		settings.EMAIL_HOST_USER,
		[send_to], 
		fail_silently=False,)
	return render(request, 'registration/my_profile_contact_us.html')
#

# import requests
# from django.contrib.auth.models import User
# from django.http import JsonResponse

# def send_otp(request):
#     response_data = {}
# 	if request.method == "POST" and request.is_ajax:
#         user_phone = request.POST['phone_number']
# 		url = "http://2factor.in/API/V1/293832-67745-11e5-88de-5600000c6b13/SMS/" + user_phone +  "/AUTOGEN/OTPSEND"
# 		response = requests.request("GET", url)
# 		data = response.json()
# 		request.session['otp_session_data'] = data['Details']
#         # otp_session_data is stored in session.
# 		response_data = {'Message':'Success'}
# 	else:
# 		response_data = {'Message':'Failed'}
# 	return JsonResponse(response_data)
# #
# #

# def otp_verification(request):
# 	response_data = {}
# 	if request.method == "POST" and request.is_ajax:
# 		user_otp = request.POST['otp']
# 		url = "http://2factor.in/API/V1/293832-67745-11e5-88de-5600000c6b13/SMS/VERIFY/" + 
#             request.session['otp_session_data'] + "/" + user_otp + ""
#         # otp_session_data is fetched from session.
# 		response = requests.request("GET", url)		
# 		data = response.json()
# 		if data['Status'] == "Success":
# 			logged_user.is_active = True
# 			response_data = {'Message':'Success'}
# 		else:
# 			response_data = {'Message':'Failed'}
# 			logout(request)
# 	return JsonResponse(response_data)