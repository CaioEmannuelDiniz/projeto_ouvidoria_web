from django.shortcuts import render,redirect #type:ignore
from .models import Denuncia
from .models import Reclamacao
from .models import Elogio
from .models import Sugestao


# --- PAGINAÇÃO ---
#GET PAGINA INDEX (OK)
def home(request):
    return render(request,"home/index.html")



# -- SUGESTÃO --
#POST PAGINA FOMULARIO SUGESTÃO (OK)(OK)
def send_sugestao(request):
    nome = request.POST.get('name')
    email = request.POST.get('email')
    descricao = request.POST.get('description')
    
    dict = {
        'condicao': True,
        'tipo': 'error',
        'mensagem': 'Sugestão já registrada!',
    }
    
    if Sugestao.objects.filter(nome_completo = nome, email = email, descricao = descricao).exists():
        return render(request, 'forms/formulario_sugestao.html',{'dict':dict})
        
    nova_sugestao = Sugestao()
    nova_sugestao.nome_completo = request.POST.get('name')
    nova_sugestao.email = request.POST.get('email')
    nova_sugestao.telefone = request.POST.get('phone')
    nova_sugestao.descricao = request.POST.get('description')
    nova_sugestao.comentario = request.POST.get('comments')
    nova_sugestao.save()
    
    dict['tipo'] = 'sucess'
    dict['mensagem'] = 'Sugestão registrada com sucesso!'

    return render(request, 'forms/formulario_sugestao.html',{'dict':dict})

#GET PAGINA FORMULARIO SUGESTÃO (OK)(OK)
def form_sugestao(request):
    dict = {
        'condicao': False,
    }
    return render(request,'forms/formulario_sugestao.html',{'dict':dict})




# -- ELOGIO -- 
#POST PAGINA FORMILARIO ELOGIO (OK)(OK)
def send_elogio(request):
    nome = request.POST.get('name')
    email = request.POST.get('email')
    descricao = request.POST.get('description')
    
    dict = {
        'condicao': True,
        'tipo': 'error',
        'mensagem': 'Elogio já registrada!',
    }
    
    if Elogio.objects.filter(nome_completo = nome, email = email, descricao = descricao).exists():
        return render(request, 'forms/formulario_elogio.html',{'dict':dict})
        
    novo_elogio = Elogio()
    novo_elogio.nome_completo = request.POST.get('name')
    novo_elogio.email = request.POST.get('email')
    novo_elogio.telefone = request.POST.get('phone')
    novo_elogio.classificacao_satisfacao = request.POST.get('satisfactionSelected')
    novo_elogio.descricao = request.POST.get('description')
    novo_elogio.comentario = request.POST.get('comments')
    novo_elogio.save()

    dict['tipo'] = 'sucess'
    dict['mensagem'] = 'Elogio registrada com sucesso!'

    return  render(request, 'forms/formulario_elogio.html',{'dict':dict})

#GET PAGINA FORMULARIO ELOGIO (OK)(OK)
def form_elogio(request):
    dict = {
        'condicao': False,
    }
    return render(request,'forms/formulario_elogio.html',{'dict':dict})




# --- DENUNCIA --- 
#POST PAGINA FORMULARIO DENUNCIA (OK)(OK)
def send_denuncia(request):
    
    nome = request.POST.get('name')
    email = request.POST.get('email')
    descricao = request.POST.get('description')
    dict = {
                'condicao': True,
                'tipo': 'error',
                'mensagem': 'Denúncia já registrada!',
            }
    
    if Denuncia.objects.filter(nome_completo = nome, email = email, descricao = descricao).exists():
        return render(request, 'forms/formulario_denuncia.html', {'dict':dict})
    
  
    nova_denuncia = Denuncia()
    nova_denuncia.nome_completo = request.POST.get('name')
    nova_denuncia.email = request.POST.get('email')
    nova_denuncia.telefone = request.POST.get('phone')
    nova_denuncia.tipo_denuncia = request.POST.get('type')
    nova_denuncia.arquivo = request.POST.get('evidence')
    nova_denuncia.descricao = request.POST.get('description')
    nova_denuncia.preferencia_contato = request.POST.get('contact-preference')
    nova_denuncia.comentario = request.POST.get('comments')
    nova_denuncia.save()

    dict['tipo'] = 'sucess'
    dict['mensagem'] = 'Denúncia registrada com sucesso!'

    return render(request,'forms/formulario_denuncia.html',{'dict':dict})

#GET PAGINA FORMULARIO DENUNCIA (OK)(OK)
def form_denuncia(request):
    dict = {
        'condicao': False,
    }
    return render(request,"forms/formulario_denuncia.html",{'dict':dict})

#GET PAGINA LISTA TODAS AS DENUNCIAS (OK)
def show_denuncias(request):
    
    denuncias ={
    'denuncias': Denuncia.objects.all()
    }
    
    return render(request,"tables/denuncias.html",denuncias)


# --- RECLAMAÇÃO ---
#POST PAGINA FORMULARIO RECLAMAÇÃO (OK)(OK)
def send_reclamacao(request):
     
    nome = request.POST.get('name')
    email = request.POST.get('email')
    descricao = request.POST.get('description')
    
    dict = {
        'condicao': True,
        'tipo': 'error',
        'mensagem': 'Reclamação já registrada!',
    }
    
    if Reclamacao.objects.filter(nome_completo = nome, email = email, descricao = descricao).exists():
        return render(request, 'forms/formulario_reclamacao.html',{'dict':dict})
    
  
    nova_reclamacao = Reclamacao()
    nova_reclamacao.nome_completo = request.POST.get('name')
    nova_reclamacao.email = request.POST.get('email')
    nova_reclamacao.telefone = request.POST.get('phone')
    nova_reclamacao.tipo_reclamacao = request.POST.get('type')
    nova_reclamacao.classificacao_insatisfacao = request.POST.get('dissatisfactionSelected')
    nova_reclamacao.descricao = request.POST.get('description')
    nova_reclamacao.preferencia_contato = request.POST.get('contact-preference')
    nova_reclamacao.comentario = request.POST.get('comments')
    nova_reclamacao.save()
    
    dict['tipo'] = 'sucess'
    dict['mensagem'] = 'Reclamação registrada com sucesso!'

    return render(request, 'forms/formulario_reclamacao.html',{'dict':dict})

#GET PAGINA FORMULARIO RECLAMAÇÃO (OK)(OK)
def form_reclamacao(request):
    dict = {
        'condicao': False,
    }
    return render(request,'forms/formulario_reclamacao.html',{'dict':dict})




# --- ACESSO INFO --
#GET PAGINA ACESSO A INFO LOCALIZAR
def find_localiza_info(request):
    nome = request.POST.get('name')
    email = request.POST.get('email')
    telefone = request.POST.get('phone')
    tipo  = request.POST.get('type')
    
    if(tipo == 'denuncia'):
        
        denuncia = Denuncia.objects.filter(nome_completo = nome, email = email, telefone = telefone)
        
        if denuncia.exists():
            {'denuncia':denuncia}
            print(denuncia)
            
        print('models')
    elif(tipo == 'reclamacao'):
        reclamacao = Reclamacao.objects.filter(nome_completo = nome, email = email, telefone = telefone)
        
        if reclamacao.exists():
            {'reclamacao':reclamacao}
            print(reclamacao)
            
    elif(tipo == 'elogio'):
        elogio = Elogio.objects.filter(nome_completo = nome, email = email, telefone = telefone)
        
        if elogio.exists():
            {'elogio':elogio}
            print(elogio)
            
    elif(tipo == 'sugestao'):
        sugestao = Sugestao.objects.filter(nome_completo = nome, email = email, telefone = telefone)
        
        if sugestao.exists():
            {'sugestao':sugestao}
            print(sugestao)
            
    return render(request,'home/index.html')
    
#GET PAGINA ACESSO A INFO (OK)
def show_localiza_info(request):
    return render(request,'info/localiza_info.html')
