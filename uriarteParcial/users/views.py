from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm
# Create your views here.

def login_user(request):
    form = LoginForm()
    message=''
   
    if request.method=='POST':    
        form = LoginForm(request.POST)  
        if form.is_valid():
            print('Metodo:', request.method)
            cd = form.cleaned_data #recupera la data limpia
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    message = f'Hola {user.username}!! Te has logueado'
                    return render(request,'base.html',{'user:': user})
                else:
                    message = 'El usuario ingresado no se encuentra activo'
            else:
                message = 'Cuenta inválida'

    return render(request,'users/login.html', context={'form': form, 'messages': message})

def register_user(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request,'users/registro.html', {'form':form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Usuario creado correctamente')
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/registro.html', {'form': form})
        
def sign_out(request):
    logout(request)
    messages.success(request, f'Acabas de cerrar tu sesión.')
    return redirect('home')