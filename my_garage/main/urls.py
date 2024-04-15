from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('instruction', views.instruction, name='instruction')

]