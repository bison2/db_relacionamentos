from django.shortcuts import render
from .models import Pessoa,Carro, Linguagem

# Create your views here.

def home(request):
    pessoa_data = Pessoa.objects.tudo()
    carro_data = Carro.objects.car()
    ling_data = Linguagem.objects.linguagem()

    p_carro_data = Pessoa.objects.p_car()
       
    return render(request, 'tabela/home.html', {
                    'pessoas':pessoa_data,
                    'carros': carro_data,
                    'linguagens': ling_data,
                    'pessoas': p_carro_data,
                    }
            )
