#
from django.urls import path
from django.contrib.auth import views as auth_views # This Views Built-in Django
from django.urls import reverse_lazy
from accounts import views
# from django.conf import settings
# from .tokens import user_tokenizer
#
#
#
# URL To Handle Password
urlpatterns  =[
    # The Full Name Of a Template to Use For Displying The Password Reset Form
    #The Full Name Of a Template To Use For GEnerating The Email With The Reset Password Link
    # The URL To Redirect To After a Successful Password Reset Request
    path('password-reset/'                             , auth_views.PasswordResetView.as_view(
        template_name='commons/password_reset.html', 
        subject_template_name='registration/password_reset_subject.txt',
        success_url= reverse_lazy('password_reset_done')),
        name='password_reset'),
        #
    # The Full Name Of a Template to Use For Displying The Password Reset Form
    path('password-reset/done/'                       , auth_views.PasswordResetDoneView.as_view(
        template_name='commons/password_reset_done.html'),
        name='password_reset_done'),
        #
    # The Full Name Of a Template to Use For Displying The Password Reset Form
    path('password-reset-confirm/<uidb64>/<token>/'  , auth_views.PasswordResetConfirmView.as_view(
        template_name='commons/password_reset_confirm.html'),
        name='password_reset_confirm'),
        #
    # The Full Name Of a Template to Use For Displying The Password Reset Form
    path('password-reset-complete/'                 , auth_views.PasswordResetCompleteView.as_view(
        template_name='commons/password_reset_complete.html'),
        name='password_reset_complete'),
]
#
#
# URL For Authentication
urlpatterns += [
    # Login In System   
    path('my_login/'                            , views.My_Login.as_view()                  , name='My_Login_URL'),
    # Exit From System
    path('my_logout/'                           , views.My_Logout.as_view()                 , name='My_Logout_URL'),
    # Checkout Confirmed Successfull
    path('my_logout_done/'                      , views.My_LogoutDone.as_view()             , name='My_LogoutDone_URL'),
    #*********************************************************************************
    # Change Password
    path('my_password_change/'                 , views.My_PasswordChange.as_view()         , name='My_PasswordChange_URL'),
    # Password Change completed Succesfull
    path('my_password_change_done/'            , views.My_PasswordChangeDone.as_view()     , name='My_PasswordChangeDone_URL'),
]
#
#
#URL For Profile (1)
urlpatterns +=[
        # Signup And Confirm Registration With Email
        path('my_signup/'                  , views.My_Signup.as_view()  , name='My_Signup_URL'), 
        # Active Registration Withe Email.
        path('activate/<uidb64>/<token>/'  , views.Activate.as_view()   , name='activate'),  
]
#
#
# URL For Profile(2)
urlpatterns += [
    # path('my_signup/'                         , views.My_Signup.as_view()                 , name='My_Signup_URL'),
    path('my_profile_contact_us/'               , views.My_ProfileContactUs                 , name='My_Profile_Contact_Us'),
    path('my_profile_update/<int:pk>/'          , views.My_ProfileUpdate.as_view()          , name='my_profile_update_URL'),
    # Delete Profile
    path('my_Profile_delete/<int:pk>/delete/'   , views.My_ProfileDelete.as_view()          , name='my_Profile_delete_URL'),
    # View a List Of The Profiles 
    path('my_profile_list/'                     , views.my_profile_list.as_view()           , name='my_profile_list_URL'),
    # View Profile Details By (slug)
    path('my_profile_detail_slug/<slug:slug>/'  , views.My_Profile_Detail_Slug.as_view()    , name='My_Profile_Detail_Slug_URL'), 
    #*********************************************************************************
    # View Profile Details By (ID)
    path('my_Profile_Detail_ID/<int:pk>/'       , views.My_Profile_Detail_ID.as_view()      , name='My_Profile_Detail_ID_URL'),
    # Show Details In The Profile - But The code Is Written In The Model
    # path('associationdetailid/<int:pk>/'       , AssociationDetailViewID.as_view()   , name='AssociationData_MODEL-detail'),
    # <td><a href="{{ object_list_item.get_absolute_url }}">{{ object_list_item.ASS_NameAssociation }}</a> ({{object_list_item.ASS_Phone}})</td> <!-- This Link Is From The Database and usls.py File-->
    #*********************************************************************************
]
#
#
#
