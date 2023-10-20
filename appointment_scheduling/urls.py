#URL configuration for appointment_scheduling project.

from django.contrib import admin
from django.urls import path
#views
from . import views as main_views
from login import views as login_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('/', main_views.home, name='home'),
    path('login/', login_views.login_view, name='login'),
    path('register/', login_views.register, name='register')
]
