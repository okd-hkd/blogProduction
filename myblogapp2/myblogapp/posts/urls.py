from django.urls import path, include, re_path
from posts.views import PostListView
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    # path('', views.index, name='index'),
    re_path(r'(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
   ]
#
# urlpatterns += i18n_patterns(
#     path('about/', about_views.main, name='about'),
#     path('news/', include(news_patterns, namespace='news')),
# 　　
