from django.shortcuts import render

# Create your views here.
def index(request):
    receitas = {
        1:'Lasanha',
        2:'Sopa de Legumes',
        3:'Sorvete',
        4:'Picadinho',
        5:'Baião de Dois',
        6:'Filé Mingnon'}
    dados = {
        'nome_das_receitas':receitas
    }
    return render(request,'index.html', dados )

def receita(request):
    return render(request,'receita.html')