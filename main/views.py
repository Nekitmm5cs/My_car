from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def menu_view(request):
    return render(request, "main/header.html")

def news_view(request):
    return render(request, "main/scraping/news/scraping_news.html")

def idea_view(request):
    return render(request, 'main/idea_elements/idea.html')

def log_view(request):
    return render(request, 'main/login/log.html')

def reg_view(request):
    return render(request, 'main/login/registration/reg.html')