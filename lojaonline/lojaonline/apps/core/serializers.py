from rest_framework import serializers
from .models import ProdutorRural, PropriedadeRural, Raca, Lote, Animal, Veterinario, ProdSanitario, Venda, ComprarAnimal, Ocorrencias, Inseminacao, Movimentacao, ProdutoAlimenticio, Suplementacao, Pesagem, OutraDespesa, AplicarProdutoSanitario, CompraProdutos

class ProdutorRuralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutorRural
        fields = ['id', 'nomeProd', 'cpf', 'email', 'telefone', 'user', 'password']

class PropriedadeRuralSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropriedadeRural
        fields = ['id', 'nomeProp', 'produtor', 'endereco', 'latitude', 'longitude', 'tamanhoAreaProducao']

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ['id','nomeLote', 'tipoCultivo', 'idProp']

class RacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raca
        fields = ['id','nomeRaca']

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id','idRaca', 'observacoesRaca', 'sexo', 'peso', 'dataNascimento', 'dataMorte', 'observacoes', 'rfid', 'idProp', 'idAnimalMae', 'idLote', 'brinco', 'animal_Pai', 'numeroGestacoes']

class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = ['id', 'nome', 'telefone', 'email', 'crmv']

class ProdSanitarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdSanitario
        fields = ['id', 'nome', 'loteProdSanitario', 'valorProdSanitario', 'dataCompraProdSanitario']

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = ['id', 'finalidadeAnimalVenda', 'valorAnimalVenda', 'dataVenda', 'dataRecebimento', 'pesoAnimalVenda', 'precoAtualArrobaKg', 'observacaoVenda', 'idAnimalVenda']

class ComprarAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprarAnimal
        fields = ['id', 'idComprarAnimal', 'dataComprarAnimal', 'valorComprarAnimal', 'observacoesComprarAnimal']

class OcorrenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencias
        fields = ['id', 'ocorrencia', 'idAnimal']

class InseminacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inseminacao
        fields = ['id', 'dataInseminacao', 'horaCio', 'tecnica', 'diaGestacao', 'identificacaoTouro', 'idInseminador', 'idVaca'] 

class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = ['id', 'motivoMovimentacao', 'idAnimal', 'idLoteOrigem', 'idLoteDestino', 'dataMovimentacao']

class ProdutoAlimenticioSerializer(serializers.ModelSerializer):
        class Meta:
            model = ProdutoAlimenticio
            fields = ['id', 'nome', 'tipoProdutoAlimenticio']

class SuplementacaoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Suplementacao
            fields = ['id', 'kgConsumoSuplementacao', 'dataAplicacaoSuplementacao', 'idLoteSuplAplicado', 'idProdutoAlimenticio']

class PesagemSerializer(serializers.ModelSerializer):
        class Meta:
            model = Pesagem
            fields = ['id', 'idAnimal', 'peso', 'dataPesagem']

class OutraDespesaSerializer(serializers.ModelSerializer):
        class Meta:
            model = OutraDespesa
            fields = ['id', 'dataDespesa', 'descricaoOutraDespesa', 'motivoGasto', 'valorOutraDespesa', 'idPropOutraDespesa']

class AplicarProdutoSanitarioSerializer(serializers.ModelSerializer):
        class Meta:
            model = AplicarProdutoSanitario
            fields = ['id', 'idProduto', 'idAnimal', 'dataAplicacao', 'dosagem', 'observacao']

class CompraProdutosSerializer(serializers.ModelSerializer):
        class Meta:
            model = CompraProdutos
            fields = ['id', 'idProduto', 'valorUnitario', 'qtdComprada', 'dataCompra', 'descricao', 'valorTotal', 'validade']