"""
URL configuration for CRIME_PREDICTION project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from accounts import views as account_views
from pages_views import (
    about_view, ai_dashboard_view, statistics_view, 
    heatmap_view, safety_measures_view, sos_emergency_view, contact_view,
    crimes_api,
    crime_prediction_api,
    heatmap_api,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Show the login page at the root so unauthenticated visitors see the
    # sign-in form first. After successful login users are redirected to
    # `/home/` (see `accounts.views`).
    path('', account_views.login_view, name='root_login'),
    # Serve the homepage on `/home/` so the root can be used for auth.
    path('home/', TemplateView.as_view(template_name='home..html'), name='home'),
    # Pages
    path('about/', about_view, name='about'),
    path('ai-dashboard/', ai_dashboard_view, name='ai_dashboard'),
    path('statistics/', statistics_view, name='statistics'),
    path('heatmap/', heatmap_view, name='heatmap'),
    path('api/predict/', crime_prediction_api, name='api_predict'),
    path('api/crimes/', crimes_api, name='api_crimes'),
    path('api/heatmap/', heatmap_api, name='api_heatmap'),
    path('report/', TemplateView.as_view(template_name='report.html'), name='report'),
    path('safety-measures/', safety_measures_view, name='safety_measures'),
    path('sos-emergency/', sos_emergency_view, name='sos_emergency'),
    path('contact/', contact_view, name='contact'),
    # Personal/Special pages
    path('special/sorry/', TemplateView.as_view(template_name='pages/personal/1.html'), name='sorry_page'),
    path('birthday/', TemplateView.as_view(template_name='birthday/index.html'), name='birthday'),
    # Accounts (register/login/logout)
    path('', include('accounts.urls')),
]
