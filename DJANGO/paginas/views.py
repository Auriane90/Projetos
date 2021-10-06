from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

from .models import Horario, Notas, Advertencia, Frequencia, Conteudo, DadosPessoais, Resp, RespSuper
from .forms import UserHorario, UserAdvertencia, UserFrequencia, UserNotas, UserConteudo, UserDados,\
    CdAluno, CdResp, AuxResp


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from pylab import *
from io import BytesIO
import base64
import matplotlib.pyplot as plt


# Pagina do Aluno
@login_required
def inicio(request):
    print(usuario_logado)
    horarios = Horario.objects.filter(turma=Turma)
    user = DadosPessoais.objects.filter(idAluno=usuario_logado)
    username = User.objects.filter(id=usuario_logado)
    return render(request, "paginas/Aluno/home.html", {'horarios': horarios, 'user': user, 'username': username})


@login_required
def chamada(request):
    frequencia = Frequencia.objects.filter(idAluno=usuario_logado)
    user = DadosPessoais.objects.filter(idAluno=usuario_logado)
    username = User.objects.filter(id=usuario_logado)
    return render(request, "paginas/Aluno/chamada.html", {"chamadas": frequencia, 'user': user, 'username': username})


@login_required
def nota(request):
    x = ['Port', 'Mat', 'His', 'Fil', 'Bio', 'Geo', 'Fis', 'Esp',
        'Ing', 'Qui', 'Soc', 'E.Fis']
    y = []
    notas = Notas.objects.filter(idAluno=usuario_logado)
    nota_pb = 0
    nota_mt = 0
    nota_hi = 0
    nota_edf = 0
    nota_bi = 0
    nota_fi = 0
    nota_geo = 0
    nota_fis = 0
    nota_es = 0
    nota_in = 0
    nota_qui = 0
    nota_so = 0

    for no in notas:
        if no.SBPortuques is None and no.SBMatematica is None and no.SBHistoria is None and no.SBBiologia is None and no.SBFilosofia is None and no.SBGeografia is None and no.SBFisica is None and no.SBEspanhol is None and no.SBIngles is None and no.SBQuimica is None \
                and no.SBSociologia is None and no.SBEdFisica is None and no.TBPortuques is None and no.TBMatematica is None and no.TBHistoria is None and no.TBBiologia is None and no.TBFilosofia is None and no.TBGeografia is None and no.TBFisica is None and no.TBEspanhol is None and no.TBIngles is None and no.TBQuimica is None \
                and no.TBSociologia is None and no.TBEdFisica is None and no.QBPortuques is None and no.QBMatematica is None and \
                no.QBHistoria is None and no.QBBiologia is None and no.QBFilosofia is None and no.QBGeografia is None and no.QBFisica is None and no.QBEspanhol is None and no.QBIngles is None and no.QBQuimica is None and no.QBSociologia is None and no.QBEdFisica is None:
            nota_pb = no.PBPortuques
            nota_mt = no.PBMatematica
            nota_hi = no.PBHistoria
            nota_bi = no.PBBiologia
            nota_fi = no.PBFilosofia
            nota_geo = no.PBGeografia
            nota_fis = no.PBFisica
            nota_es = no.PBEspanhol
            nota_in = no.PBIngles
            nota_qui = no.PBQuimica
            nota_so = no.PBSociologia
            nota_edf = no.PBEdFisica
        elif no.TBPortuques is None and no.TBMatematica is None and no.TBHistoria is None and no.TBBiologia is None and no.TBFilosofia is None \
                    and no.TBGeografia is None and no.TBFisica is None and no.TBEspanhol is None and no.TBIngles is None and no.TBQuimica is None \
                    and no.TBSociologia is None and no.TBEdFisica is None and no.QBPortuques is None and no.QBMatematica is None and no.QBHistoria is None and no.QBBiologia is None and no.QBFilosofia is None \
                    and no.QBGeografia is None and no.QBFisica is None and no.QBEspanhol is None and no.QBIngles is None and no.QBQuimica is None \
                    and no.QBSociologia is None and no.QBEdFisica is None:
                nota_pb = ((no.PBPortuques + no.SBPortuques) / 2)
                nota_mt = ((no.PBMatematica + no.SBMatematica) / 2)
                nota_hi = ((no.PBHistoria + no.SBHistoria) / 2)
                nota_bi = ((no.PBBiologia + no.SBBiologia) / 2)
                nota_fi = ((no.PBFilosofia + no.SBFilosofia) / 2)
                nota_geo = ((no.PBGeografia + no.SBGeografia) / 2)
                nota_fis = ((no.PBFisica + no.SBFisica) / 2)
                nota_es = ((no.PBEspanhol + no.SBEspanhol) / 2)
                nota_in = ((no.PBIngles + no.SBIngles) / 2)
                nota_qui = ((no.PBQuimica + no.SBQuimica) / 2)
                nota_so = ((no.PBSociologia + no.SBSociologia) / 2)
                nota_edf = ((no.PBEdFisica + no.SBEdFisica) / 2)
        elif no.QBPortuques is None and no.QBMatematica is None and no.QBHistoria is None and no.QBBiologia is None and no.QBFilosofia is None \
                    and no.QBGeografia is None and no.QBFisica is None and no.QBEspanhol is None and no.QBIngles is None and no.QBQuimica is None \
                    and no.QBSociologia is None and no.QBEdFisica is None:
                nota_pb = ((no.PBPortuques + no.SBPortuques + no.TBPortuques) / 3)
                nota_mt = ((no.PBMatematica + no.SBMatematica + no.TBMatematica) / 3)
                nota_hi = ((no.PBHistoria + no.SBHistoria + no.TBHistoria) / 3)
                nota_bi = ((no.PBBiologia + no.SBBiologia + no.TBBiologia) / 3)
                nota_fi = ((no.PBFilosofia + no.SBFilosofia + no.TBFilosofia) / 3)
                nota_geo = ((no.PBGeografia + no.SBGeografia + no.TBGeografia) / 3)
                nota_fis = ((no.PBFisica + no.SBFisica + no.TBFisica) / 3)
                nota_es = ((no.PBEspanhol + no.SBEspanhol + no.TBEspanhol) / 3)
                nota_in = ((no.PBIngles + no.SBIngles + no.TBIngles) / 3)
                nota_qui = ((no.PBQuimica + no.SBQuimica + no.TBQuimica) / 3)
                nota_so = ((no.PBSociologia + no.SBSociologia + no.TBSociologia) / 3)
                nota_edf = ((no.PBEdFisica + no.SBEdFisica + no.TBEdFisica) / 3)
        else:
                nota_pb = ((no.PBPortuques + no.SBPortuques + no.TBPortuques + no.QBPortuques) / 4)
                nota_mt = ((no.PBMatematica + no.SBMatematica + no.TBMatematica + no.QBMatematica) / 4)
                nota_hi = ((no.PBHistoria + no.SBHistoria + no.TBHistoria + no.QBHistoria) / 4)
                nota_bi = ((no.PBBiologia + no.SBBiologia + no.TBBiologia + no.QBBiologia) / 4)
                nota_fi = ((no.PBFilosofia + no.SBFilosofia + no.TBFilosofia + no.QBFilosofia) / 4)
                nota_geo = ((no.PBGeografia + no.SBGeografia + no.TBGeografia + no.QBGeografia) / 4)
                nota_fis = ((no.PBFisica + no.SBFisica + no.TBFisica + no.QBFisica) / 4)
                nota_es = ((no.PBEspanhol + no.SBEspanhol + no.TBEspanhol + no.QBEspanhol) / 4)
                nota_in = ((no.PBIngles + no.SBIngles + no.TBIngles + no.QBIngles) / 4)
                nota_qui = ((no.PBQuimica + no.SBQuimica + no.TBQuimica + no.QBQuimica) / 4)
                nota_so = ((no.PBSociologia + no.SBSociologia + no.TBSociologia + no.QBSociologia) / 4)
                nota_edf = ((no.PBEdFisica + no.SBEdFisica + no.TBEdFisica + no.QBEdFisica) / 4)

    y = [nota_pb, nota_mt, nota_hi, nota_fi, nota_bi, nota_geo, nota_fis, nota_es,
             nota_in, nota_qui, nota_so, nota_edf]

    plt.bar(x, y, label='Barras', color='blue')

    xlabel('Disciplinas', color='black')
    ylabel('Notas', color='black')
    title('Gráfico De Notas')
    subplots_adjust(left=0.21)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    gf = base64.b64encode(image_png)
    gf = gf.decode('utf-8')

    user = DadosPessoais.objects.filter(idAluno=usuario_logado)
    username = User.objects.filter(id=usuario_logado)

    return render(request, "paginas/Aluno/notas.html", {"notas": notas, 'gf': gf, 'user': user, 'username': username})


@login_required
def revisao(request):
    user = DadosPessoais.objects.filter(idAluno=usuario_logado)
    username = User.objects.filter(id=usuario_logado)
    revisoes = Conteudo.objects.filter(turma=Turma)
    return render(request, "paginas/Aluno/revisao.html", {"conteudo": revisoes,'user': user, 'username': username})


@login_required
def advertencias(request):
    user = DadosPessoais.objects.filter(idAluno=usuario_logado)
    username = User.objects.filter(id=usuario_logado)
    advertencia = Advertencia.objects.filter(idAluno=usuario_logado)
    return render(request, "paginas/Aluno/advertencias.html", {"advertecia": advertencia, 'user': user, 'username': username})


@login_required
def dados(request):
    user = DadosPessoais.objects.filter(idAluno=usuario_logado)
    username = User.objects.filter(id=usuario_logado)
    dado = DadosPessoais.objects.filter(idAluno=usuario_logado)
    return render(request, "paginas/Aluno/dadospessoais.html", {"dados": dado,'user': user, 'username': username})


# Login e logout
def do_login(request):
    global usuario_logado, Turma, usuario_logado_Resp, usuario_logado_Resp2
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.last_name == 'aluno':
                usuario_logado = user.id
                Turma = user.first_name
                login(request, user)
                return redirect(inicio)
            elif user.last_name == 'supResp':
                usuario_logado_Resp2 = user.id
                login(request, user)
                return redirect(inicioRespSurp)
        else:
            resp = Resp.objects.filter(nome=request.POST['username'], senha=request.POST['password']).exists()
            if resp:
                global nome, senha
                resp2 = Resp.objects.filter(nome=request.POST['username'], senha=request.POST['password'])
                for dados in resp2:
                    nome = dados.nome_aluno
                    senha = dados.matricula_aluno
                user = authenticate(username=nome, password=senha)
                if user is not None:
                    usuario_logado_Resp = user.id
                    login(request, user)
                    return redirect(inicioResp)
                return HttpResponse("usuario Responsavel")

    return render(request, "paginas/login.html")


def do_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


# Cadastro de conteudos das paginas
def cadastro(request):
    form = CdAluno(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse("Usuario cadastrado")
    return render(request, "paginas/Cadastro/cadastro.html", {'form': form})


def add_conteudo(request):
    form = UserConteudo(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario cadastrado")
    return render(request, "paginas/Cadastro/cdConteudo.html", {'form': form})


def add_advertencia(request):
    alunos = User.objects.all()
    form = UserAdvertencia(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.turma = request.POST['turma']
            form.idAluno = request.POST['idAluno']
            form.save()
            return HttpResponse("Usuario cadastrado")
    return render(request, "paginas/Cadastro/cdAdivertencia.html", {'form': form, 'alunos': alunos})


def add_notas(request):
    alunos = User.objects.all()
    form = UserNotas(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.turma = request.POST['turma']
            form.idAluno = request.POST['idAluno']
            form.save()
            return HttpResponse("Usuario cadastrado")
    return render(request, "paginas/Cadastro/cdNotas.html", {'form': form, 'alunos': alunos})


def add_frequencia(request):
    alunos = User.objects.all()
    form = UserFrequencia(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.turma = request.POST['turma']
            form.idAluno = request.POST['idAluno']
            form.save()
            return HttpResponse("Usuario cadastrado")
    return render(request, "paginas/Cadastro/cdFrequencia.html", {'form': form, 'alunos': alunos})


def add_horario(request):
    form = UserHorario(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario cadastrado")
    return render(request, "paginas/Cadastro/cdHorario.html", {'form': form})


def add_dados(request):
    alunos = User.objects.all()
    form = UserDados(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.turma = request.POST['turma']
            form.idAluno = request.POST['idAluno']
            form.save()
            return HttpResponse("Usuario cadastrado")
    return render(request, "paginas/Cadastro/cdDados.html", {'form': form, 'alunos': alunos})


def cadastroResp(request):
    form = CdResp(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario cadastrado")
    return render(request, "paginas/Cadastro/cadastroResp.html", {'form': form})


def auxResp(request):
    alunos = User.objects.filter(last_name='supResp')
    form = AuxResp(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.id_resp = request.POST['id_resp']
            form.save()
            return HttpResponse("Usuario cadastrado")
    return render(request, "paginas/Cadastro/cdAuxResp.html", {'form': form, 'alunos': alunos})


# pagina dos responsaveis
@login_required
def inicioResp(request):
    user = DadosPessoais.objects.filter(idAluno=usuario_logado_Resp)
    username = User.objects.filter(id=usuario_logado_Resp)
    return render(request, "paginas/Responsaveis/homeR.html", {'user': user, 'username': username})


@login_required
def chamadaResp(request):
    frequencia = Frequencia.objects.filter(idAluno=usuario_logado_Resp)
    user = DadosPessoais.objects.filter(idAluno=usuario_logado_Resp)
    username = User.objects.filter(id=usuario_logado_Resp)
    return render(request, "paginas/Responsaveis/chamada.html", {"chamadas": frequencia, 'user': user, 'username': username})


@login_required
def notaResp(request):
    x = ['Port', 'Mat', 'His', 'Fil', 'Bio', 'Geo', 'Fis', 'Esp',
        'Ing', 'Qui', 'Soc', 'E.Fis']
    y = []
    notas = Notas.objects.filter(idAluno=usuario_logado_Resp)
    nota_pb = 0
    nota_mt = 0
    nota_hi = 0
    nota_edf = 0
    nota_bi = 0
    nota_fi = 0
    nota_geo = 0
    nota_fis = 0
    nota_es = 0
    nota_in = 0
    nota_qui = 0
    nota_so = 0

    for no in notas:
        if no.SBPortuques is None and no.SBMatematica is None and no.SBHistoria is None and no.SBBiologia is None and no.SBFilosofia is None and no.SBGeografia is None and no.SBFisica is None and no.SBEspanhol is None and no.SBIngles is None and no.SBQuimica is None \
                and no.SBSociologia is None and no.SBEdFisica is None and no.TBPortuques is None and no.TBMatematica is None and no.TBHistoria is None and no.TBBiologia is None and no.TBFilosofia is None and no.TBGeografia is None and no.TBFisica is None and no.TBEspanhol is None and no.TBIngles is None and no.TBQuimica is None \
                and no.TBSociologia is None and no.TBEdFisica is None and no.QBPortuques is None and no.QBMatematica is None and \
                no.QBHistoria is None and no.QBBiologia is None and no.QBFilosofia is None and no.QBGeografia is None and no.QBFisica is None and no.QBEspanhol is None and no.QBIngles is None and no.QBQuimica is None and no.QBSociologia is None and no.QBEdFisica is None:
            nota_pb = no.PBPortuques
            nota_mt = no.PBMatematica
            nota_hi = no.PBHistoria
            nota_bi = no.PBBiologia
            nota_fi = no.PBFilosofia
            nota_geo = no.PBGeografia
            nota_fis = no.PBFisica
            nota_es = no.PBEspanhol
            nota_in = no.PBIngles
            nota_qui = no.PBQuimica
            nota_so = no.PBSociologia
            nota_edf = no.PBEdFisica
        elif no.TBPortuques is None and no.TBMatematica is None and no.TBHistoria is None and no.TBBiologia is None and no.TBFilosofia is None \
                    and no.TBGeografia is None and no.TBFisica is None and no.TBEspanhol is None and no.TBIngles is None and no.TBQuimica is None \
                    and no.TBSociologia is None and no.TBEdFisica is None and no.QBPortuques is None and no.QBMatematica is None and no.QBHistoria is None and no.QBBiologia is None and no.QBFilosofia is None \
                    and no.QBGeografia is None and no.QBFisica is None and no.QBEspanhol is None and no.QBIngles is None and no.QBQuimica is None \
                    and no.QBSociologia is None and no.QBEdFisica is None:
                nota_pb = ((no.PBPortuques + no.SBPortuques) / 2)
                nota_mt = ((no.PBMatematica + no.SBMatematica) / 2)
                nota_hi = ((no.PBHistoria + no.SBHistoria) / 2)
                nota_bi = ((no.PBBiologia + no.SBBiologia) / 2)
                nota_fi = ((no.PBFilosofia + no.SBFilosofia) / 2)
                nota_geo = ((no.PBGeografia + no.SBGeografia) / 2)
                nota_fis = ((no.PBFisica + no.SBFisica) / 2)
                nota_es = ((no.PBEspanhol + no.SBEspanhol) / 2)
                nota_in = ((no.PBIngles + no.SBIngles) / 2)
                nota_qui = ((no.PBQuimica + no.SBQuimica) / 2)
                nota_so = ((no.PBSociologia + no.SBSociologia) / 2)
                nota_edf = ((no.PBEdFisica + no.SBEdFisica) / 2)
        elif no.QBPortuques is None and no.QBMatematica is None and no.QBHistoria is None and no.QBBiologia is None and no.QBFilosofia is None \
                    and no.QBGeografia is None and no.QBFisica is None and no.QBEspanhol is None and no.QBIngles is None and no.QBQuimica is None \
                    and no.QBSociologia is None and no.QBEdFisica is None:
                nota_pb = ((no.PBPortuques + no.SBPortuques + no.TBPortuques) / 3)
                nota_mt = ((no.PBMatematica + no.SBMatematica + no.TBMatematica) / 3)
                nota_hi = ((no.PBHistoria + no.SBHistoria + no.TBHistoria) / 3)
                nota_bi = ((no.PBBiologia + no.SBBiologia + no.TBBiologia) / 3)
                nota_fi = ((no.PBFilosofia + no.SBFilosofia + no.TBFilosofia) / 3)
                nota_geo = ((no.PBGeografia + no.SBGeografia + no.TBGeografia) / 3)
                nota_fis = ((no.PBFisica + no.SBFisica + no.TBFisica) / 3)
                nota_es = ((no.PBEspanhol + no.SBEspanhol + no.TBEspanhol) / 3)
                nota_in = ((no.PBIngles + no.SBIngles + no.TBIngles) / 3)
                nota_qui = ((no.PBQuimica + no.SBQuimica + no.TBQuimica) / 3)
                nota_so = ((no.PBSociologia + no.SBSociologia + no.TBSociologia) / 3)
                nota_edf = ((no.PBEdFisica + no.SBEdFisica + no.TBEdFisica) / 3)
        else:
                nota_pb = ((no.PBPortuques + no.SBPortuques + no.TBPortuques + no.QBPortuques) / 4)
                nota_mt = ((no.PBMatematica + no.SBMatematica + no.TBMatematica + no.QBMatematica) / 4)
                nota_hi = ((no.PBHistoria + no.SBHistoria + no.TBHistoria + no.QBHistoria) / 4)
                nota_bi = ((no.PBBiologia + no.SBBiologia + no.TBBiologia + no.QBBiologia) / 4)
                nota_fi = ((no.PBFilosofia + no.SBFilosofia + no.TBFilosofia + no.QBFilosofia) / 4)
                nota_geo = ((no.PBGeografia + no.SBGeografia + no.TBGeografia + no.QBGeografia) / 4)
                nota_fis = ((no.PBFisica + no.SBFisica + no.TBFisica + no.QBFisica) / 4)
                nota_es = ((no.PBEspanhol + no.SBEspanhol + no.TBEspanhol + no.QBEspanhol) / 4)
                nota_in = ((no.PBIngles + no.SBIngles + no.TBIngles + no.QBIngles) / 4)
                nota_qui = ((no.PBQuimica + no.SBQuimica + no.TBQuimica + no.QBQuimica) / 4)
                nota_so = ((no.PBSociologia + no.SBSociologia + no.TBSociologia + no.QBSociologia) / 4)
                nota_edf = ((no.PBEdFisica + no.SBEdFisica + no.TBEdFisica + no.QBEdFisica) / 4)

    y = [nota_pb, nota_mt, nota_hi, nota_fi, nota_bi, nota_geo, nota_fis, nota_es,
             nota_in, nota_qui, nota_so, nota_edf]

    plt.bar(x, y, label='Barras', color='green')

    xlabel('Disciplinas', color='black')
    ylabel('Notas', color='black')
    title('Gráfico De Notas')
    subplots_adjust(left=0.21)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    gf = base64.b64encode(image_png)
    gf = gf.decode('utf-8')

    user = DadosPessoais.objects.filter(idAluno=usuario_logado_Resp)
    username = User.objects.filter(id=usuario_logado_Resp)

    return render(request, "paginas/Responsaveis/notas.html", {"notas": notas, 'gf': gf, 'user': user, 'username': username})


@login_required
def advertenciasResp(request):
    user = DadosPessoais.objects.filter(idAluno=usuario_logado_Resp)
    username = User.objects.filter(id=usuario_logado_Resp)
    advertencia = Advertencia.objects.filter(idAluno=usuario_logado_Resp)
    return render(request, "paginas/Responsaveis/advertencias.html", {"advertecia": advertencia, 'user': user, 'username': username})


@login_required
def dadosResp(request):
    user = DadosPessoais.objects.filter(idAluno=usuario_logado_Resp)
    username = User.objects.filter(id=usuario_logado_Resp)
    dado = DadosPessoais.objects.filter(idAluno=usuario_logado_Resp)
    return render(request, "paginas/Responsaveis/dadospessoais.html", {"dados": dado,'user': user, 'username': username})


# Pagina de Responsavel com mais de 1 filho
def inicioRespSurp(request):
    dadoss = list()
    username = User.objects.filter(id=usuario_logado_Resp2)
    alunos = RespSuper.objects.filter(id_resp=usuario_logado_Resp2)
    for a in alunos:
        dadoss.append(DadosPessoais.objects.filter(idAluno=a.id_aluno))
    print(dadoss)
    return render(request, "paginas/SupResp/inicio.html", {'teste': dadoss, 'username': username})


def adverRespSurp(request):
    dadoss = list()
    adv = list()
    username = User.objects.filter(id=usuario_logado_Resp2)
    alunos = RespSuper.objects.filter(id_resp=usuario_logado_Resp2)
    for a in alunos:
        dadoss.append(DadosPessoais.objects.filter(idAluno=a.id_aluno))
        adv.append(Advertencia.objects.filter(idAluno=a.id_aluno))
    print(dadoss)
    return render(request, "paginas/SupResp/adver.html", {'teste': adv, 'user': dadoss, 'username': username})


def chamadaRespSurp(request):
    dadoss = list()
    frq = list()
    username = User.objects.filter(id=usuario_logado_Resp2)
    alunos = RespSuper.objects.filter(id_resp=usuario_logado_Resp2)
    for a in alunos:
        dadoss.append(DadosPessoais.objects.filter(idAluno=a.id_aluno))
        frq.append(Frequencia.objects.filter(idAluno=a.id_aluno))
    print(dadoss)
    return render(request, "paginas/SupResp/frequencia.html", {'teste': frq, 'username': username})


def notasRespSurp(request):
    dadoss = list()
    nots = list()
    username = User.objects.filter(id=usuario_logado_Resp2)
    alunos = RespSuper.objects.filter(id_resp=usuario_logado_Resp2)
    for a in alunos:
        dadoss.append(DadosPessoais.objects.filter(idAluno=a.id_aluno))
        nots.append(Notas.objects.filter(idAluno=a.id_aluno))
    print(dadoss)
    return render(request, "paginas/SupResp/notas.html", {'teste': nots, 'username': username})


def dadosRespSurp(request):
    dadoss = list()
    username = User.objects.filter(id=usuario_logado_Resp2)
    alunos = RespSuper.objects.filter(id_resp=usuario_logado_Resp2)
    for a in alunos:
        dadoss.append(DadosPessoais.objects.filter(idAluno=a.id_aluno))
    print(dadoss)
    return render(request, "paginas/SupResp/dados.html", {'teste': dadoss, 'username': username})