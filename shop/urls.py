from django.urls import path
from . import views


app_name ='shop'

urlpatterns = [
    path('shop/', views.content_list, name='product_list'),
    path('shop/(?P<category_slug>[-\w]+)/', views.content_list, name='product_list_by_category'),
    path('shop/(?P<id>\d+)/(?P<slug>[-\w]+)/', views.contant_detail, name='product_detail'),
]