from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.PostListView.as_view(), name='content'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post'),
    path('user_content', views.PostUserListView.as_view(), name='user_content'),
    path('create', views.PostCreateView.as_view(), name='create_post'),
    path('update/<int:pk>', views.PostUpdateView.as_view(), name='update_post'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='delete_post'),
]