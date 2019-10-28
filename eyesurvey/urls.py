"""eyesurvey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import detail

urlpatterns = [
    url(r'^$', detail, name='index'),
    url(r'^index.html', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', admin.site.urls),
]


