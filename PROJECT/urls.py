"""PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
#
#
urlpatterns = [
    path('admin/', admin.site.urls),
]
#
#
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')), # This Path Coming From Django App
]
#
#
urlpatterns += [
    path('public_pages/', include('public_pages.urls')),# Path App Public_Pages
    path('accounts/', include('accounts.urls')), # This Path I was Created From My App
    
]

#
#
#
#
# Download These Folders If There are No Errors In the Serveer
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
#
#
urlpatterns += [
    path('', include('social_django.urls')),
]
