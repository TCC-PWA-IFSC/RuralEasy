from django import forms
from .models import ProdutorRural, PropriedadeRural, Raca, Lote, Animal, Veterinario, ProdSanitario, Venda, ComprarAnimal, Ocorrencias, Inseminacao, Movimentacao, ProdutoAlimenticio, Suplementacao, Pesagem, OutraDespesa, AplicarProdutoSanitario, CompraProdutos

class ProdutorRuralForm(forms.ModelForm):
        class Meta:
            model = ProdutorRural
            fields = ['nomeProd', 'cpf', 'email', 'telefone', 'user', 'password']

class PropriedadeRuralForm(forms.ModelForm):
        class Meta:
            model = PropriedadeRural
            fields = ['nomeProp', 'produtor', 'endereco', 'latitude', 'longitude', 'tamanhoAreaProducao']

class LoteForm(forms.ModelForm):
        class Meta:
            model = Lote
            fields = ['nomeLote', 'tipoCultivo', 'idProp']

class RacaForm(forms.ModelForm):
        class Meta:
            model = Raca
            fields = ['nomeRaca']

class AnimalForm(forms.ModelForm):
        class Meta:
            model = Animal
            fields = ['idRaca', 'observacoesRaca', 'sexo', 'peso', 'dataNascimento', 'dataMorte', 'observacoes', 'rfid', 'idProp', 'idAnimalMae', 'idLote', 'brinco', 'animal_Pai', 'numeroGestacoes']

class VeterinarioForm(forms.ModelForm):
        class Meta:
            model = Veterinario
            fields = ['nome', 'telefone', 'email', 'crmv']

class ProdSanitarioForm(forms.ModelForm):
        class Meta:
            model = ProdSanitario
            fields = ['id', 'nome', 'loteProdSanitario', 'valorProdSanitario', 'dataCompraProdSanitario']

class VendaForm(forms.ModelForm):
        class Meta:
            model = Venda
            fields = ['id', 'finalidadeAnimalVenda', 'valorAnimalVenda', 'dataVenda', 'dataRecebimento', 'pesoAnimalVenda', 'precoAtualArrobaKg', 'observacaoVenda', 'idAnimalVenda']

class ComprarAnimalForm(forms.ModelForm):
        class Meta:
            model = ComprarAnimal
            fields = ['id', 'idComprarAnimal', 'dataComprarAnimal', 'valorComprarAnimal', 'observacoesComprarAnimal']

class OcorrenciasForm(forms.ModelForm):
        class Meta:
            model = Ocorrencias
            fields = ['id', 'ocorrencia', 'idAnimal']

class InseminacaoForm(forms.ModelForm):
        class Meta:
            model = Inseminacao
            fields = ['id', 'dataInseminacao', 'horaCio', 'tecnica', 'diaGestacao', 'identificacaoTouro', 'idInseminador', 'idVaca'] 

class MovimentacaoForm(forms.ModelForm):
        class Meta:
            model = Movimentacao
            fields = ['id', 'motivoMovimentacao', 'idAnimal', 'idLoteOrigem', 'idLoteDestino', 'dataMovimentacao']

class ProdutoAlimenticioForm(forms.ModelForm):
        class Meta:
            model = ProdutoAlimenticio
            fields = ['id', 'nome', 'tipoProdutoAlimenticio']

class SuplementacaoForm(forms.ModelForm):
        class Meta:
            model = Suplementacao
            fields = ['id', 'kgConsumoSuplementacao', 'dataAplicacaoSuplementacao', 'idLoteSuplAplicado', 'idProdutoAlimenticio']

class PesagemForm(forms.ModelForm):
        class Meta:
            model = Pesagem
            fields = ['id', 'idAnimal', 'peso', 'dataPesagem']

class OutraDespesaForm(forms.ModelForm):
        class Meta:
            model = OutraDespesa
            fields = ['id', 'dataDespesa', 'descricaoOutraDespesa', 'motivoGasto', 'valorOutraDespesa', 'idPropOutraDespesa']

class AplicarProdutoSanitarioForm(forms.ModelForm):
        class Meta:
            model = AplicarProdutoSanitario
            fields = ['id', 'idProduto', 'idAnimal', 'dataAplicacao', 'dosagem', 'observacao']

class CompraProdutosForm(forms.ModelForm):
        class Meta:
            model = CompraProdutos
            fields = ['id', 'idProduto', 'valorUnitario', 'qtdComprada', 'dataCompra', 'descricao', 'valorTotal', 'validade']