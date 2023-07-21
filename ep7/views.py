# ep7_project/ep7/views.py
from rest_framework import generics
from .models import Role, User, Pessoa, Entidade, EntidadePessoa, Provincia, Distrito, Estabelecimento, TipoVinculacao, TipoEntrada, TipoPerda, CargoFuncao, EspecialidadeMedica, Regime, NivelOcupacao, Carreia, Categoria, Escalao, Sector, Financiamento, Entrada, Saida
from .serializers import RoleSerializer, UserSerializer, PessoaSerializer, EntidadeSerializer, EntidadePessoaSerializer, ProvinciaSerializer, DistritoSerializer, EstabelecimentoSerializer, TipoVinculacaoSerializer, TipoEntradaSerializer, TipoPerdaSerializer, CargoFuncaoSerializer, EspecialidadeMedicaSerializer, RegimeSerializer, NivelOcupacaoSerializer, CarreiaSerializer, CategoriaSerializer, EscalaoSerializer, SectorSerializer, FinanciamentoSerializer, EntradaSerializer, SaidaSerializer

# Views for Role model
class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

# Views for User model
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Views for Pessoa model
class PessoaListCreateView(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

# Views for Entidade model
class EntidadeListCreateView(generics.ListCreateAPIView):
    queryset = Entidade.objects.all()
    serializer_class = EntidadeSerializer

class EntidadeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entidade.objects.all()
    serializer_class = EntidadeSerializer

# Views for EntidadePessoa model
class EntidadePessoaListCreateView(generics.ListCreateAPIView):
    queryset = EntidadePessoa.objects.all()
    serializer_class = EntidadePessoaSerializer

class EntidadePessoaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EntidadePessoa.objects.all()
    serializer_class = EntidadePessoaSerializer

# Views for Provincia model
class ProvinciaListCreateView(generics.ListCreateAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class ProvinciaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

# Views for Distrito model
class DistritoListCreateView(generics.ListCreateAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer

class DistritoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer

# Views for Estabelecimento model
class EstabelecimentoListCreateView(generics.ListCreateAPIView):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer

class EstabelecimentoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer

# Views for TipoVinculacao model
class TipoVinculacaoListCreateView(generics.ListCreateAPIView):
    queryset = TipoVinculacao.objects.all()
    serializer_class = TipoVinculacaoSerializer

class TipoVinculacaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoVinculacao.objects.all()
    serializer_class = TipoVinculacaoSerializer

# Views for TipoEntrada model
class TipoEntradaListCreateView(generics.ListCreateAPIView):
    queryset = TipoEntrada.objects.all()
    serializer_class = TipoEntradaSerializer

class TipoEntradaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoEntrada.objects.all()
    serializer_class = TipoEntradaSerializer

# Views for TipoPerda model
class TipoPerdaListCreateView(generics.ListCreateAPIView):
    queryset = TipoPerda.objects.all()
    serializer_class = TipoPerdaSerializer

class TipoPerdaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoPerda.objects.all()
    serializer_class = TipoPerdaSerializer

# Views for CargoFuncao model
class CargoFuncaoListCreateView(generics.ListCreateAPIView):
    queryset = CargoFuncao.objects.all()
    serializer_class = CargoFuncaoSerializer

class CargoFuncaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CargoFuncao.objects.all()
    serializer_class = CargoFuncaoSerializer

# Views for EspecialidadeMedica model
class EspecialidadeMedicaListCreateView(generics.ListCreateAPIView):
    queryset = EspecialidadeMedica.objects.all()
    serializer_class = EspecialidadeMedicaSerializer

class EspecialidadeMedicaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EspecialidadeMedica.objects.all()
    serializer_class = EspecialidadeMedicaSerializer

# Views for Regime model
class RegimeListCreateView(generics.ListCreateAPIView):
    queryset = Regime.objects.all()
    serializer_class = RegimeSerializer

class RegimeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Regime.objects.all()
    serializer_class = RegimeSerializer

# Views for NivelOcupacao model
class NivelOcupacaoListCreateView(generics.ListCreateAPIView):
    queryset = NivelOcupacao.objects.all()
    serializer_class = NivelOcupacaoSerializer

class NivelOcupacaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NivelOcupacao.objects.all()
    serializer_class = NivelOcupacaoSerializer

# Views for Carreia model
class CarreiaListCreateView(generics.ListCreateAPIView):
    queryset = Carreia.objects.all()
    serializer_class = CarreiaSerializer

class CarreiaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carreia.objects.all()
    serializer_class = CarreiaSerializer

# Views for Categoria model
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Views for Escalao model
class EscalaoListCreateView(generics.ListCreateAPIView):
    queryset = Escalao.objects.all()
    serializer_class = EscalaoSerializer

class EscalaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Escalao.objects.all()
    serializer_class = EscalaoSerializer

# Views for Sector model
class SectorListCreateView(generics.ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class SectorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

# Views for Financiamento model
class FinanciamentoListCreateView(generics.ListCreateAPIView):
    queryset = Financiamento.objects.all()
    serializer_class = FinanciamentoSerializer

class FinanciamentoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Financiamento.objects.all()
    serializer_class = FinanciamentoSerializer

# Views for Entrada model
class EntradaListCreateView(generics.ListCreateAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

class EntradaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

# Views for Saida model
class SaidaListCreateView(generics.ListCreateAPIView):
    queryset = Saida.objects.all()
    serializer_class = SaidaSerializer

class SaidaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saida.objects.all()
    serializer_class = SaidaSerializer
