from django.shortcuts import render

def home(request):
    return render(request, 'appointment_scheduling/home.html')
