from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            # Lide com a autenticação de usuário falhada aqui
            pass
    return render(request, 'login/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já existe!')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email já cadastrado!')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Você foi registrado com sucesso!')
                return redirect('login')
        else:
            messages.error(request, 'As senhas não correspondem!')
    return render(request, 'login/register.html')