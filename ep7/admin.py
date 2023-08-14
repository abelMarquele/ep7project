from django.contrib import admin

from ep7.models import (
    Role, Pessoa, Entidade, EntidadePessoa, Provincia, Distrito, Estabelecimento, TipoVinculacao, 
    EspecialidadeMedica,TipoEntrada, TipoPerda, CargoFuncao, Regime, NivelOcupacao, Carreia, Categoria,
    Escalao, Sector, Financiamento, Entrada, Saida

)
# Register your models here.
admin.site.register(Role)
admin.site.register(Pessoa)
admin.site.register(Entidade)
admin.site.register(EntidadePessoa)
admin.site.register(Provincia)
admin.site.register(Distrito)
admin.site.register(Estabelecimento)
admin.site.register(TipoVinculacao)
admin.site.register(EspecialidadeMedica)
admin.site.register(TipoEntrada)
admin.site.register(TipoPerda)
admin.site.register(CargoFuncao)
admin.site.register(Regime)
admin.site.register(NivelOcupacao)
admin.site.register(Carreia)
admin.site.register(Categoria)
admin.site.register(Escalao)
admin.site.register(Sector)
admin.site.register(Financiamento)
admin.site.register(Entrada)
admin.site.register(Saida)
