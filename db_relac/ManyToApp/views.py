from django.shortcuts import render
from .models import Pessoa,Carro, Linguagem

# Create your views here.

def home(request):
    pessoa_data = Pessoa.objects.tudo()

    carro_data = Carro.objects.car()
    ling_data = Linguagem.objects.all()
   
    p1 = Pessoa.objects.get(nome="Luzia Lisboa")
    p1.carro
    p1_data = p1.carro.all()

    return render(request, 'tabela/home.html', {
                    'pessoas':pessoa_data,
                    'carros': carro_data,
                    'linguagens': ling_data,
                    'p1s':p1_data,
                    'pss':p1
                    }
            )
