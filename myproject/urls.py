"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('', include('myapp.urls')),
    path('viewUserLogin',include('myapp.urls')),
    path('viewAdminLogin',include('myapp.urls')),
    path('adminLogin',include('myapp.urls')),
    path('adminLogout',include('myapp.urls')),
    path('createUser',include('myapp.urls')),
    path('admin/', admin.site.urls),
    path('userLogin',include('myapp.urls')),
    path('createUserView',include('myapp.urls')),
    path('viewUser',include('myapp.urls')),
    path('ajax-data',include('myapp.urls')),
    path('forgotPassword',include('myapp.urls')),
    path('validateFgtPwd',include('myapp.urls')),
    path('changePassword',include('myapp.urls')),




]
