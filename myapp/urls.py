"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
     path('', views.IndexView, name="index"),
     path("submittd/",views.insertData,name="insert"),
    #  path("in/",views.Ins,name="insert")
    #  path('show_file', views.showfile, name="show_file"),
    #  path('form',views.formview,name="form")

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
