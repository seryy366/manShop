from django.urls import path
from .views import *


urlpatterns = [
    # path('', index, name='home'),
    # path('shop/', product_list, name='product_list'),
    path('shop/', ProductList.as_view(), name='product_list'),
    path('shop/<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('shop/<int:id>/<slug:slug>/', product_detail, name='product_detail'),

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', BlogPost.as_view(), name='home'),
    path('category/<str:slug>/', CategoryByPost.as_view(), name='category'),
    path('blog-details/<str:slug>/', ViewPost.as_view(), name='post'),
]