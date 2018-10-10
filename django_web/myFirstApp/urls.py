from django.urls import path

from . import views
from django.views.generic import TemplateView
from .views import AboutView
from .models import Product
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about/', AboutView.as_view()),
    path('<int:pk>/', views.ProductDetail.as_view(), name='detail'),
    path('test/', views.test, name='test'),
]