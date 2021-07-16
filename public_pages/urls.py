from django.urls import path 
from public_pages import views
#
#
#
urlpatterns = [
    path('home'      , views.Index.as_view(), name='Index_URL'),
    path('about/'    , views.About.as_view(), name='About_URL'),
    
] 
