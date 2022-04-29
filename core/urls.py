from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('check_url/', views.check_url, name='check_url'),
    path('/<str:link>', views.redirect, name='redirect')
]
