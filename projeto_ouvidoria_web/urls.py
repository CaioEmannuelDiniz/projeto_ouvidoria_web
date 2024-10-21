from django.urls import path # type: ignore
from ouvidoria_web import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    
    #GET ROTA INDEX
    path('',views.home,name='home'),
    
    #DENUNCIAR
    #POST ROTA CADASTRAR DENUNCIA
    path('cadastrar/denuncia/',views.send_denuncia,name='cadastrar_denuncia'),
    #POST ROTA ALTERAR DENUNCIA
    path('denuncia/alterar/<int:id>/',views.alter_denuncia,name='alterar_denuncia'),
    #GET ROTA FORMULARIO DENUNCIA
    path('formulario/denuncia/',views.form_denuncia,name='formulario_denuncia'),
    #GET ALL ROTA MOSTRAR DENUNCIAS
    path('denuncias/',views.show_denuncias,name='mostrar_denuncias'),
    #GET ROTA MOSTRA DENUNCIA
    path('denuncia/<int:id>/',views.show_denuncia,name='mostrar_denuncia'),
    #DELETE ROTA DELETAR DENUNCIA
    path('denuncia/deletar/<int:id>/',views.delete_denuncia,name='deletar_denuncia'),
    
    
    #RECLAMAÇÃO
    #POST ROTA CADASTRAR RECLAMAÇÃO
    path('cadastrar/reclamacao/',views.send_reclamacao,name='cadastrar_reclamacao'),
    #POST ROTA ALTERAR RECLAMAÇÃO
    path('reclamacao/alterar/<int:id>/',views.alter_reclamacao,name='alterar_reclamacao'),
    #GET ROTA FORMULARIO RECLAMAÇÃO
    path('formulario/reclamacao/',views.form_reclamacao,name='formulario_reclamacao'),
    #GET ALL ROTA MOSTRAR RECLAMAÇÕES
    path('reclamacoes/',views.show_reclamacoes,name='mostrar_reclamacoes'),
    #GET ROTA MOSTRA RECLAMACAO
    path('reclamacao/<int:id>/',views.show_reclamacao,name='mostrar_reclamacao'),
    #DELETE ROTA DELETAR RECLAMACAO
    path('reclamacao/deletar/<int:id>/',views.delete_reclamacao,name='deletar_reclamacao'),
    
    
    #SUGESTÃO
    #POST ROTA CADASTRAR SUGESTÃO
    path('cadastrar/sugestao/',views.send_sugestao,name='cadastrar_sugestao'),
    #POST ROTA ALTERAR SUGESTÃO
    path('sugestao/alterar/<int:id>/',views.alter_sugestao,name='alterar_sugestao'),
    #GET ROTA FORMULARIO SUGESTÃO
    path('formulario/sugestao/',views.form_sugestao,name='formulario_sugestao'),
    #GET ALL ROTA MOSTRAR SUGESTÃO
    path('sugestoes/',views.show_sugestoes,name='mostrar_sugestoes'),
    #GET ROTA MOSTRA SUGESTÃO
    path('sugestao/<int:id>/',views.show_sugestao,name='mostrar_sugestao'),
    #DELETE ROTA DELETAR SUGESTÃO
    path('sugestao/deletar/<int:id>/',views.delete_sugestao,name='deletar_sugestao'),
    
    
    
    
    #ELOGIO
    #POST ROTA CADASTRAR ELOGIO
    path('cadastrar/elogio/',views.send_elogio,name='cadastrar_elogio'),
    #POST ROTA ALTERAR ELOGIO
    path('elogio/alterar/<int:id>/',views.alter_elogio,name='alterar_elogio'),
    #GET ROTA FORMULARIO ELOGIO
    path('formulario/elogio/',views.form_elogio,name='formulario_elogio'),
    #GET ALL ROTA MOSTRAR ELOGIO
    path('elogios/',views.show_elogios,name='mostrar_elogio'),
    #GET ROTA MOSTRA ELOGIO
    path('elogio/<int:id>/',views.show_elogio,name='mostrar_elogio'),
    #DELETE ROTA DELETAR ELOGIO
    path('elogio/deletar/<int:id>/',views.delete_elogio,name='deletar_elogio'),
    
    
    #ACESSAR INFO
    #GET ROTA LOCALIZA INFO
    path('localiza/info/',views.find_localiza_info,name='localiza_info'),
    #GET ROTA MOSTRAR INFO
    path('formulario/localiza/info/',views.show_localiza_info,name='show_info'),
]
