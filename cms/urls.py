from django.urls import path
from cms import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.HomePageView.as_view(), name='home'),
    #path('detail/<id>/', views.detail, name='detail'),
    path('detail/<pk>/', views.DetailPageView.as_view(), name='detail'),
    path('search/', views.search, name='search'),
    path('delete/<id>/', views.Delete, name='delete'),
    path('contacts/create/', views.ContactCreateView.as_view(), name='create'),
    path('contacts/update/<pk>/', views.ContactUpdateView.as_view(), name='update'),
    #path('contacts/delete/<pk>/', views.ContactDeleteView.as_view(), name='delete'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
