from django.urls import path
from cms import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home_class/', views.HomePageView.as_view(), name='home2'),
    path('detail/<id>/', views.detail, name='detail'),
    path('detail_class/<pk>/', views.DetailPageView.as_view(), name='detail2'),
    path('search/', views.search, name='search'),
    path('update/<id>/', views.detail, name='update'),
    path('delete/<id>/', views.detail, name='delete'),
    path('contacts/create/', views.ContactCreateView.as_view(), name='create'),
]
