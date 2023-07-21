# ep7_project/ep7/models.py
from django.db import models

class Role(models.Model):
    perfil = models.TextField()

    def __str__(self):
        return self.perfil

class User(models.Model):
    user = models.TextField()
    password = models.CharField(max_length=128)  # You should encrypt the password in a real application
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Pessoa(models.Model):
    nome = models.TextField()
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField()
    nacionalidade = models.TextField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Entidade(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class EntidadePessoa(models.Model):
    pessoaId = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    entidadeId = models.ForeignKey(Entidade, on_delete=models.CASCADE)

class Provincia(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class Distrito(models.Model):
    nome = models.TextField()
    provinciaId = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Estabelecimento(models.Model):
    nome = models.TextField()
    distritoId = models.ForeignKey(Distrito, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class TipoVinculacao(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class TipoEntrada(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class TipoPerda(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class CargoFuncao(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class EspecialidadeMedica(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class Regime(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class NivelOcupacao(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class Carreia(models.Model):
    nome = models.TextField()
    data = models.DateField()
    regimeId = models.ForeignKey(Regime, on_delete=models.CASCADE)
    ocupacaoId = models.ForeignKey(NivelOcupacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.TextField()
    carreiraId = models.ForeignKey(Carreia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Escalao(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class Sector(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class Financiamento(models.Model):
    nome = models.TextField()

    def __str__(self):
        return self.nome

class Entrada(models.Model):
    conclusaoCurso = models.DateField()
    despacho = models.DateField()
    visto = models.DateField()
    observacao = models.TextField()
    pessoalId = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    carreiraId = models.ForeignKey(Carreia, on_delete=models.CASCADE)
    especialidadeId = models.ForeignKey(EspecialidadeMedica, on_delete=models.CASCADE)
    cargoId = models.ForeignKey(CargoFuncao, on_delete=models.CASCADE)
    vinculacaoId = models.ForeignKey(TipoVinculacao, on_delete=models.CASCADE)
    estabelecimentoId = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    entradaId = models.ForeignKey(TipoEntrada, on_delete=models.CASCADE)
    financiamentoId = models.ForeignKey(Financiamento, on_delete=models.CASCADE)
    escalaoId = models.ForeignKey(Escalao, on_delete=models.CASCADE)
    sectorId = models.ForeignKey(Sector, on_delete=models.CASCADE)

class Saida(models.Model):
    despacho = models.DateField()
    visto = models.DateField()
    iniciativaFuncionario = models.TextField()
    entradaId = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    perdaId = models.ForeignKey(TipoPerda, on_delete=models.CASCADE)

    def __str__(self):
        return f"Saida {self.id} - {self.entradaId}"
