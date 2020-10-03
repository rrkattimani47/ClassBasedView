"""CBV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('function1/',views.function1,name='function1'),
    path('cbv/',views.CBV.as_view(),name='CBV'),
    path('FBV_template/',views.FBV_template,name='FBV_template'),
    path('CBV_template/',views.CBV_template.as_view(),name='CBV_template'),
    path('FBV_form/',views.FBV_form,name='FBV_form'),
    path('CBV_form/',views.CBV_form.as_view(),name='CBV_form'),
    
    path('template_view/',views.template_view.as_view(),name='template_view'),

]