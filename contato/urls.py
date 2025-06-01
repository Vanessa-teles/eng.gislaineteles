from django.urls import path
from . import views

app_name = 'contato'

urlpatterns = [
    path('', views.contato_view, name='contato'),
    path('sucesso/', views.sucesso_view, name='sucesso'),
]
