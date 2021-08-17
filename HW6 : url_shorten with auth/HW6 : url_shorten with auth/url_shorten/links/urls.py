from django.urls import path, re_path
from . import views

app_name = 'links'
urlpatterns = [
    path('', views.main, name='main'),
    path('reduce_link', views.reduce_link, name='reduce_link'),
    path('redirect_link/<str:new_key>', views.redirect_link, name='redirect_link'),
    path('<str:key>', views.link, name='link'),
    #re_path(r"\S*", views.random_link, name='random_link'),
]