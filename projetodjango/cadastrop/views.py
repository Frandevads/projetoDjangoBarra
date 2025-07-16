from django.shortcuts import render, redirect
from .models import Produto

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')

        Produto.objects.create(
            nome=nome,
            preco=preco,
            descricao=descricao
        )
        return redirect('/produtos')  # ou redirecionar para outra página

    return render(request, 'cadastroProdutos.html')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listaProdutos.html', {'produtos': produtos})


