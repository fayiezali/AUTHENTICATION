# from django.contrib.auth import views as auth_views
# from  accounts import views
# from django.urls import reverse_lazy

# from django.urls import path

# urlpatterns = [
#     path('login/'          , auth_views.LoginView.as_view()  , name='login'),
#     path('logout/'         , auth_views.LogoutView.as_view() , name='logout'),
    
#     path('my_logout_done/' , views.My_LogoutDone.as_view()    , name='My_LogoutDone_URL'),


#     path('my_password_change/'      , views.My_PasswordChange.as_view()         , name='My_PasswordChange_URL'),
#     path('my_password_change_done/' , views.My_PasswordChangeDone.as_view()     , name='My_PasswordChangeDone_URL'),

#     # path('password_change/'      , auth_views.PasswordChangeView.as_view()     , name='password_change'),
#     # path('password_change/done/' , auth_views.PasswordChangeDoneView.as_view() , name='password_change_done'),


#     # path('password_reset/'         , auth_views.PasswordResetView.as_view()         , name='password_reset'),
#     # path('password_reset/done/'    , auth_views.PasswordResetDoneView.as_view()     , name='password_reset_done'),
#     # path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view()  , name='password_reset_confirm'),
#     # path('reset/done/'             , auth_views.PasswordResetCompleteView.as_view() , name='password_reset_complete'),
# ]
# Good Wording - start========================================
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
urlpatterns  =[
# Forget Password
    path('password-reset/',
        auth_views.PasswordResetView.as_view(
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        template_name='commons/password_reset.html',
        #The Full Name Of a Template To Use For GEnerating The Email With The Reset Password Link
        subject_template_name='registration/password_reset_subject.txt',
        # The URL To Redirect To After a Successful Password Reset Request
        success_url= reverse_lazy('password_reset_done')),
                name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        template_name='commons/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        template_name='commons/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
        # The Full Name Of a Template to Use For Displying The Password Reset Form
        template_name='commons/password_reset_complete.html'),
        name='password_reset_complete'),
]
# Good Wording - End=======================================

# Start New**********************************************************

# from django.urls import path
# from django.contrib.auth import views as auth_views
# #
# urlpatterns = [
#     path('login/'                  , auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('logout/'                 , auth_views.LogoutView.as_view(), name='logout'),
#     #********************************************************************************
#     path('password_change/'        , auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
#     path('password_change/done/'   , auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
#     #********************************************************************************
#     path('password_reset/'         , auth_views.PasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/'    , auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/'             , auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
#     #********************************************************************************
# ]
#############################################################################################################################################################
# Good Wording - start========================================
# from django.urls import path
# from django.contrib.auth import views as auth_views

# urlpatterns =[
# # Forget Password
#     path('password-reset/',
#         auth_views.PasswordResetView.as_view(
#         # The Full Name Of a Template to Use For Displying The Password Reset Form
#         template_name='commons/password_reset.html',
#         #The Full Name Of a Template To Use For GEnerating The Email With The Reset Password Link
#         subject_template_name='commons/password_reset_subject.txt',
#         # The URL To Redirect To After a Successful Password Reset Request
#         success_url= reverse_lazy('password_reset_done')),
#                 name='password_reset'),
#     path('password-reset/done/',
#         auth_views.PasswordResetDoneView.as_view(
#         # The Full Name Of a Template to Use For Displying The Password Reset Form
#         template_name='commons/password_reset_done.html'),
#         name='password_reset_done'),
#     path('password-reset-confirm/<uidb64>/<token>/',
#         auth_views.PasswordResetConfirmView.as_view(
#         # The Full Name Of a Template to Use For Displying The Password Reset Form
#         template_name='commons/password_reset_confirm.html'),
#         name='password_reset_confirm'),
#     path('password-reset-complete/',
#         auth_views.PasswordResetCompleteView.as_view(
#         # The Full Name Of a Template to Use For Displying The Password Reset Form
#         template_name='commons/password_reset_complete.html'),
#         name='password_reset_complete'),
# ]
# Good Wording - End=======================================

from django.urls import path

from django.contrib.auth import views as views_django_authentication # This Views Built-in Django

# from accounts.views import *

from accounts import views

from django.contrib.auth import views as auth_views

# urlpatterns = [

#     path("reset_password"                           , auth_views.PasswordResetView.as_view(         template_name="registration/password_reset_form.html")          , name="password_reset_URL"),
#     path("password_reset_done/"                     , auth_views.PasswordResetDoneView.as_view(     template_name="registration/password_reset_done.html")     , name="password_reset_done_URL"),
#     path("reset_password_confirm/<uidb64>/<token>"  , auth_views.PasswordResetConfirmView.as_view(  template_name="registration/password_reset_confirm.html")  , name="password_reset_confirm_URL"),
#     path("reset_password_complete/"                 , auth_views.PasswordResetCompleteView.as_view( template_name="registration/password_reset_complete.html") , name="password_reset_complete_URL")
# ]
#
#
#
#


#
#
# urlpatterns = [
#     path('my_reset_password/'                        , views.My_PasswordReset.as_view()         , name ='My_reset_password_URL'),
#     path('my_reset_password_sent/'                   , views.My_PasswordResetDone.as_view()     , name ='My_password_reset_done_URL'),
#     path('my_password-reset-confirm/<uidb64>/<token>/'  , views.My_PasswordResetConfirm.as_view()  , name ='My_password_reset_confirm_URL'),
#     path('my_reset_password_complete/'               , views.My_PasswordResetComplete.as_view() , name ='My_password_reset_complete_URL')
# ]
#
#
urlpatterns += [
    path('my_login/'                            , views.My_Login.as_view()                  , name='My_Login_URL'),
    path('my_logout/'                           , views.My_Logout.as_view()                 , name='My_Logout_URL'),
    path('my_logout_done/'                      , views.My_LogoutDone.as_view()             , name='My_LogoutDone_URL'),
    #*********************************************************************************
    # path('my_signup/'                           , My_Signup.as_view()                 , name='My_Signup_URL'),
    # path('my_profile_update/<int:pk>/'          , My_ProfileUpdate.as_view()          , name='my_profile_update_URL'),
    # path('my_Profile_delete/<int:pk>/delete/'   , My_ProfileDelete.as_view()          , name='my_Profile_delete_URL'),
    # path('my_profile_list/'                     , my_profile_list.as_view()           , name='my_profile_list_URL'),
    # path('my_profile_detail_slug/<slug:slug>/'  , My_Profile_Detail_Slug.as_view()    , name='My_Profile_Detail_Slug_URL'), 
    #*********************************************************************************
    # path('my_Profile_Detail_ID/<int:pk>/'       , My_Profile_Detail_ID.as_view()      , name='My_Profile_Detail_ID_URL'),
    # path('associationdetailid/<int:pk>/'       , AssociationDetailViewID.as_view()   , name='AssociationData_MODEL-detail'),
    # <td><a href="{{ object_list_item.get_absolute_url }}">{{ object_list_item.ASS_NameAssociation }}</a> ({{object_list_item.ASS_Phone}})</td> <!-- This Link Is From The Database and usls.py File-->
    #*********************************************************************************
    path('my_password_change/'                 , views.My_PasswordChange.as_view()         , name='My_PasswordChange_URL'),
    path('my_password_change_done/'            , views.My_PasswordChangeDone.as_view()     , name='My_PasswordChangeDone_URL'),
    # path('my_password_reset/'                  , My_PasswordReset.as_view()          , name='My_PasswordReset_URL'),
    # path('password_reset/done/'                , My_PasswordResetDone.as_view()      , name='My_PasswordResetDone_URL'),
    # # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), 

]



