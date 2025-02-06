"""
URL configuration for student_crm project.

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
from crm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',views.StudentCreate.as_view()),
    path('read/',views.StudentRead.as_view()),
    path('update/<int:pk>',views.StudentUpdate.as_view()),
    path('delete/<int:pk>',views.StudentDelete.as_view()),
    path('register/',views.RegisterView.as_view()),
    path('login/',views.LoginView.as_view())
]
