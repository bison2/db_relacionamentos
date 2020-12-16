from django.contrib import admin
from ManyToApp.models import (Pessoa,
                        Filmes,
                        Programador,
                        Linguagem,
                        ProgramadorLinguagem,
                        DocumentoCpf,
                        Carro)

                        
# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Filmes)
admin.site.register(Programador)
admin.site.register(Linguagem)
admin.site.register(ProgramadorLinguagem)
admin.site.register(DocumentoCpf)
admin.site.register(Carro)

