from django.urls import path, include
from posts.views import PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='index')
    # path('', views.index, name='index')
    ]
