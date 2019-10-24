"""Hackathon URL Configuration

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
from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import home
from .views import school
from .views import students
from .views import reports
from .views import groups

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home/home.html'),name='home'),
    path('school/',TemplateView.as_view(template_name='school/school.html'), name='school'),
    path('school/students',TemplateView.as_view(template_name='school/students.html'), name='students'),
    path('school/reports',TemplateView.as_view(template_name='school/reports.html'), name='reports'),
    path('school/groups',TemplateView.as_view(template_name='school/groups.html'), name='groups'),
    path('statistics/',TemplateView.as_view(template_name='statistics/statistics.html'), name='statistics'),
    path('organisation/',TemplateView.as_view(template_name='organisation/organisation.html'), name='organisation'),
    path('economy/',TemplateView.as_view(template_name='economy/economy.html'), name='economy'),
    path('economy/settingspricing/',TemplateView.as_view(template_name='economy/settings_pricing.html'), name='settingsPricing'),
    path('economy/calculate/',TemplateView.as_view(template_name='economy/calculate.html'), name='calculate'),
    path('economy/calculationmodel/',TemplateView.as_view(template_name='economy/calculation_models.html'), name='calculationModels'),
    path('economy/filteredcalculation/',TemplateView.as_view(template_name='economy/filtered_calculation.html'), name='filteredCalculation'),
    path('economy/pricingandaccounting/',TemplateView.as_view(template_name='economy/pricing_accounting.html'), name='pricingAndAccounting'),
    path('economy/receiver/',TemplateView.as_view(template_name='economy/receiver.html'), name='receiver'),
    path('economy/updatedata/',TemplateView.as_view(template_name='economy/update_data.html'), name='updateData'),
]


