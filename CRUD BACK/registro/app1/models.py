from django.db import models

class Cadastro(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=150)
    email = models.EmailField(max_length=150)
    senha = models.TextField(max_length=150)


class Agenda(models.Model):

    id = models.AutoField(primary_key=True)
    id_cad = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    nome = models.TextField(max_length=150)
    email = models.TextField(max_length=150)
    telefone = models.TextField(max_length=150)

