"""python_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path,include
from tutorial import views

urlpatterns = [
    # Invoke the home view in the tutorial app by default
    re_path(r'^$', views.home, name='home'),
    # Defer any URLS to the /tutorial directory to the tutorial app
    re_path(r'^tutorial/', include('tutorial.urls', namespace='tutorial')),
    re_path(r'^admin/', admin.site.urls),
]

