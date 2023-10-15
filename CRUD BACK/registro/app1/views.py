from pyexpat.errors import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, authenticate, login
from .models import Cadastro
from .models import Agenda
import pymysql


# Create your views here.


def SignUp(request):

    if request.method == 'POST':

        my_user = Cadastro()
        
        my_user.nome = request.POST.get('username')
        my_user.email = request.POST.get('email')
        my_user.senha = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        
        if my_user.senha != pass2:

            return HttpResponse('Senhas diferentes.')
        
        else:

            my_user.save()
            return redirect('login')
        
      
        
    return render(request, 'signup.html')



def SignIn(request):


    if request.method == 'POST':

        connection = pymysql.connect(user='root', passwd='luisa123@', host='127.0.0.1', database='cadastro')

        global unome

        usuario = request.POST['username']
        senha = request.POST['password']

        unome = usuario  

        cur = connection.cursor()

        sql = ("SELECT * FROM app1_cadastro WHERE nome = %s and senha = %s")
        
        cur.execute(sql, (usuario, senha))

        row = cur.fetchone()


        # Acaba para a verificação de Login, agora é para o ID


        cons = connection.cursor()

        sql2 = ("SELECT id FROM app1_cadastro WHERE nome = %s and senha = %s")

        cons.execute(sql2, (usuario, senha))

        row2 = cons.fetchone()

        global id_usuario

        global id_defer

        for x in row2:
            print(x)
            
        id_usuario = x
        
        id_defer = id_usuario
        

        if row == None:
            
            return render(request, 'login.html')
        
        else:

            return redirect('home')
        
  
   
    return render(request, 'login.html')



def Home(request):


    contatos = Agenda.objects.filter(id_cad_id=id_defer)


    if request.method == 'POST':

        connection = pymysql.connect(user='root', passwd='luisa123@', host='127.0.0.1', database='cadastro')
        
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')


        cur = connection.cursor()

        sql = ("INSERT INTO app1_agenda (nome, email, telefone, id_cad_id) VALUES (%s, %s, %s, %s)")

        cur.execute(sql, (nome, email, telefone, id_defer))

        connection.commit()

        return redirect('home')
        
    
    return render(request, 'home.html',{'nome':unome, 'id': id_usuario, 'contatos':contatos})



def edit(request, id):

    agenda = Agenda.objects.get(id=id) 

    if request.method == "POST": 

        agenda.nome = request.POST.get('nome')
        agenda.email = request.POST.get('email')
        agenda.telefone = request.POST.get('telefone')

        agenda.save()
        return redirect('home')

    return render(request, 'editar.html', {'lista':agenda})



def delete(request, id):
    agenda = Agenda.objects.filter(id=id)
    agenda.delete()
    return redirect('home')



def Logout(request):
    logout(request)
    return redirect('login')