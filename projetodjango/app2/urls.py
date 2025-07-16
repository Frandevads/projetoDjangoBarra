from django.urls import path
from.views import lista_livros, adicionar_livro

urlpatterns = [
    path('', lista_livros),
    path('adicionar_livro/', adicionar_livro),
]