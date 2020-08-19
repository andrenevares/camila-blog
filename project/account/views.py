from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
# from django.contrib.auth import login
# # from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # se o método for POST eu vou instaciar com os dados do Form
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Nova conta criada para {username}')
            # login(request, user)
            return redirect ('account/login.html')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
            return render (request, 'account/register.html', {'form': form})
    else:
        # Caso contrário vou trazer apenas o Form
        form = UserRegisterForm()
    return render (request, 'account/register.html', {'form': form})

def profile(request):
    return render (request, 'account/profile.html')