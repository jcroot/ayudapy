"""ayudapy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from conf import api_urls
from core import views as core_views
from org import views as org_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('recibir', TemplateView.as_view(template_name="info_request.html")),
    path('solicitar', core_views.request_form, name="request-form"),
    path('dar', TemplateView.as_view(template_name="info_give.html")),
    path('legal', TemplateView.as_view(template_name="legal.html")),
    path('pedidos/<int:id>', core_views.view_request, name='pedidos-detail'),
    path('pedidos_ciudad/<slug:city>', core_views.list_by_city, name='pedidos-by-city'),
    path('pedidos', core_views.list_requests),
    path('preguntas_frecuentes', core_views.view_faq, name='general_faq'),
    path('contacto', TemplateView.as_view(template_name="contact_us.html"), name='contact_us'),
    path('tag/<slug:slug>', core_views.tagged, name="tagged"),
    path('tag/<slug:slug>/pedidos_ciudad/<slug:city>', core_views.tagged_with_city, name="tagged_with_city")
    path('donaciones', org_views.list_donation),
    path('donaciones_ciudad/<slug:city>', org_views.list_donation_by_city, name='donation-by-city'),
    path('donaciones/<int:id>', org_views.view_donation_center, name='donaciones-detail'),
]
urlpatterns += api_urls.urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
