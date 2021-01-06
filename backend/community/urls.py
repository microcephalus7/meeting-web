from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('post/', views.posting, name="posting")
]
