from django.shortcuts import render

def menu_view(request):
    return render(request, "main/header.html")

def instruction_view(request):
    return render(request, "main/instruction/instruction.html")

def input_view(request):
    return render(request, 'main/instruction/input.html')

def reminder_view(request):
    return render(request, 'main/instruction/reminder.html')

def map_view(request):
    return render(request, 'main/instruction/map.html')

def idea_view(request):
    return render(request, 'main/idea.html')