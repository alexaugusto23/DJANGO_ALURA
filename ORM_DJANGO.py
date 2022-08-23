from django.db import models

class Pessoa(models.Model):
   nome = models.CharField(max_length=200)
   email = models.CharField(max_length=200)

 def __str__(self):
       return self.nome

# Método para salvar.
pessoa = Pessoa(nome='Adriélly', email='adrielly@alura.com')
pessoa.save()

# Método para criar e salvar.
Pessoa.objects.create(nome='Guilherme', email='gui@alura.com')

# Método para buscar tudo.
Pessoa.objects.all()

# Método para buscar uma informção especifica.
pessoa = Pessoa.objects.get(nome='Guilherme')

# Método para altualizar.
pessoa.email = 'guilherme@alura.com'
pessoa.save()

# Método para deletar.
pessoa = Pessoa.objects.get(id=1)
pessoa.delete()

# Filtros

from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    modo_preparo = models.TextField()
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_receita

# Filtrando tudo.
receitas_publicadas = Receita.objects.filter(publicada=True)

# Filtro especifico.
receita_publicada_chocolate = Receita.objects.filter(publicada=True, nome_receita='Bolo de chocolate')

# Ordenação

# Ordenar por receita.
receitas_ordenadas = Receita.objects.order_by('nome_receita')
