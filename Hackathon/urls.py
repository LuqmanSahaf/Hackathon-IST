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
from django.views.generic import TemplateView

from .views import home, school, students, reports, groups, settingspricing

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home.index, name='home'),
    path('school/', school.index, name='school'),
    path('school/students', students.index, name='students'),
    path('school/reports', reports.index, name='reports'),
    path('school/groups', groups.index, name='groups'),
    path('statistics/', TemplateView.as_view(template_name='statistics/statistics.html'), name='statistics'),
    path('organisation/', TemplateView.as_view(template_name='organisation/organisation.html'), name='organisation'),
    path('economy/', TemplateView.as_view(template_name='economy/economy.html'), name='economy'),
    path('economy/settingspricing/', settingspricing.index, name='settingsPricing'),
    path('economy/calculate/', TemplateView.as_view(template_name='economy/calculate.html'), name='calculate'),
    path('economy/calculationmodel/', TemplateView.as_view(template_name='economy/calculation_models.html'),
         name='calculationModels'),
    path('economy/filteredcalculation/', TemplateView.as_view(template_name='economy/filtered_calculation.html'),
         name='filteredCalculation'),
    path('economy/pricingandaccounting/', TemplateView.as_view(template_name='economy/pricing_accounting.html'),
         name='pricingAndAccounting'),
    path('economy/receiver/', TemplateView.as_view(template_name='economy/receiver.html'), name='receiver'),
    path('economy/updatedata/', TemplateView.as_view(template_name='economy/update_data.html'), name='updateData'),
]
