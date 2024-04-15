from django.shortcuts import render

def menu(request):
    return render(request, "main/header.html")

def instruction(request):
    return render(request, "main/instruction.html")
