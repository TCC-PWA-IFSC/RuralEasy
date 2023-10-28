from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import datetime
#from core.forms import AnimalFormLazy

##tcc

class ProdutorRural (models.Model):
    cpf = models.CharField()
    email = models.CharField(max_length=100)
    nomeProd = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100, default='telefone')
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeProd

class PropriedadeRural (models.Model):
    nomeProp = models.CharField(max_length=100)
    produtor = models.ForeignKey(ProdutorRural, on_delete=models.CASCADE, blank=True, null=True)
    endereco = models.CharField(max_length=100, default='endereço')
    latitude = models.CharField(max_length=100, default='latitude')
    longitude = models.CharField(max_length=100, default='longitude')
    tamanhoAreaProducao = models.CharField(max_length=100, default='Padrao')

    def __str__(self):
        return self.nomeProp

class Raca (models.Model):
    nomeRaca = models.CharField(max_length=100, default='raça padrao')

    def __str__(self):
        return self.nomeRaca

class Lote (models.Model):
    nomeLote = models.CharField(max_length=100, default='lote padrao')
    tipoCultivo = models.CharField(max_length=100, default='lote padrao')
    idProp = models.ForeignKey(PropriedadeRural, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nomeLote

class Animal (models.Model):
    idRaca = models.ForeignKey(Raca, on_delete=models.CASCADE, blank=True, null=True)
    observacoesRaca = models.CharField(max_length=100, default='padrão')
    sexo = models.CharField(max_length=100, default='padrão')
    peso = models.FloatField(default='0.0')
    dataNascimento = models.DateField (default=datetime.date.today)
    dataMorte = models.DateField (default=datetime.date.today)
    observacoes = models.CharField(max_length=100, default='padrão')
    rfid = models.CharField(max_length=100, default='padrão')
    idProp = models.ForeignKey(PropriedadeRural, on_delete=models.CASCADE, blank=True, null=True)
    idAnimalMae = models.ForeignKey('Animal', on_delete=models.CASCADE, blank=True, null=True)
    idLote = models.ForeignKey(Lote, on_delete=models.CASCADE, blank=True, null=True)
    brinco = models.CharField(max_length=100, default='padrão')
    animal_Pai = models.CharField(max_length=100, default='padrão')
    numeroGestacoes = models.IntegerField(default='0')
    
    def __str__(self):
        return self.brinco

class Veterinario (models.Model):
    nome = models.CharField(max_length=100, default='nome padrao')
    telefone = models.CharField(max_length=100, default='telefone padrao')
    email = models.CharField(max_length=100, default='email padrao')
    crmv = models.CharField(max_length=100, default='crm padrao')

    def __str__(self):
        return self.nome

class ProdSanitario (models.Model):
    nome = models.CharField(max_length=100, default='Padrao')
    loteProdSanitario = models.CharField(max_length=100, default='Padrao')
    valorProdSanitario = models.FloatField(default='0.0')
    dataCompraProdSanitario = models.DateField (default=datetime.date.today)

    def __str__(self):
        return self.nomeProdSanitario

class Venda (models.Model):
    finalidadeAnimalVenda = models.CharField(max_length=100, default='Padrao')
    valorAnimalVenda = models.FloatField(default='0.0')
    dataVenda = models.DateField (default=datetime.date.today)
    dataRecebimento = models.DateField (default=datetime.date.today)
    pesoAnimalVenda = models.FloatField(default='0.0')
    precoAtualArrobaKg = models.FloatField(default='0.0')
    observacaoVenda = models.CharField(max_length=100, default='Padrao')
    idAnimalVenda = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.observacaoVenda

class ComprarAnimal(models.Model):
    idComprarAnimal = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True, null=True)
    dataComprarAnimal = models.DateField (default=datetime.date.today)
    valorComprarAnimal = models.FloatField(default='0.0')
    observacoesComprarAnimal =  models.CharField(max_length=100, default='Padrao')
    
    def __str__(self):
        return self.observacaoComprarAnimal

class Ocorrencias(models.Model):
    ocorrencia = models.CharField(max_length=100, default='Padrao')
    idAnimal = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.ocorrencia

class Inseminacao(models.Model):
    dataInseminacao = models.DateField (default=datetime.date.today)
    horaCio = models.CharField(max_length=100, default='Padrao')
    tecnica = models.CharField(max_length=100, default='Padrao')
    diaGestacao = models.DateField (default=datetime.date.today)
    identificacaoTouro = models.CharField(max_length=100, default='Padrao')
    idInseminador = models.ForeignKey(Veterinario, on_delete=models.CASCADE, blank=True, null=True)
    idVaca = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.tecnica

class Movimentacao(models.Model):
    motivoMovimentacao = models.CharField(max_length=100, default='Padrao')
    idAnimal = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True, null=True)
    idLoteOrigem = models.ForeignKey(Lote, on_delete=models.CASCADE, blank=True, null=True, related_name="movimentacoes_origem")
    idLoteDestino = models.ForeignKey(Lote, on_delete=models.CASCADE, blank=True, null=True, related_name="movimentacoes_destino")
    dataMovimentacao = models.DateField (default=datetime.date.today)

    def __str__(self):
        return self.motivoMovimentacao

class ProdutoAlimenticio(models.Model):
    nome = models.CharField(max_length=100, default='Padrao')
    tipoProdutoAlimenticio = models.CharField(max_length=100, default='Padrao')

    def __str__(self):
        return self.nomeProdutoAlimenticio

class Suplementacao(models.Model):
    kgConsumoSuplementacao = models.FloatField(default='0.0')
    dataAplicacaoSuplementacao = models.DateField (default=datetime.date.today)
    idLoteSuplAplicado = models.ForeignKey(Lote, on_delete=models.CASCADE, blank=True, null=True)
    idProdutoAlimenticio = models.ForeignKey(ProdutoAlimenticio, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.kgConsumoSuplementacao

class Pesagem(models.Model):
    idAnimal = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True, null=True)
    peso = models.FloatField(default='0.0')
    dataPesagem = models.DateField (default=datetime.date.today)

    def __str__(self):
        return self.peso

class OutraDespesa(models.Model):
    dataDespesa = models.DateField (default=datetime.date.today)
    descricaoOutraDespesa = models.CharField(max_length=100, default='Padrao')
    motivoGasto = models.CharField(max_length=100, default='Padrao')
    valorOutraDespesa = models.FloatField(default='0.0')
    idPropOutraDespesa = models.ForeignKey(PropriedadeRural, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.descricaoOutraDespesa

class AplicarProdutoSanitario(models.Model):
    idProduto = models.ForeignKey(ProdSanitario, on_delete=models.CASCADE, blank=True, null=True)
    idAnimal = models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True, null=True)
    dataAplicacao = models.DateField (default=datetime.date.today)
    dosagem = models.CharField(max_length=100, default='Padrao')
    observacao = models.CharField(max_length=100, default='Padrao')
    
    def __str__(self):
        return self.observacao

class CompraProdutos(models.Model):
    #idProduto = models.ForeignKey(ProdSanitario, on_delete=models.CASCADE, blank=True, null=True)
    #valorUnitario = models.FloatField(default='0.0')
    #qtdComprada = models.IntegerField(default='0')
    #dataCompra = models.DateField (default=datetime.date.today)
    #descricao = models.CharField(max_length=100, default='Padrao')
    #valorTotal = models.FloatField(default='0.0')
    #validade = models.DateField (default=datetime.date.today)
    #content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #object_id = models.PositiveIntegerField()
    #idProduto = GenericForeignKey('content_type', 'object_id')

    idProduto = models.CharField(max_length=100, default='Padrao')
    valorUnitario = models.FloatField(default='0.0')
    qtdComprada = models.IntegerField(default='0')
    dataCompra = models.DateField (default=datetime.date.today)
    descricao = models.CharField(max_length=100, default='Padrao')
    valorTotal = models.FloatField(default='0.0')
    validade = models.DateField (default=datetime.date.today)

    def __str__(self):
        return self.descricao