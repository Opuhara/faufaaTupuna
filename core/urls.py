# core/urls.py
from django.urls import path
from core.views import index, styles

urlpatterns = [
    path('', index, name='index'),
    path('styles', styles, name='styles'),
]
