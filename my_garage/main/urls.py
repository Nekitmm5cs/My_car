from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('instruction/', views.instruction_view, name='instruction'),
    path('input/', views.input_view, name='input'),
    path('reminder/', views.reminder_view, name='reminder'), 
    path('wheels/', views.wheels_view, name='wheels'),  
    path('map/', views.map_view, name='map'),  
    path('maps/', views.maps_view, name='maps'), 
    path('idea/', views.idea_view, name='idea'),  
]
