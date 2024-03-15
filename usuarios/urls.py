from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-vendedor/', views.cadastrar_vendedor, name='cadastrar-vendedor')
]
