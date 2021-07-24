#
from django.urls import path
from django.contrib.auth import views as auth_views # This Views Built-in Django
from django.urls import reverse_lazy
# from accounts.views import *
from accounts import views
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
    path('my_login/'                            , views.My_Login.as_view()                  , name='My_Login_URL'),
    path('my_logout/'                           , views.My_Logout.as_view()                 , name='My_Logout_URL'),
    path('my_logout_done/'                      , views.My_LogoutDone.as_view()             , name='My_LogoutDone_URL'),
    #*********************************************************************************
    path('my_password_change/'                 , views.My_PasswordChange.as_view()         , name='My_PasswordChange_URL'),
    path('my_password_change_done/'            , views.My_PasswordChangeDone.as_view()     , name='My_PasswordChangeDone_URL'),
]
#
#
# URL For Profile
urlpatterns += [
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

]
urlpatterns +=[
        path('signup/', views.signup, name="signup"),  
        path('activate/<uidb64>/<token>/',views.activate, name='activate'),  
]