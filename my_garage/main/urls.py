from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('instruction', views.instruction_view, name='instruction'),
    path('input', views.input_view, name='input'),
]