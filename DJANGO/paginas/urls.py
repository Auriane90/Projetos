from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastroResp/', views.cadastroResp, name='cadastroResp'),
    path('cadastroSupResp/', views.auxResp, name='cadastroResps'),
    path('cdHorario/', views.add_horario, name='cdHorario'),
    path('cdDados/', views.add_dados, name='cdDados'),
    path('cdConteudo/', views.add_conteudo, name='cdConteudo'),
    path('cdAdvertencia/', views.add_advertencia, name='cdAdvertencia'),
    path('cdFrequencia/', views.add_frequencia, name='cdFrequencia'),
    path('cdNotas/', views.add_notas, name='cdNotas'),
    path('login/', views.do_login, name='login'),
    path('logout/', views.do_logout, name='logout'),
    
    path('', views.inicio, name='inicio'),
    path('inicioResp', views.inicioResp, name='inicioResp'),
    path('frequencia/', views.chamada, name='frequencia'),
    path('notas/', views.nota, name='notas'),
    path('revisao/', views.revisao, name='revisao'),
    path('advertencia/', views.advertencias, name='advertencia'),
    path('dados/', views.dados, name='dados'),

    path('frequenciaResp/', views.chamadaResp, name='frequenciaResp'),
    path('notasResp/', views.notaResp, name='notasResp'),
    path('advertenciaResp/', views.advertenciasResp, name='advertenciaResp'),
    path('dadosResp/', views.dadosResp, name='dadosResp'),
    path('inicioSupResp/', views.inicioRespSurp, name='inicioSupResp'),
    path('adverSupResp/', views.adverRespSurp, name='adverSupResp'),
    path('chamadaSupResp/', views.chamadaRespSurp, name='chamadaSupResp'),
    path('dadosSupResp/', views.dadosRespSurp, name='dadosSupResp'),
    path('notasSupResp/', views.notasRespSurp, name='notasSupResp'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
