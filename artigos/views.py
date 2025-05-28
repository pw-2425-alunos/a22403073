from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Rating
from .forms import ArtigoForm
from .forms import ComentarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

def listar_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/artigos.html', {'artigos': artigos})


def ver_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, pk=artigo_id)
    media_rating = artigo.ratings.aggregate(avg=Avg('rate'))['avg']
    return render(request, 'artigos/artigo_detalhe.html', {
        'artigo': artigo,
        'media_rating': media_rating
    })


def gerir_artigos_view(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/gerir_artigos.html', {'artigos': artigos})

def criar_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artigos:gerir_artigos')
    else:
        form = ArtigoForm()
    return render(request, 'artigos/artigo_form.html', {'form': form, 'operacao': 'Criar'})

def editar_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:gerir_artigos')
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'artigos/artigo_form.html', {'form': form, 'operacao': 'Editar'})

def eliminar_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos:gerir_artigos')
    return render(request, 'artigos/artigo_eliminar.html', {'artigo': artigo})


@login_required
def avaliar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    if request.method == 'POST':
        rate = int(request.POST.get('rating', 0))

        rating, created = Rating.objects.update_or_create(
            artigo=artigo,
            usuario=request.user,
            defaults={'rate': rate}
        )

    return redirect('artigos:ver_artigo', artigo_id=artigo_id)

