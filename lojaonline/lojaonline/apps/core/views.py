from django.shortcuts import render
from .models import ProdutorRural, PropriedadeRural, Animal, Raca, Lote, Veterinario, ProdSanitario, Venda, ComprarAnimal, Ocorrencias, Inseminacao, Movimentacao, ProdutoAlimenticio, Suplementacao, Pesagem, OutraDespesa, AplicarProdutoSanitario, CompraProdutos
from .forms import ProdutorRuralForm, PropriedadeRuralForm, AnimalForm, LoteForm, RacaForm, VeterinarioForm, ProdSanitarioForm, VendaForm, ComprarAnimalForm, OcorrenciasForm, InseminacaoForm, MovimentacaoForm, ProdutoAlimenticioForm, SuplementacaoForm, PesagemForm, OutraDespesaForm, AplicarProdutoSanitarioForm, CompraProdutosForm
from rest_framework import generics
from .serializers import ProdutorRuralSerializer, PropriedadeRuralSerializer, AnimalSerializer, RacaSerializer, LoteSerializer, VeterinarioSerializer, ProdSanitarioSerializer, VendaSerializer, ComprarAnimalSerializer, OcorrenciasSerializer, InseminacaoSerializer, MovimentacaoSerializer, ProdutoAlimenticioSerializer, SuplementacaoSerializer, PesagemSerializer, OutraDespesaSerializer, AplicarProdutoSanitarioSerializer, CompraProdutosSerializer
from django.http import JsonResponse, QueryDict
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

#- Tabela 1 - Produtor Rural (Nome, CPF, e-mail).
#- Tabela 2 - Propriedade Rural (Nome, Produtor)

#PRODUTOR
def lista_produtores(request):
    template_name = 'core/produtores.html'
    produtores = ProdutorRural.objects.all()
    context = {
        'produtores': produtores
    }
    return render(request, template_name, context)

def mostra_produtor(request, id_produtor):
    template_name = 'core/produtor.html'
    produtor = ProdutorRural.objects.get(id=id_produtor)
    context = {
        'produtores': produtor
    }

    return render(request, template_name, context)

def delete_produtor(request, produtor_id):
    produtor = get_object_or_404(ProdutorRural, id=produtor_id)
    produtor.delete()
    return JsonResponse({'message': 'Produtor excluído com sucesso.'})

def adicionar_produtor(request):
    if request.method == 'POST':
        serializer = ProdutorRuralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'Produtor adicionado com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)


@csrf_exempt
def editar_produtor(request, pk):
    produtor = get_object_or_404(ProdutorRural, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProdutorRuralSerializer(produtor, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Produtor rural editado com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = ProdutorRuralForm(instance=produtor)

    return render(request, 'editar_produtor.html', {'form': form, 'produtor': produtor})


#PROPRIEDADE
def lista_propriedades(request):
    template_name = 'core/propriedades.html'
    propriedades = PropriedadeRural.objects.all()
    context = {
        'propriedades': propriedades
    }
    return render(request, template_name, context)

def mostra_propriedade(request, id_propriedade):
    template_name = 'core/propriedade.html'
    propriedade = PropriedadeRural.objects.get(id=id_propriedade)
    context = {
        'propriedades': propriedade
    }

    return render(request, template_name, context) 

def delete_propriedade(request, propriedade_id):
    propriedade = get_object_or_404(PropriedadeRural, id=propriedade_id)
    propriedade.delete()
    return JsonResponse({'message': 'Propriedade excluída com sucesso.'})

def adicionar_propriedade(request):
    if request.method == 'POST':
        serializer = PropriedadeRuralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'Propriedade adicionada com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_propriedade(request, pk):
    propriedade = get_object_or_404(PropriedadeRural, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PropriedadeRuralSerializer(propriedade, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Propriedade rural editada com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = PropriedadeRuralForm(instance=propriedade)

    return render(request, 'editar_propriedade.html', {'form': form, 'propriedade': propriedade})

#ANIMAL
def lista_animais(request):
    template_name = 'core/animais.html'
    animais = Animal.objects.all()
    context = {
        'animais': animais
    }
    return render(request, template_name, context)

def mostra_animal(request, id_animal):
    template_name = 'core/animal.html'
    animal = Animal.objects.get(id=id_animal)
    context = {
        'animais': animal
    }

    return render(request, template_name, context)

def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    animal.delete()
    return JsonResponse({'message': 'Animal excluído com sucesso.'})

def adicionar_animal(request):
    if request.method == 'POST':
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'Animal adicionado com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AnimalSerializer(animal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Animal editado com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = AnimalForm(instance=animal)

    return render(request, 'editar_animal.html', {'form': form, 'animal': animal})

#LOTE
def lista_lotes(request):
    template_name = 'core/lotes.html'
    lotes = Lote.objects.all()
    context = {
        'lotes': lotes
    }
    return render(request, template_name, context)

def mostra_lote(request, id_lote):
    template_name = 'core/lote.html'
    lote = Lote.objects.get(id=id_lote)
    context = {
        'lotes': lote
    }

    return render(request, template_name, context)

def delete_lote(request, lote_id):
    lote = get_object_or_404(Lote, id=lote_id)
    lote.delete()
    return JsonResponse({'message': 'Lote excluído com sucesso.'})

def adicionar_lote(request):
    if request.method == 'POST':
        serializer = LoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'Lote adicionado com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_lote(request, pk):
    lote = get_object_or_404(Lote, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LoteSerializer(lote, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Lote editado com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = LoteForm(instance=lote)

    return render(request, 'editar_lote.html', {'form': form, 'lote': lote})

#RAÇA
def lista_racas(request):
    template_name = 'core/racas.html'
    racas = Raca.objects.all()
    context = {
        'racas': racas
    }
    return render(request, template_name, context)

def mostra_raca(request, id_raca):
    template_name = 'core/raca.html'
    raca = Raca.objects.get(id=id_raca)
    context = {
        'racas': raca
    }

    return render(request, template_name, context)

def delete_raca(request, raca_id):
    raca = get_object_or_404(Raca, id=raca_id)
    raca.delete()
    return JsonResponse({'message': 'Raca excluído com sucesso.'})

def adicionar_raca(request):
    if request.method == 'POST':
        serializer = RacaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'Raca adicionado com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_raca(request, pk):
    raca = get_object_or_404(Raca, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RacaSerializer(raca, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Raca editada com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = RacaForm(instance=raca)

    return render(request, 'editar_raca.html', {'form': form, 'raca': raca})

#VETERINARIO
def lista_veterinarios(request):
    template_name = 'core/veterinarios.html'
    veterinarios = Veterinario.objects.all()
    context = {
        'veterinarios': veterinarios
    }
    return render(request, template_name, context)

def mostra_veterinario(request, id_veterinario):
    template_name = 'core/veterinario.html'
    veterinario = Veterinario.objects.get(id=id_veterinario)
    context = {
        'veterinarios': veterinario
    }

    return render(request, template_name, context)

def delete_veterinario(request, veterinario_id):
    veterinario = get_object_or_404(Veterinario, id=veterinario_id)
    veterinario.delete()
    return JsonResponse({'message': 'Veterinario excluído com sucesso.'})

def adicionar_veterinario(request):
    if request.method == 'POST':
        serializer = VeterinarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'Veterinario adicionado com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_veterinario(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VeterinarioSerializer(veterinario, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Veterinario editado com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = VeterinarioForm(instance=veterinario)

    return render(request, 'editar_veterinario.html', {'form': form, 'veterinario': veterinario})

#PRODUTOS SANITARIOS
def lista_prodSanitarios(request):
    template_name = 'core/prodSanitarios.html'
    prodSanitarios = ProdSanitario.objects.all()
    context = {
        'prodSanitarios': prodSanitarios
    }
    return render(request, template_name, context)

def mostra_prodSanitario(request, id_prodSanitario):
    template_name = 'core/prodSanitario.html'
    prodSanitario = ProdSanitario.objects.get(id=id_prodSanitario)
    context = {
        'prodSanitarios': prodSanitario
    }

    return render(request, template_name, context)

def delete_prodSanitario(request, prodSanitario_id):
    prodSanitario = get_object_or_404(ProdSanitario, id=prodSanitario_id)
    prodSanitario.delete()
    return JsonResponse({'message': 'ProdSanitario excluído com sucesso.'})

def adicionar_prodSanitario(request):
    if request.method == 'POST':
        serializer = ProdSanitarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'ProdSanitario adicionado com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_prodSanitario(request, pk):
    prodSanitario = get_object_or_404(ProdSanitario, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProdSanitarioSerializer(prodSanitario, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'ProdSanitario editado com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = ProdSanitarioForm(instance=prodSanitario)

    return render(request, 'editar_prodSanitario.html', {'form': form, 'prodSanitario': prodSanitario})

#VENDAS
def lista_vendas(request):
    template_name = 'core/vendas.html'
    vendas = Venda.objects.all()
    context = {
        'vendas': vendas
    }
    return render(request, template_name, context)

def mostra_venda(request, id_venda):
    template_name = 'core/venda.html'
    venda = Venda.objects.get(id=id_venda)
    context = {
        'vendas': venda
    }

    return render(request, template_name, context)

def delete_venda(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    venda.delete()
    return JsonResponse({'message': 'Venda excluído com sucesso.'})

def adicionar_venda(request):
    if request.method == 'POST':
        serializer = VendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'Venda adicionado com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VendaSerializer(venda, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Venda editado com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = VendaForm(instance=venda)

    return render(request, 'editar_venda.html', {'form': form, 'venda': venda})

#COMPRAR ANIMAL
def lista_comprarAnimais(request):
    template_name = 'core/comprarAnimais.html'
    comprarAnimais = ComprarAnimal.objects.all()
    context = {
        'comprarAnimais': comprarAnimais
    }
    return render(request, template_name, context)

def mostra_comprarAnimal(request, id_comprarAnimal):
    template_name = 'core/comprarAnimal.html'
    comprarAnimal = ComprarAnimal.objects.get(id=id_comprarAnimal)
    context = {
        'comprarAnimais': comprarAnimal
    }

    return render(request, template_name, context)

def delete_comprarAnimal(request, comprarAnimal_id):
    comprarAnimal = get_object_or_404(ComprarAnimal, id=comprarAnimal_id)
    comprarAnimal.delete()
    return JsonResponse({'message': 'ComprarAnimal excluído com sucesso.'})

def adicionar_comprarAnimal(request):
    if request.method == 'POST':
        serializer = ComprarAnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'ComprarAnimal adicionado com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_comprarAnimal(request, pk):
    comprarAnimal = get_object_or_404(ComprarAnimal, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ComprarAnimalSerializer(comprarAnimal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'ComprarAnimal editado com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = ComprarAnimalForm(instance=comprarAnimal)

    return render(request, 'editar_comprarAnimal.html', {'form': form, 'comprarAnimal': comprarAnimal})

#APLICAR PRODUTOS SANITARIOS
def lista_aplicarProdutosSanitarios(request):
    template_name = 'core/aplicarProdutosSanitarios.html'
    aplicarProdutosSanitarios = AplicarProdutoSanitario.objects.all()
    context = {
        'aplicarProdutosSanitarios': aplicarProdutosSanitarios
    }
    return render(request, template_name, context)

def mostra_aplicarProdutoSanitario(request, id_aplicarProdutoSanitario):
    template_name = 'core/aplicarProdutoSanitario.html'
    aplicarProdutoSanitario = AplicarProdutoSanitario.objects.get(id=id_aplicarProdutoSanitario)
    context = {
        'aplicarProdutosSanitarios': aplicarProdutoSanitario
    }

    return render(request, template_name, context)

def delete_aplicarProdutoSanitario(request, aplicarProdutoSanitario_id):
    aplicarProdutoSanitario = get_object_or_404(AplicarProdutoSanitario, id=aplicarProdutoSanitario_id)
    aplicarProdutoSanitario.delete()
    return JsonResponse({'message': 'AplicarProdutoSanitario excluído com sucesso.'})

def adicionar_aplicarProdutoSanitario(request):
    if request.method == 'POST':
        serializer = AplicarProdutoSanitarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'AplicarProdutoSanitario adicionado com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_aplicarProdutoSanitario(request, pk):
    aplicarProdutoSanitario = get_object_or_404(AplicarProdutoSanitario, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AplicarProdutoSanitarioSerializer(aplicarProdutoSanitario, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'AplicarProdutoSanitario editado com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = AplicarProdutoSanitarioForm(instance=aplicarProdutoSanitario)

    return render(request, 'editar_aplicarProdutoSanitario.html', {'form': form, 'aplicarProdutoSanitario': aplicarProdutoSanitario})


#OCORRENCIAS
def lista_ocorrencias(request):
    template_name = 'core/ocorrencias.html'
    ocorrencias = Ocorrencias.objects.all()
    context = {
        'ocorrencias': ocorrencias
    }
    return render(request, template_name, context)

def mostra_ocorrencia(request, id_ocorrencia):
    template_name = 'core/ocorrencia.html'
    ocorrencia = Ocorrencias.objects.get(id=id_ocorrencia)
    context = {
        'ocorrencias': ocorrencia
    }

    return render(request, template_name, context)

def delete_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencias, id=ocorrencia_id)
    ocorrencia.delete()
    return JsonResponse({'message': 'Ocorrência excluída com sucesso.'})

def adicionar_ocorrencia(request):
    if request.method == 'POST':
        serializer = OcorrenciasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'Ocorrencia adicionada com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_ocorrencia(request, pk):
    ocorrencia = get_object_or_404(Ocorrencias, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OcorrenciasSerializer(ocorrencia, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Ocorrencia editada com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = OcorrenciasForm(instance=ocorrencia)

    return render(request, 'editar_ocorrencia.html', {'form': form, 'ocorrencia': ocorrencia})

#INSEMINAÇÃO
def lista_inseminacoes(request):
    template_name = 'core/inseminacoes.html'
    inseminacoes = Inseminacoes.objects.all()
    context = {
        'inseminacoes': inseminacoes
    }
    return render(request, template_name, context)

def mostra_inseminacao(request, id_inseminacao):
    template_name = 'core/inseminacao.html'
    inseminacao = Inseminacoes.objects.get(id=id_inseminacao)
    context = {
        'inseminacoes': inseminacao
    }

    return render(request, template_name, context)

def delete_inseminacao(request, inseminacao_id):
    inseminacao = get_object_or_404(Inseminacao, id=inseminacao_id)
    inseminacao.delete()
    return JsonResponse({'message': 'Inseminação excluída com sucesso.'})

def adicionar_inseminacao(request):
    if request.method == 'POST':
        serializer = InseminacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'Inseminacao adicionada com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_inseminacao(request, pk):
    inseminacao = get_object_or_404(Inseminacao, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InseminacaoSerializer(inseminacao, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Inseminacao editada com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = InseminacaoForm(instance=inseminacao)

    return render(request, 'editar_inseminacao.html', {'form': form, 'inseminacao': inseminacao})

#MOVIMENTAÇÕES
def lista_movimentacoes(request):
    template_name = 'core/movimentacoes.html'
    movimentacoes = Movimentacoes.objects.all()
    context = {
        'movimentacoes': movimentacoes
    }
    return render(request, template_name, context)

def mostra_movimentacao(request, id_movimentacao):
    template_name = 'core/movimentacao.html'
    movimentacao = Movimentacoes.objects.get(id=id_movimentacao)
    context = {
        'movimentacoes': movimentacao
    }

    return render(request, template_name, context)

def delete_movimentacao(request, movimentacao_id):
    movimentacao = get_object_or_404(Movimentacao, id=movimentacao_id)
    movimentacao.delete()
    return JsonResponse({'message': 'Movimentação excluída com sucesso.'})

def adicionar_movimentacao(request):
    if request.method == 'POST':
        serializer = MovimentacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'movimentacao adicionada com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_movimentacao(request, pk):
    movimentacao = get_object_or_404(Movimentacao, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MovimentacaoSerializer(movimentacao, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'movimentacao editada com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = movimentacaoForm(instance=movimentacao)

    return render(request, 'editar_movimentacao.html', {'form': form, 'movimentacao': movimentacao})

#PRODUTO ALIMENTICIO
def lista_produtosAlimenticios(request):
    template_name = 'core/produtosAlimenticios.html'
    produtosAlimenticios = ProdutosAlimenticios.objects.all()
    context = {
        'produtosAlimenticios': produtosAlimenticios
    }
    return render(request, template_name, context)

def mostra_produtoAlimenticio(request, id_produtoAlimenticio):
    template_name = 'core/produtoAlimenticio.html'
    produtoAlimenticio = ProdutosAlimenticios.objects.get(id=id_produtoAlimenticio)
    context = {
        'produtosAlimenticios': produtoAlimenticio
    }

    return render(request, template_name, context)

def delete_produtoAlimenticio(request, produtoAlimenticio_id):
    produtoAlimenticio = get_object_or_404(ProdutoAlimenticio, id=produtoAlimenticio_id)
    produtoAlimenticio.delete()
    return JsonResponse({'message': 'Produto Alimenticio excluída com sucesso.'})

def adicionar_produtoAlimenticio(request):
    if request.method == 'POST':
        serializer = ProdutoAlimenticioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'produtoAlimenticio adicionada com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_produtoAlimenticio(request, pk):
    produtoAlimenticio = get_object_or_404(ProdutoAlimenticio, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProdutoAlimenticioSerializer(produtoAlimenticio, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'produtoAlimenticio editada com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = ProdutoAlimenticioForm(instance=produtoAlimenticio)

    return render(request, 'editar_produtoAlimenticio.html', {'form': form, 'produtoAlimenticio': produtoAlimenticio})

#SUPLEMENTAÇÕES
def lista_suplementacoes(request):
    template_name = 'core/suplementacoes.html'
    suplementacoes = Suplementacoes.objects.all()
    context = {
        'suplementacoes': suplementacoes
    }
    return render(request, template_name, context)

def mostra_suplementacao(request, id_suplementacao):
    template_name = 'core/suplementacao.html'
    suplementacao = Suplementacoes.objects.get(id=id_suplementacao)
    context = {
        'suplementacoes': suplementacao
    }

    return render(request, template_name, context)

def delete_suplementacao(request, suplementacao_id):
    suplementacao = get_object_or_404(Suplementacao, id=suplementacao_id)
    suplementacao.delete()
    return JsonResponse({'message': 'Suplementação excluída com sucesso.'})

def adicionar_suplementacao(request):
    if request.method == 'POST':
        serializer = SuplementacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'Suplementação adicionada com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_suplementacao(request, pk):
    suplementacao = get_object_or_404(Suplementacao, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SuplementacaoSerializer(suplementacao, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Suplementação editada com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = SuplementacaoForm(instance=suplementacao)

    return render(request, 'editar_suplementacao.html', {'form': form, 'suplementacao': suplementacao})

#PESAGEM
def lista_pesagens(request):
    template_name = 'core/pesagens.html'
    pesagens = Pesagens.objects.all()
    context = {
        'pesagens': pesagens
    }
    return render(request, template_name, context)

def mostra_pesagem(request, id_pesagem):
    template_name = 'core/pesagem.html'
    pesagem = Pesagens.objects.get(id=id_pesagem)
    context = {
        'pesagens': pesagem
    }

    return render(request, template_name, context)

def delete_pesagem(request, pesagem_id):
    pesagem = get_object_or_404(Pesagem, id=pesagem_id)
    pesagem.delete()
    return JsonResponse({'message': 'Pesagem excluída com sucesso.'})

def adicionar_pesagem(request):
    if request.method == 'POST':
        serializer = PesagemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'Pesagem adicionada com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_pesagem(request, pk):
    pesagem = get_object_or_404(Pesagem, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PesagemSerializer(pesagem, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Pesagem editada com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = PesagemForm(instance=pesagem)

    return render(request, 'editar_pesagem.html', {'form': form, 'pesagem': pesagem})

#OUTRAS DESPESAS
def lista_outrasDespesas(request):
    template_name = 'core/outrasDespesas.html'
    outrasDespesas = OutrasDespesas.objects.all()
    context = {
        'outrasDespesas': outrasDespesas
    }
    return render(request, template_name, context)

def mostra_outraDespesa(request, id_outraDespesa):
    template_name = 'core/outraDespesa.html'
    outraDespesa = outrasDespesas.objects.get(id=id_outraDespesa)
    context = {
        'outrasDespesas': outraDespesa
    }

    return render(request, template_name, context)

def delete_outraDespesa(request, outraDespesa_id):
    outraDespesa = get_object_or_404(OutraDespesa, id=outraDespesa_id)
    outraDespesa.delete()
    return JsonResponse({'message': 'OutraDespesa excluída com sucesso.'})

def adicionar_outraDespesa(request):
    if request.method == 'POST':
        serializer = OutraDespesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'OutraDespesa adicionada com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_outraDespesa(request, pk):
    outraDespesa = get_object_or_404(OutraDespesa, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OutraDespesaSerializer(outraDespesa, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'OutraDespesa editada com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = OutraDespesaForm(instance=outraDespesa)

    return render(request, 'editar_outraDespesa.html', {'form': form, 'outraDespesa': outraDespesa})

#COMPRA PRODUTOS
def lista_compraProdutos(request):
    template_name = 'core/compraProdutos.html'
    compraProdutos = compraProdutos.objects.all()
    context = {
        'compraProdutos': compraProdutos
    }
    return render(request, template_name, context)

def mostra_compraProdutos(request, id_outraDespesa):
    template_name = 'core/compraProduto.html'
    compraProduto = compraProdutos.objects.get(id=id_compraProduto)
    context = {
        'compraProdutos': compraProduto
    }

    return render(request, template_name, context)

def delete_compraProduto(request, compraProduto_id):
    compraProduto = get_object_or_404(CompraProdutos, id=compraProduto_id)
    compraProduto.delete()
    return JsonResponse({'message': 'Compra do produto excluída com sucesso.'})

def adicionar_compraProduto(request):
    if request.method == 'POST':
        serializer = CompraProdutosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'mensagem': 'Compra de produto adicionada com sucesso.'}, status=201)
            return JsonResponse(serializer.errors, status=400)
            return JsonResponse({'mensagem': 'Método não permitido.'}, status=405)

@csrf_exempt
def editar_compraProduto(request, pk):
    compraProduto = get_object_or_404(CompraProdutos, pk=pk)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CompraProdutosSerializer(compraProduto, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Compra de produto editada com sucesso.'})
        else:
            return JsonResponse({'error': serializer.errors}, status=400)
    else:
        form = CompraProdutosForm(instance=compraProduto)

    return render(request, 'editar_compraProduto.html', {'form': form, 'compraProduto': compraProduto})


#####api#####
class ProdutorRuralList(generics.ListCreateAPIView):
    queryset = ProdutorRural.objects.all()
    serializer_class = ProdutorRuralSerializer

class PropriedadeRuralList(generics.ListCreateAPIView):
    queryset = PropriedadeRural.objects.all()
    serializer_class = PropriedadeRuralSerializer

class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class LoteList(generics.ListCreateAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

class RacaList(generics.ListCreateAPIView):
    queryset = Raca.objects.all()
    serializer_class = RacaSerializer

class VeterinarioList(generics.ListCreateAPIView):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer

class ProdSanitarioList(generics.ListCreateAPIView):
    queryset = ProdSanitario.objects.all()
    serializer_class = ProdSanitarioSerializer

class VendaList(generics.ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class ComprarAnimalList(generics.ListCreateAPIView):
    queryset = ComprarAnimal.objects.all()
    serializer_class = ComprarAnimalSerializer

class OcorrenciasList(generics.ListCreateAPIView):
    queryset = Ocorrencias.objects.all()
    serializer_class = OcorrenciasSerializer

class InseminacaoList(generics.ListCreateAPIView):
    queryset = Inseminacao.objects.all()
    serializer_class = InseminacaoSerializer

class MovimentacaoList(generics.ListCreateAPIView):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer

class ProdutoAlimenticioList(generics.ListCreateAPIView):
    queryset = ProdutoAlimenticio.objects.all()
    serializer_class = ProdutoAlimenticioSerializer


class SuplementacaoList(generics.ListCreateAPIView):
    queryset = Suplementacao.objects.all()
    serializer_class = SuplementacaoSerializer

class PesagemList(generics.ListCreateAPIView):
    queryset = Pesagem.objects.all()
    serializer_class = PesagemSerializer

class OutraDespesaList(generics.ListCreateAPIView):
    queryset = OutraDespesa.objects.all()
    serializer_class = OutraDespesaSerializer

class AplicarProdutoSanitarioList(generics.ListCreateAPIView):
    queryset = AplicarProdutoSanitario.objects.all()
    serializer_class = AplicarProdutoSanitarioSerializer

class CompraProdutosList(generics.ListCreateAPIView):
    queryset = CompraProdutos.objects.all()
    serializer_class = CompraProdutosSerializer