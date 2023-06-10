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

from django.urls import path
from .import views

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('viewUserLogin', views.view_user_login, name='viewUserLogin'),
    path('viewAdminLogin', views.view_admin_login, name='viewAdminLogin'),
    path('adminLogin',views.admin_login, name='adminLogin'),
    path('adminLogout',views.admin_logout, name='adminLogout'),
    path('createUser',views.create_user, name='createUser'),
    path('userLogin',views.user_login, name='userLogin'),
    path('createUserView',views.create_user_view, name='createUserView'),
    path('viewUser',views.view_user, name='viewUser'),
    path('ajax-data',views.view_user_api, name='ajax-data'),
    path('forgotPassword',views.forgot_password, name='forgotPassword'),
    path('validateFgtPwd',views.validate_forgot_password, name='validateFgtPwd'),
    path('changePassword',views.change_password, name='changePassword'),







]
