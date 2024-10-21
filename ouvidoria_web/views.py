from django.shortcuts import render,redirect,get_object_or_404 #type:ignore
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

#POST PAGINA ALTERAR SUGESTÃO (OK)
def alter_sugestao(request, id):
    sugestao = get_object_or_404(Sugestao, id=id)
    
    print(sugestao)

    # Verifica se é uma requisição POST
    if request.method == 'POST':
        
        sugestao.feedback = request.POST.get('feedback')
        print(request.POST.get('feedback'))
        print(sugestao.feedback)
        sugestao.status = request.POST.get('status')
        print(request.POST.get('status'))
        print(sugestao.status)

        dict = {
            'condicao': True,
            'tipo': 'error',
            'mensagem': 'Sugestão não foi alterada!',
        }

        # Salva o elogio e atualiza a mensagem
        try:
            sugestao.save()
            dict['tipo'] = 'sucess'
            dict['mensagem'] = 'Sugestão alterada com sucesso!'
        except Exception:
            # Lidar com possíveis erros de salvamento
            dict['mensagem'] = 'Sugestão não foi alterada!'

    # Busca todas os elogios
    sugestoes = Sugestao.objects.all()

    return render(request, 'tables/sugestoes.html', {'dict': dict, 'sugestoes': sugestoes})

#GET PAGINA FORMULARIO SUGESTÃO (OK)(OK)
def form_sugestao(request):
    dict = {
        'condicao': False,
    }
    return render(request,'forms/formulario_sugestao.html',{'dict':dict})

#GET PAGINA LISTA TODOS SUGESTÃO (OK)
def show_sugestoes(request):
       
    sugestoes ={
    'sugestoes': Sugestao.objects.all()
    }
    
    return render(request,"tables/sugestoes.html",sugestoes)

#GET PAGINA DE ALTERAR UM SUGESTÃO (OK)
def show_sugestao(request,id):
    sugestao = get_object_or_404(Sugestao, id = id)

    return render(request,"forms/formulario_sugestao.html",{'sugestao': sugestao})

#DELETE PAGINA DELETAR UM SUGESTÃO (OK)
def delete_sugestao(request,id):
    sugestao = get_object_or_404(Sugestao, id = id)
    
    dict = {
                'condicao': True,
                'tipo': 'error',
                'mensagem': 'Sugestão não foi excluida!',
            }
    
    
    try:
        sugestao.delete()
        dict['tipo'] = 'sucess'
        dict['mensagem'] = 'Sugestão excluida com sucesso!'
    except Exception:
        dict['mensagem'] = 'Sugestão não foi excluida!'
    
    
    return render(request,"tables/sugestoes.html",{'dict':dict,'sugestoes': Sugestao.objects.all()})



# -- ELOGIO -- 
#POST PAGINA FORMILARIO ELOGIO (OK)(OK)
def send_elogio(request):
    nome = request.POST.get('name')
    email = request.POST.get('email')
    descricao = request.POST.get('description')
    
    dict = {
        'condicao': True,
        'tipo': 'error',
        'mensagem': 'Elogio já registrado!',
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
    dict['mensagem'] = 'Elogio registrado com sucesso!'

    return  render(request, 'forms/formulario_elogio.html',{'dict':dict})

#POST PAGINA ALTERAR ELOGIO (OK)(OK)
def alter_elogio(request, id):
    elogio = get_object_or_404(Elogio, id=id)
    
    print(elogio)

    # Verifica se é uma requisição POST
    if request.method == 'POST':
        
        elogio.feedback = request.POST.get('feedback')
        print(request.POST.get('feedback'))
        print(elogio.feedback)
        elogio.status = request.POST.get('status')
        print(request.POST.get('status'))
        print(elogio.status)

        dict = {
            'condicao': True,
            'tipo': 'error',
            'mensagem': 'Elogio não foi alterado!',
        }

        # Salva o elogio e atualiza a mensagem
        try:
            elogio.save()
            dict['tipo'] = 'sucess'
            dict['mensagem'] = 'Elogio alterado com sucesso!'
        except Exception:
            # Lidar com possíveis erros de salvamento
            dict['mensagem'] = 'Elogio não foi alterado!'

    # Busca todas os elogios
    elogios = Elogio.objects.all()

    return render(request, 'tables/elogios.html', {'dict': dict, 'elogios': elogios})

#GET PAGINA FORMULARIO ELOGIO (OK)(OK)
def form_elogio(request):
    dict = {
        'condicao': False,
    }
    return render(request,'forms/formulario_elogio.html',{'dict':dict})

#GET PAGINA LISTA TODOS ELOGIOS (OK)(OK)
def show_elogios(request):
       
    elogios ={
    'elogios': Elogio.objects.all()
    }
    
    return render(request,"tables/elogios.html",elogios)

#GET PAGINA DE ALTERAR UM ELOGIO (OK)(OK)
def show_elogio(request,id):
    elogio = get_object_or_404(Elogio, id = id)

    return render(request,"forms/formulario_elogio.html",{'elogio': elogio})

#DELETE PAGINA DELETAR UM ELOGIO (OK)(OK)
def delete_elogio(request,id):
    elogio = get_object_or_404(Elogio, id = id)
    
    dict = {
                'condicao': True,
                'tipo': 'error',
                'mensagem': 'Elogio não foi excluido!',
            }
    
    
    try:
        elogio.delete()
        dict['tipo'] = 'sucess'
        dict['mensagem'] = 'Elogio excluido com sucesso!'
    except Exception:
        dict['mensagem'] = 'Elogio não foi excluido!'
    
    
    return render(request,"tables/elogios.html",{'dict':dict,'elogios': Elogio.objects.all()})




# --- DENUNCIA --- 
#POST PAGINA CADASTRAR DENUNCIA (OK)(OK)
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

#POST PAGINA ALTERAR DENUNCIA (OK)(OK)
def alter_denuncia(request, id):
    denuncia = get_object_or_404(Denuncia, id=id)
    
    print(denuncia)

    # Verifica se é uma requisição POST
    if request.method == 'POST':
        
        denuncia.feedback = request.POST.get('feedback')
        print(request.POST.get('feedback'))
        print(denuncia.feedback)
        denuncia.status = request.POST.get('status')
        print(request.POST.get('status'))
        print(denuncia.status)

        dict = {
            'condicao': True,
            'tipo': 'error',
            'mensagem': 'Denúncia não foi alterada!',
        }

        # Salva a denúncia e atualiza a mensagem
        try:
            denuncia.save()
            dict['tipo'] = 'sucess'
            dict['mensagem'] = 'Denúncia alterada com sucesso!'
        except Exception:
            # Lidar com possíveis erros de salvamento
            dict['mensagem'] = 'Denúncia não foi alterada!'

    # Busca todas as denúncias
    denuncias = Denuncia.objects.all()

    return render(request, 'tables/denuncias.html', {'dict': dict, 'denuncias': denuncias})

#GET PAGINA FORMULARIO DENUNCIA (OK)(OK)
def form_denuncia(request):
    dict = {
        'condicao': False,
    }
    
    return render(request,"forms/formulario_denuncia.html",{'dict':dict})

#GET PAGINA LISTA TODAS AS DENUNCIAS (OK)(OK)
def show_denuncias(request):
    
    denuncias ={
    'denuncias': Denuncia.objects.all()
    }
    
    return render(request,"tables/denuncias.html",denuncias)

#GET PAGINA DE ALTERAR UMA DENUNCIA (OK)(OK)
def show_denuncia(request,id):
    denuncia = get_object_or_404(Denuncia, id = id)

    return render(request,"forms/formulario_denuncia.html",{'denuncia': denuncia})

#DELETE PAGINA DELETAR UMA DENUNCIA (OK)(OK)
def delete_denuncia(request,id):
    denuncia = get_object_or_404(Denuncia, id = id)
    
    dict = {
                'condicao': True,
                'tipo': 'error',
                'mensagem': 'Denúncia não foi excluida!',
            }
    
    
    try:
        denuncia.delete()
        dict['tipo'] = 'sucess'
        dict['mensagem'] = 'Denúncia excluida com sucesso!'
    except Exception:
        dict['mensagem'] = 'Denúncia não foi excluida!'
    
    
    return render(request,"tables/denuncias.html",{'dict':dict,'denuncias': Denuncia.objects.all()})




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

#POST PAGINA ALTERAR RECLAMAÇÃO (OK)(OK)
def alter_reclamacao(request,id):
    reclamacao = get_object_or_404(Reclamacao, id=id)
    
    print(reclamacao)

    # Verifica se é uma requisição POST
    if request.method == 'POST':
        
        reclamacao.feedback = request.POST.get('feedback')
        print(request.POST.get('feedback'))
        print(reclamacao.feedback)
        reclamacao.status = request.POST.get('status')
        print(request.POST.get('status'))
        print(reclamacao.status)

        dict = {
            'condicao': True,
            'tipo': 'error',
            'mensagem': 'Reclamação não foi alterada!',
        }

        # Salva a reclamação e atualiza a mensagem
        try:
            reclamacao.save()
            dict['tipo'] = 'sucess'
            dict['mensagem'] = 'Reclamação alterada com sucesso!'
        except Exception:
            # Lidar com possíveis erros de salvamento
            dict['mensagem'] = 'Reclamação não foi alterada!'

    # Busca todas as reclamação
    reclamacoes = Reclamacao.objects.all()

    return render(request, 'tables/reclamacoes.html', {'dict': dict, 'reclamacoes': reclamacoes})

#GET PAGINA FORMULARIO RECLAMAÇÃO (OK)(OK)
def form_reclamacao(request):
    dict = {
        'condicao': False,
    }
    return render(request,'forms/formulario_reclamacao.html',{'dict':dict})

#GET PAGINA LISTA TODAS AS RECLAMAÇÕES (OK)
def show_reclamacoes(request):
    reclamacoes = {
        'reclamacoes':Reclamacao.objects.all()
    }
    
    return render(request,"tables/reclamacoes.html",reclamacoes)

#GET PAGINA DE ALTERAR UMA RECLAMAÇÃO (OK)(OK)
def show_reclamacao(request,id):
    reclamacao = get_object_or_404(Reclamacao, id = id)

    return render(request,"forms/formulario_reclamacao.html",{'reclamacao': reclamacao})

#DELETE PAGINA DELETAR UMA RECLAMAÇÃO (OK)(OK)
def delete_reclamacao(request,id):
    reclamacao = get_object_or_404(Reclamacao, id = id)
    
    dict = {
                'condicao': True,
                'tipo': 'error',
                'mensagem': 'Reclamação não foi excluida!',
            }
    
    
    try:
        reclamacao.delete()
        dict['tipo'] = 'sucess'
        dict['mensagem'] = 'Reclamação excluida com sucesso!'
    except Exception:
        dict['mensagem'] = 'Reclamação não foi excluida!'
    
    
    return render(request,"tables/reclamacoes.html",{'dict':dict,'reclamacoes': Reclamacao.objects.all()})       


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
