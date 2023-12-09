from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError

def authenticate_user(email, password):
    try:
        user = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    return None

@login_required(login_url = 'login/')
def cadastrar_usuario(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastrar_usuario.html')
    elif request.method == 'POST':
        # Salvar os dados da tela para o Banco de Dados:
        try:
            if Usuario.objects.filter(email= request.POST.get('email')).exists():
                messages.error(request,'Já existe um usuário com esse email cadastrado' )
                return render(request, 'usuarios/cadastrar_usuario.html')
                   
            novo_usuario = Usuario()
            novo_usuario.nome = request.POST.get('nome')
            novo_usuario.datanascimento = request.POST.get('datanascimento')
            novo_usuario.email = request.POST.get('email')
            novo_usuario.telefone = request.POST.get('telefone')
            novo_usuario.cidade = request.POST.get('cidade')
            novo_usuario.endereco = request.POST.get('endereco') 
            novo_usuario.username = request.POST.get('email')  
            novo_usuario.password = make_password(request.POST.get('password'))
            
            
            novo_usuario.save()
            messages.success(request, "Usuário criado com sucesso!")

            return redirect('/')
        except IntegrityError as error:
            
            messages.error(request, error )
            return render(request, 'usuarios/cadastrar_usuario.html')
 

@login_required(login_url = 'login/')
def usuarios(request):
# Exibir todos usuários cadastrados em uma nova página:
    usuarios = Usuario.objects.all()

    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html',{'usuarios':usuarios})

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('usuarios/')
        return render(request, 'usuarios/login.html')
    elif request.method =='POST':
        email= request.POST.get('email')
        senha= request.POST.get('password')
        print(email,senha)
        user_cliente = authenticate_user(email, senha)
        print(user_cliente)
        if user_cliente:         
            login_django(request, user_cliente)
            print(user_cliente)
            return redirect('usuarios/')
            
        
        else:
            messages.error(request, "E-mail ou senha incorretos!")
            return render(request, "usuarios/login.html")
        
def logout_view(request):
     logout(request)
     return redirect('/')
