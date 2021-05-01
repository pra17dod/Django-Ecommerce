from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', item_list, name='item-list')
]
