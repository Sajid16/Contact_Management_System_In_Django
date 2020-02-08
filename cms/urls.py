from django.urls import path
from cms import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]
