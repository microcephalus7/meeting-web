from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, ),
    path('post/', views.post, ),
    path('<int:pk>/', views.detail, ),
    path('<int:pk>/modify', views.postModify, ),
    path('<int:pk>/delete', views.postDelete, ),
    path('<int:pk>/post', views.commentPost, ),
    path('<int:pk>/<int:comment_id>/modify', views.commentModify),
    path('<int:pk>/<int:comment_id>/delete', views.commentDelete)
]
