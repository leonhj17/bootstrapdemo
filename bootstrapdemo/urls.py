"""bootstrapdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', include('ama.urls')),
    url(r'^index/', TemplateView.as_view(template_name="index.html")),
    url(r'^exe1/', TemplateView.as_view(template_name="exe1.html")),
    url(r'^exe2/', TemplateView.as_view(template_name="exe2.html")),
    url(r'^jsdom1/', TemplateView.as_view(template_name="jsdom1.html")),
    url(r'^jsdom7/', TemplateView.as_view(template_name="jsdom7.html")),
    url(r'^', include('fileops.urls', namespace='formtest')),
]
