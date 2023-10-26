#URL configuration for appointment_scheduling project.

from django.contrib import admin
from django.urls import path
#views
from login import views as login_views
from calendar_app import views as calendar_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', login_views.login_view, name='login'),
    path('register/', login_views.register, name='register')
]
