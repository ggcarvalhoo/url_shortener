from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('check_url/', views.check_url, name='check_url'),
    path('url/<str:link>/', views.redirect_url, name='redirect_url')
]
