from django.urls import path
from . import views

urlpatterns = [
    path('add-produto/', views.add_produto, name='add-produto'),
]
