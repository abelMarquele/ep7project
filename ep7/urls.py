# ep7_project/ep7/urls.py
from django.urls import path
from .views import (
    RoleListCreateView, RoleRetrieveUpdateDestroyView,
    UserListCreateView, UserRetrieveUpdateDestroyView,
    PessoaListCreateView, PessoaRetrieveUpdateDestroyView,
    EntidadeListCreateView, EntidadeRetrieveUpdateDestroyView,
    EntidadePessoaListCreateView, EntidadePessoaRetrieveUpdateDestroyView,
    ProvinciaListCreateView, ProvinciaRetrieveUpdateDestroyView,
    DistritoListCreateView, DistritoRetrieveUpdateDestroyView,
    EstabelecimentoListCreateView, EstabelecimentoRetrieveUpdateDestroyView,
    TipoVinculacaoListCreateView, TipoVinculacaoRetrieveUpdateDestroyView,
    TipoEntradaListCreateView, TipoEntradaRetrieveUpdateDestroyView,
    TipoPerdaListCreateView, TipoPerdaRetrieveUpdateDestroyView,
    CargoFuncaoListCreateView, CargoFuncaoRetrieveUpdateDestroyView,
    EspecialidadeMedicaListCreateView, EspecialidadeMedicaRetrieveUpdateDestroyView,
    RegimeListCreateView, RegimeRetrieveUpdateDestroyView,
    NivelOcupacaoListCreateView, NivelOcupacaoRetrieveUpdateDestroyView,
    CarreiaListCreateView, CarreiaRetrieveUpdateDestroyView,
    CategoriaListCreateView, CategoriaRetrieveUpdateDestroyView,
    EscalaoListCreateView, EscalaoRetrieveUpdateDestroyView,
    SectorListCreateView, SectorRetrieveUpdateDestroyView,
    FinanciamentoListCreateView, FinanciamentoRetrieveUpdateDestroyView,
    EntradaListCreateView, EntradaRetrieveUpdateDestroyView,
    SaidaListCreateView, SaidaRetrieveUpdateDestroyView,
)

from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ep7",
        default_version='v1',
        description="Descrição da API ep7",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="abel.marquele@jhpiego.org"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)










urlpatterns = [
    # URLs for Role model
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', RoleRetrieveUpdateDestroyView.as_view(), name='role-retrieve-update-destroy'),

    # URLs for User model
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),

    # URLs for Pessoa model
    path('pessoas/', PessoaListCreateView.as_view(), name='pessoa-list-create'),
    path('pessoas/<int:pk>/', PessoaRetrieveUpdateDestroyView.as_view(), name='pessoa-retrieve-update-destroy'),

    # URLs for Entidade model
    path('entidades/', EntidadeListCreateView.as_view(), name='entidade-list-create'),
    path('entidades/<int:pk>/', EntidadeRetrieveUpdateDestroyView.as_view(), name='entidade-retrieve-update-destroy'),

    # URLs for EntidadePessoa model
    path('entidadepessoas/', EntidadePessoaListCreateView.as_view(), name='entidadepessoa-list-create'),
    path('entidadepessoas/<int:pk>/', EntidadePessoaRetrieveUpdateDestroyView.as_view(), name='entidadepessoa-retrieve-update-destroy'),

    # URLs for Provincia model
    path('provincias/', ProvinciaListCreateView.as_view(), name='provincia-list-create'),
    path('provincias/<int:pk>/', ProvinciaRetrieveUpdateDestroyView.as_view(), name='provincia-retrieve-update-destroy'),

    # URLs for Distrito model
    path('distritos/', DistritoListCreateView.as_view(), name='distrito-list-create'),
    path('distritos/<int:pk>/', DistritoRetrieveUpdateDestroyView.as_view(), name='distrito-retrieve-update-destroy'),

    # URLs for Estabelecimento model
    path('estabelecimentos/', EstabelecimentoListCreateView.as_view(), name='estabelecimento-list-create'),
    path('estabelecimentos/<int:pk>/', EstabelecimentoRetrieveUpdateDestroyView.as_view(), name='estabelecimento-retrieve-update-destroy'),

    # URLs for TipoVinculacao model
    path('tiposvinculacao/', TipoVinculacaoListCreateView.as_view(), name='tipovinculacao-list-create'),
    path('tiposvinculacao/<int:pk>/', TipoVinculacaoRetrieveUpdateDestroyView.as_view(), name='tipovinculacao-retrieve-update-destroy'),

    # URLs for TipoEntrada model
    path('tiposentrada/', TipoEntradaListCreateView.as_view(), name='tipoentrada-list-create'),
    path('tiposentrada/<int:pk>/', TipoEntradaRetrieveUpdateDestroyView.as_view(), name='tipoentrada-retrieve-update-destroy'),

    # URLs for TipoPerda model
    path('tiposperda/', TipoPerdaListCreateView.as_view(), name='tipoperda-list-create'),
    path('tiposperda/<int:pk>/', TipoPerdaRetrieveUpdateDestroyView.as_view(), name='tipoperda-retrieve-update-destroy'),

    # URLs for CargoFuncao model
    path('cargosfuncao/', CargoFuncaoListCreateView.as_view(), name='cargofuncao-list-create'),
    path('cargosfuncao/<int:pk>/', CargoFuncaoRetrieveUpdateDestroyView.as_view(), name='cargofuncao-retrieve-update-destroy'),

    # URLs for EspecialidadeMedica model
    path('especialidadesmedicas/', EspecialidadeMedicaListCreateView.as_view(), name='especialidademedica-list-create'),
    path('especialidadesmedicas/<int:pk>/', EspecialidadeMedicaRetrieveUpdateDestroyView.as_view(), name='especialidademedica-retrieve-update-destroy'),

    # URLs for Regime model
    path('regimes/', RegimeListCreateView.as_view(), name='regime-list-create'),
    path('regimes/<int:pk>/', RegimeRetrieveUpdateDestroyView.as_view(), name='regime-retrieve-update-destroy'),

    # URLs for NivelOcupacao model
    path('niveisocupacao/', NivelOcupacaoListCreateView.as_view(), name='nivelocupacao-list-create'),
    path('niveisocupacao/<int:pk>/', NivelOcupacaoRetrieveUpdateDestroyView.as_view(), name='nivelocupacao-retrieve-update-destroy'),

    # URLs for Carreia model
    path('carreias/', CarreiaListCreateView.as_view(), name='carreia-list-create'),
    path('carreias/<int:pk>/', CarreiaRetrieveUpdateDestroyView.as_view(), name='carreia-retrieve-update-destroy'),

    # URLs for Categoria model
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', CategoriaRetrieveUpdateDestroyView.as_view(), name='categoria-retrieve-update-destroy'),

    # URLs for Escalao model
    path('escaloes/', EscalaoListCreateView.as_view(), name='escalao-list-create'),
    path('escaloes/<int:pk>/', EscalaoRetrieveUpdateDestroyView.as_view(), name='escalao-retrieve-update-destroy'),

    # URLs for Sector model
    path('sectores/', SectorListCreateView.as_view(), name='sector-list-create'),
    path('sectores/<int:pk>/', SectorRetrieveUpdateDestroyView.as_view(), name='sector-retrieve-update-destroy'),

    # URLs for Financiamento model
    path('financiamentos/', FinanciamentoListCreateView.as_view(), name='financiamento-list-create'),
    path('financiamentos/<int:pk>/', FinanciamentoRetrieveUpdateDestroyView.as_view(), name='financiamento-retrieve-update-destroy'),

    # URLs for Entrada model
    path('entradas/', EntradaListCreateView.as_view(), name='entrada-list-create'),
    path('entradas/<int:pk>/', EntradaRetrieveUpdateDestroyView.as_view(), name='entrada-retrieve-update-destroy'),

    # URLs for Saida model
    path('saidas/', SaidaListCreateView.as_view(), name='saida-list-create'),
    path('saidas/<int:pk>/', SaidaRetrieveUpdateDestroyView.as_view(), name='saida-retrieve-update-destroy'),


    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
