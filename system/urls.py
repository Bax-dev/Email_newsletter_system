# newsletter/urls.py

from django.urls import path
from .views import subscribe, subscribe_success, create_newsletter, send_newsletter

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('subscribe/success/', subscribe_success, name='subscribe_success'),
    path('system/create/', create_newsletter, name='create_newsletter'),
    path('system/send/<int:newsletter_id>/', send_newsletter, name='send_newsletter'),
]
