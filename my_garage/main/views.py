from django.shortcuts import render

def menu_view(request):
    return render(request, "main/header.html")

def instruction_view(request):
    return render(request, "main/instruction/instruction.html")

def input_view(request):
    return render(request, 'instruction/input.html')
