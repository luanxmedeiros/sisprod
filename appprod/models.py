from django.db import models

# Create your models here.
class Cargo(models.Model):
    salario = models.DecimalField("Salário",max_digits=20, decimal_places=2)
    cargo = models.CharField("Cargo", max_length=250, null=False, unique=True)
    def __str__(self):
        return "{0:s}".format(self.cargo)

class Prestador(models.Model):
    nome = models.CharField("Nome", max_length=250, null=False)
    cpf = models.CharField("CPF", max_length=14, unique=True, null=False)
    data_nascimento = models.DateField("Data de Nascimento", null=False, blank=True)
    email = models.EmailField("E-Mail", max_length=200)
    telefone = models.CharField("Telefone", max_length=20)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, verbose_name="Cargo")
    def __str__(self):
        return "{0:s}".format(self.nome)

class UnidadeMedida(models.Model):
    descricao=models.CharField("Descrição",max_length=100)
    sigla=models.CharField("Sigla",max_length=5)
    def __str__(self):
        return "{0:s}-{1:s}".format(self.descricao,self.sigla)

class ProcessoProducao(models.Model):
    data_inicio = models.DateField("Data de Início", null=True, blank=True)
    data_termino = models.DateField("Data de Término",null=True, blank=True)
    descricao = models.CharField("Descrição", max_length=250, null=False, unique=True)
    prestador = models.ManyToManyField(Prestador)
    def __str__(self):
        return "{0:s}".format(self.descricao)

class MateriaPrima(models.Model):
    descricao = models.CharField("Descrição", max_length=250, null=False, unique=True)
    quantidade_estoque = models.DecimalField("Quantidade em estoque", max_digits=20, decimal_places=2)
    custo = models.DecimalField("Custo", max_digits=20, decimal_places=2)
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.PROTECT, verbose_name="Unidade de Medida")
    def __str__(self):
        return "{0:s}".format(self.descricao)

class EtapaProducao(models.Model):
    descricao = models.CharField("Descrição", max_length=250, null=False, unique=True)
    processo_producao = models.ForeignKey(ProcessoProducao, on_delete=models.PROTECT, verbose_name="Processo de Produção")
    materia_etapa = models.ManyToManyField(MateriaPrima, through="MateriaEtapa")
    def __str__(self):
        return "{0:s}".format(self.descricao)

class MateriaEtapa(models.Model):
    quantidade_materia_etapa = models.DecimalField("Quantidade Etapa", max_digits=20, decimal_places=2)
    etapa_producao = models.ForeignKey(EtapaProducao, on_delete=models.PROTECT, verbose_name="Etapa Produção")
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.PROTECT, verbose_name="Matéria Prima")






