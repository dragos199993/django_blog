from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']

        if password == password_repeat:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'registration/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Credentials invalid!')
            return redirect('login')

    return render(request, 'registration/login.html')
