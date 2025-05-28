from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Projeto, Tecnologia, Visitante, Professor, Interesse
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseServerError
from .forms import ProjetoForm, InteresseForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.urls import reverse
from django.contrib.auth import login as auth_login
from django.db.models import Count



def contar_visitante(request):
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key

    if not Visitante.objects.filter(session_key=session_key).exists():
        Visitante.objects.create(session_key=session_key)

    return Visitante.objects.count()

# Data atual
data_atual = datetime.now().strftime("%d/%m/%Y")

# Views
def index_view(request):
    visitantes = contar_visitante(request)
    return render(request, "portfolio/index.html", {"data": data_atual, "visitantes": visitantes})

def sobre_view(request):
    visitantes = contar_visitante(request)
    return render(request, "portfolio/sobre.html", {"data": data_atual, "visitantes": visitantes})

def interesses_view(request):
    visitantes = contar_visitante(request)
    return render(request, "portfolio/interesses.html", {"data": data_atual, "visitantes": visitantes})

def tecnologias_view(request):
    visitantes = contar_visitante(request)
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias, "visitantes": visitantes})

def projetos_view(request):
    visitantes = contar_visitante(request)
    projetos = Projeto.objects.all()\
        .select_related('disciplina', 'conceito')\
        .prefetch_related('tecnologias', 'imagens')

    return render(request, "portfolio/projetos.html", {
        "projetos": projetos,
        "data": data_atual,
        "visitantes": visitantes
    })

def contact_view(request):
    visitantes = contar_visitante(request)
    success = False

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        try:
            send_mail(
                subject=f'Nova mensagem de {nome}',
                message=mensagem,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            success = True
        except Exception as e:
            print(f'Erro ao enviar e-mail: {e}')
            return HttpResponseServerError('Erro ao enviar o e-mail')

    return render(request, 'portfolio/contact.html', {'success': success, "visitantes": visitantes})

@login_required
def gerir_projetos_view(request):
    visitantes = contar_visitante(request)
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/gerir_projetos.html', {'projetos': projetos, "visitantes": visitantes})

@login_required
def criar_projeto(request):
    visitantes = contar_visitante(request)
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:gerir_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Criar Projeto', "visitantes": visitantes})

@login_required
def editar_projeto(request, pk):
    visitantes = contar_visitante(request)
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('portfolio:gerir_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'portfolio/projeto_form.html', {'form': form, 'titulo': 'Editar Projeto', "visitantes": visitantes})

@login_required
def eliminar_projeto(request, pk):
    visitantes = contar_visitante(request)
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('portfolio:gerir_projetos')
    return render(request, 'portfolio/projeto_eliminar.html', {'projeto': projeto, "visitantes": visitantes})

def login_view(request):
    visitantes = contar_visitante(request)

    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return render(request, 'portfolio/user.html', {"visitantes": visitantes})
        else:
            return render(request, 'portfolio/login.html', {
                'mensagem': 'Credenciais inválidas',
                'visitantes': visitantes
            })

    if request.user.is_authenticated:
        return render(request, 'portfolio/user.html', {"visitantes": visitantes})
    else:
        return render(request, 'portfolio/login.html', {"visitantes": visitantes})


def logout_view(request):
    logout(request)
    return redirect('portfolio:login')

def registo_view(request):
    visitantes = contar_visitante(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de utilizador já existe.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Já existe uma conta com este email.')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Registo realizado com sucesso. Já pode iniciar sessão.')
            return redirect('portfolio:login')

    return render(request, 'portfolio/registo.html', {'visitantes': visitantes})


signer = TimestampSigner()

def pedido_link_magico_view(request):
    visitantes = contar_visitante(request)
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = signer.sign(user.pk)
            link = request.build_absolute_uri(reverse('portfolio:login_magico') + f'?token={token}')

            # Enviar o email com o link mágico
            send_mail(
                'O teu link mágico para login',
                f'Clica aqui para entrar: {link}',
                'noreply@teuportfolio.com',  # ou settings.DEFAULT_FROM_EMAIL
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Verifica o teu email. Enviámos-te um link mágico.')
        except User.DoesNotExist:
            messages.error(request, 'Este email não está registado.')
    return render(request, 'portfolio/link_magico_pedido.html', {"visitantes": visitantes})

def login_magico_view(request):
    visitantes = contar_visitante(request)
    token = request.GET.get('token')
    try:
        user_id = signer.unsign(token, max_age=300)  # 5 minutos
        user = User.objects.get(pk=user_id)
        auth_login(request, user)
        messages.success(request, 'Autenticado com sucesso via link mágico!')
        return redirect('portfolio:index')
    except (BadSignature, SignatureExpired, User.DoesNotExist):
        messages.error(request, 'O link é inválido ou expirou.')
        return redirect('portfolio:login')

#ESTUDAR

def professor_view(request):
    visitantes= contar_visitante(request)
    professores = Professor.objects.all().order_by('nome')  #Ordena pelo no nome
    return render(request, 'portfolio/professores.html', {
        'professores' : professores,
        'visitantes' : visitantes
        })


#DEFESA

def interesses_defesa_view(request):
    interesses = Interesse.objects.annotate(
        num_projetos=Count('projetos')
    ).order_by('-num_projetos', 'nome')

    return render(request, 'portfolio/interesses_lista.html', {
        'interesses': interesses,
    })

def interesse_detalhe_view(request, pk):
    interesse = get_object_or_404(Interesse, pk=pk)
    return render(request, 'portfolio/interesse_detalhe.html', {
        'interesse': interesse,
    })

def criar_interesses_view(request):
    if request.method == 'POST':
        form = InteresseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:interesses_defesa')
    else:
        form = InteresseForm()
    return render(request, 'portfolio/interesses_form.html', {
        'form': form,
        'titulo': 'Criar Interesse',
    })

def editar_interesse_view(request, pk):
    interesse = get_object_or_404(Interesse, pk=pk)
    if request.method == 'POST':
        form = InteresseForm(request.POST, instance=interesse)
        if form.is_valid():
            form.save()
            return redirect('portfolio:interesses_defesa')
    else:
        form = InteresseForm(instance=interesse)
    return render(request, 'portfolio/interesses_form.html', {
        'form': form,
        'titulo': 'Editar Interesse',
    })






















