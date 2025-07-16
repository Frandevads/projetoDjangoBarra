from django.shortcuts import render, redirect
from .models import Livro
# Create your views here.
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})







def adicionar_livro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        ano_publicacao = request.POST.get('ano_publicacao')
        Livro.objects   .create(titulo=titulo, autor=autor, ano_publicacao=ano_publicacao)
        return redirect('lista_livros')
    return render(request, 'form_livro.html')

