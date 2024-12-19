from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('scraping_news/', views.news_view, name='news'),
    path('idea/', views.idea_view, name='idea'),
    path('login/', views.log_view, name='log'),
    path('reg/', views.reg_view, name='reg')
]
