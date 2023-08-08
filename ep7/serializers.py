# ep7_project/ep7/serializers.py
from rest_framework import serializers
from .models import Role, User, Pessoa, Entidade, EntidadePessoa, Provincia, Distrito, Estabelecimento, TipoVinculacao, TipoEntrada, TipoPerda, CargoFuncao, EspecialidadeMedica, Regime, NivelOcupacao, Carreia, Categoria, Escalao, Sector, Financiamento, Entrada, Saida

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        depth = 1

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
        depth = 1

class EntidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidade
        fields = '__all__'
        depth = 1

class EntidadePessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntidadePessoa
        fields = '__all__'
        depth = 1

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'
        depth = 1

class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = '__all__'
        depth = 1

class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = '__all__'
        depth = 1

class TipoVinculacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVinculacao
        fields = '__all__'
        depth = 1

class TipoEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEntrada
        fields = '__all__'
        depth = 1

class TipoPerdaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPerda
        fields = '__all__'
        depth = 1

class CargoFuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoFuncao
        fields = '__all__'
        depth = 1

class EspecialidadeMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspecialidadeMedica
        fields = '__all__'
        depth = 1

class RegimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regime
        fields = '__all__'
        depth = 1

class NivelOcupacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelOcupacao
        fields = '__all__'
        depth = 1

class CarreiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreia
        fields = '__all__'
        depth = 1

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        depth = 1

class EscalaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escalao
        fields = '__all__'
        depth = 1

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'
        depth = 1

class FinanciamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiamento
        fields = '__all__'
        depth = 1

class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = '__all__'
        depth = 1

class SaidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saida
        fields = '__all__'
        depth = 1
