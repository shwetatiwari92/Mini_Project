from django.urls import path
from .views import *

urlpatterns=[
    path('', admin_index, name='admin_index'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:pid>',edit_product,name='edit_products'),
    
]