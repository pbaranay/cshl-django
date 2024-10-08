"""
URL configuration for bearlab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from lab import views as lab_views
from web import views as web_views


urlpatterns = [
    path('', web_views.homepage),
    path('admin/', admin.site.urls),
    path('staff/', lab_views.all_lab_members, name="all_staff"),
    path('staff/<slug:slug>/', lab_views.staff_page, name="staff_page"),
]
