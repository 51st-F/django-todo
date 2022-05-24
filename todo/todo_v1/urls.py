from unicodedata import name
from django.urls import path
from todo_v1 import views

urlpatterns = [
    path('', views.list, name="list"),
    path('finish_item/<str:pk>', views.finish_item),
    path('delete_item/<str:pk>', views.delete_item),
]