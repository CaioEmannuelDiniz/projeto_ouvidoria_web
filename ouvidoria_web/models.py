from django.db import models #type:ignore


class Denuncia(models.Model):
    id = models.AutoField(primary_key = True)
    nome_completo = models.TextField(max_length = 255)
    email = models.EmailField(max_length = 254)
    telefone = models.TextField(max_length = 15)
    tipo_denuncia = models.TextField(max_length = 20)
    arquivo = models.FileField(upload_to = 'documentos/denuncia', null = True,blank = True)
    descricao = models.TextField()
    preferencia_contato = models.TextField(max_length = 20)
    comentario = models.TextField( null = True,blank = True)    
    
class Reclamacao(models.Model):
    id = models.AutoField(primary_key = True)
    nome_completo = models.TextField(max_length = 255)
    email = models.EmailField(max_length = 254)
    telefone = models.TextField(max_length = 15)
    tipo_reclamacao = models.TextField(max_length = 20)
    classificacao_insatisfacao = models.IntegerField()
    descricao = models.TextField()
    preferencia_contato = models.TextField(max_length = 20)
    comentario = models.TextField( null = True,blank = True)  
    
class Elogio(models.Model):
    id = models.AutoField(primary_key = True)
    nome_completo = models.TextField(max_length = 255)
    email = models.EmailField(max_length = 254)
    telefone = models.TextField(max_length = 15)
    classificacao_satisfacao = models.IntegerField()
    descricao = models.TextField()
    comentario = models.TextField( null = True,blank = True)  

class Sugestao(models.Model):
    id = models.AutoField(primary_key = True)
    nome_completo = models.TextField(max_length = 255)
    email = models.EmailField(max_length = 254)
    telefone = models.TextField(max_length = 15)
    descricao = models.TextField()
    comentario = models.TextField( null = True,blank = True)  
    