from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('instruction', views.instruction_view, name='instruction'),
    path('input', views.input_view, name='input'),
    path('reminder', views.reminder_view, name='reminder'),
    path('map', views.map_view, name='map'),
    path('idea', views.idea_view, name='idea'),
]