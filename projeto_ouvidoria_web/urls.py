from django.urls import path # type: ignore
from ouvidoria_web import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    
    #GET ROTA INDEX
    path('',views.home,name='home'),
    
    #DENUNCIAR
    #POST ROTA CADASTRAR DENUNCIA
    path('cadastrar/denuncia/',views.send_denuncia,name='cadastrar_denuncia'),
    #GET ROTA FORMULARIO DENUNCIA
    path('formulario/denuncia/',views.form_denuncia,name='formulario_denuncia'),
    #GET ROTA MOSTRAR DENUNCIA
    path('denuncias/',views.show_denuncias,name='mostrar_denuncias'),
    #POST ROTA ALTERAR DENUNCIA
    path('denuncia/<int:id>/',views.show_denuncia,name='alterar_denuncia'),
    #DELETE ROTA DELETAR DENUNCIA
    path('denuncia/deletar/<int:id>/',views.delete_denuncia,name='deletar_denuncia'),
    
    
    #RECLAMAÇÃO
    #POST ROTA CADASTRAR RECLAMAÇÃO
    path('cadastrar/reclamacao/',views.send_reclamacao,name='cadastrar_reclamacao'),
    #GET ROTA FORMULARIO RECLAMAÇÃO
    path('formulario/reclamacao/',views.form_reclamacao,name='formulario_reclamacao'),
    
    
    #SUGESTÃO
    #POST ROTA CADASTRAR SUGESTÃO
    path('cadastrar/sugestao/',views.send_sugestao,name='cadastrar_sugestao'),
    #GET ROTA FORMULARIO SUGESTÃO
    path('formulario/sugestao/',views.form_sugestao,name='formulario_sugestao'),
    
    
    #ELOGIO
    #POST ROTA CADASTRAR ELOGIO
    path('cadastrar/elogio/',views.send_elogio,name='cadastrar_elogio'),
    #GET ROTA FORMULARIO ELOGIO
    path('formulario/elogio/',views.form_elogio,name='formulario_elogio'),
    
    
    #ACESSAR INFO
    #GET ROTA LOCALIZA INFO
    path('localiza/info/',views.find_localiza_info,name='localiza_info'),
    #GET ROTA MOSTRAR INFO
    path('formulario/localiza/info/',views.show_localiza_info,name='show_info'),
]
