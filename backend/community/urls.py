from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, ),

    path('<int:pk>', views.post),
    path('<int:pk>/<int:comment_id', views.comment)
]
