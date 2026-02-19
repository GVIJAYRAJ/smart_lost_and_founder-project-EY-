from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from core.views import chatbot


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='login.html'), name='home'),
    path('login.html', TemplateView.as_view(template_name='login.html'), name='login'),

    path('dashboard.html', TemplateView.as_view(template_name='dashboard.html')),
    path('about.html', TemplateView.as_view(template_name='about.html')),
    path('help.html', TemplateView.as_view(template_name='help.html')),
    path('pricing.html', TemplateView.as_view(template_name='pricing.html')),
    path('privacy.html', TemplateView.as_view(template_name='privacy.html')),
    path('report.html', TemplateView.as_view(template_name='report.html')),
    path('found.html', TemplateView.as_view(template_name='found.html')),
    path('item.html', TemplateView.as_view(template_name='item.html')),
    path('project.html', TemplateView.as_view(template_name='project.html')),
    path('contract.html', TemplateView.as_view(template_name='contract.html')),
    path('admin.html', TemplateView.as_view(template_name='admin.html')),

path('chatbot/', chatbot, name='chatbot'),
]
