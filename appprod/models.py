from django.db import models

# Create your models here.

class Prestador(models.Model):
    nome = models.CharField("Nome", max_length=250, null=False)
    cpf = models.CharField("CPF", max_length=14, unique=True, null=False)
    data_nascimento = models.DateField("Data de Nascimento", null=False, blank=True)
    email = models.EmailField("E-Mail", max_length=200)
    telefone = models.CharField("Telefone", max_length=20)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, verbose_name="Cargo")


class Cargo(models.Model):
    salario = models.DecimalField("Salário",max_digits=20, decimal_places=2)
    cargo = models.CharField("Cargo", max_length=250, null=False, unique=True)


class UnidadeMedida(models.Model):
    descricao=models.CharField("Descrição",max_length=100)
    sigla=models.CharField("Sigla",max_length=5)
    def __str__(self):
        return "{0:s}-{1:s}".format(self.descricao,self.sigla)


class MateriaPrima(models.Model):
    descricao = models.CharField("Descrição", max_length=250, null=False, unique=True)
    quantidade_estoque = models.IntegerField("Quantidade em estoque", max_digits=20)
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.PROTECT, verbose_name="Unidade de Medida")

class EtapaProducao(models.Model):
    descricao = models.CharField("Descrição", max_length=250, null=False, unique=True)
    quantidade_utilizada = models.IntegerField("Quantidade utilizada", max_digits=20)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.PROTECT, verbose_name="Matéria Prima")
    processo_producao = models.ForeignKey(ProcessoProducao, on_delete=models.PROTECT, verbose_name="Processo de Produção")


class ProcessoProducao(models.Model):
    data_inicio = models.DateField("Data de Início", null=False)
    data_termino = models.DateField("Data de Término",null=True, blank=True)
    descricao = models.CharField("Descrição", max_length=250, null=False, unique=True)
    prestador = models.ManyToManyField(Prestador)


