from django.shortcuts import render
from .models import Pessoa,Carro, Linguagem

# Create your views here.

def home(request):
    pessoa_data = Pessoa.objects.all()
    carro_data = Carro.objects.all()
    ling_data = Linguagem.objects.all()
    return render(request, 'tabela/home.html', {
                    'pessoas':pessoa_data,
                    'carros': carro_data,
                    'linguagens': ling_data,
                    }
            )
