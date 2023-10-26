from django.shortcuts import render

def home(request):
    return render(request, 'data_visualization/home.html')
