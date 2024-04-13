"""
URL configuration for subhakaarya project.

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
from django.contrib import admin
from django.urls import path, include
from subhakaarya_app import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from account.views import VendorView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', views.EventView.as_view(), name='events'),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework')),
    path('auth/', include('account.urls')),
    path('vendors/', VendorView.as_view(), name='vendors'),
    path('services/', views.ServiceView.as_view(), name='services'),
    path('vendor-services/', views.VendorServiceView.as_view(), name='vendor-services'),
    path('plans/', views.PlanView.as_view(), name='plans'),
    path('vendorlist/', views.VendorlistView.as_view(), name='vendorlist'),
    path('verification/', include('verify_email.urls')),
    path('subhakaarya/',
         RedirectView.as_view(url='https://subhakaarya.com'), name='subhakaarya'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
