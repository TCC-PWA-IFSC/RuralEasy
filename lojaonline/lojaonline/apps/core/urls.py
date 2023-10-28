from django.urls import path
from core import views
from .views import ProdutorRuralList, PropriedadeRuralList, delete_produtor, delete_propriedade, LoteList, RacaList, AnimalList, delete_lote, delete_animal, delete_raca, VeterinarioList, delete_veterinario, ProdSanitarioList, delete_prodSanitario, VendaList, delete_venda, ComprarAnimalList, delete_comprarAnimal, OcorrenciasList, delete_ocorrencia, InseminacaoList, delete_inseminacao, MovimentacaoList, delete_movimentacao, ProdutoAlimenticioList, delete_produtoAlimenticio, SuplementacaoList, delete_suplementacao, PesagemList, delete_pesagem, OutraDespesaList, delete_outraDespesa, AplicarProdutoSanitarioList, delete_aplicarProdutoSanitario, CompraProdutosList, delete_compraProduto

app_name= 'core'

urlpatterns = [
    #PRODUTOR
    #path('produtores/', views.lista_produtores, name='produtores'),
    path('produtores/produtor/<int:id_produtor>/',views.mostra_produtor,name='mostra_produtor'),
    #path('propriedades/',views.lista_propriedades, name='lista_propriedades'),
    path('produtores/deleteprodutor/<int:produtor_id>/', delete_produtor, name='delete_produtor'),
    path('produtores/adicionarprodutor/<JsonResponse>/', views.adicionar_produtor, name='adicionar_produtor'),
    #path('produtores/<int:pk>/editar/', views.editar_produtor, name='editar_produtor'),
    #path('produtores/editar/<JsonResponse>', views.editar_produtor, name='editar_produtor'),
    path('produtores/editar/<int:pk>/', views.editar_produtor, name='editar_produtor'),
    path('produtores/', ProdutorRuralList.as_view()),

    #PROPRIEDADE
    path('propriedades/', PropriedadeRuralList.as_view()),
    path('propriedades/propriedade/<int:id_propriedade>/',views.mostra_propriedade,name='mostra_propriedade'),
    path('propriedades/editar/<int:pk>/', views.editar_propriedade, name='editar_propriedade'),
    path('propriedades/deletepropriedade/<int:propriedade_id>/', delete_propriedade, name='delete_propriedade'),

    #LOTE
    path('lotes/', LoteList.as_view()),
    path('lotes/lote/<int:id_lote>/',views.mostra_lote,name='mostra_lote'),
    path('lotes/editar/<int:pk>/', views.editar_lote, name='editar_lote'),
    path('lotes/deletelote/<int:lote_id>/', delete_lote, name='delete_lote'),

    #RACA
    path('racas/', RacaList.as_view()),
    path('racas/raca/<int:id_raca>/',views.mostra_raca,name='mostra_raca'),
    path('racas/editar/<int:pk>/', views.editar_raca, name='editar_raca'),
    path('racas/deleteraca/<int:raca_id>/', delete_raca, name='delete_raca'),

    #ANIMAL
    path('animais/', AnimalList.as_view()),
    path('animais/animal/<int:id_animal>/',views.mostra_animal,name='mostra_animal'),
    path('animais/editar/<int:pk>/', views.editar_animal, name='editar_animal'),
    path('animais/deleteanimal/<int:animal_id>/', delete_animal, name='delete_animal'),

    #VETERINARIO
    path('veterinarios/', VeterinarioList.as_view()),
    path('veterinarios/veterinario/<int:id_veterinario>/',views.mostra_veterinario,name='mostra_veterinario'),
    path('veterinarios/editar/<int:pk>/', views.editar_veterinario, name='editar_veterinario'),
    path('veterinarios/deleteveterinario/<int:veterinario_id>/', delete_veterinario, name='delete_veterinario'),

    #PRODUTOS SANITARIOS
    path('prodSanitarios/', ProdSanitarioList.as_view()),
    path('prodSanitarios/prodSanitario/<int:id_prodSanitario>/',views.mostra_prodSanitario,name='mostra_prodSanitario'),
    path('prodSanitarios/editar/<int:pk>/', views.editar_prodSanitario, name='editar_prodSanitario'),
    path('prodSanitarios/deleteprodSanitario/<int:prodSanitario_id>/', delete_prodSanitario, name='delete_prodSanitario'),

    #VENDAS
    path('vendas/', VendaList.as_view()),
    path('vendas/venda/<int:id_venda>/',views.mostra_venda,name='mostra_venda'),
    path('vendas/editar/<int:pk>/', views.editar_venda, name='editar_venda'),
    path('vendas/deletevenda/<int:venda_id>/', delete_venda, name='delete_venda'),

    #COMPRAR ANIMAL
    path('comprarAnimais/', ComprarAnimalList.as_view()),
    path('comprarAnimais/comprarAnimal/<int:id_comprarAnimal>/',views.mostra_comprarAnimal,name='mostra_comprarAnimal'),
    path('comprarAnimais/editar/<int:pk>/', views.editar_comprarAnimal, name='editar_comprarAnimal'),
    path('comprarAnimais/deletecomprarAnimal/<int:comprarAnimal_id>/', delete_comprarAnimal, name='delete_comprarAnimal'),

    #OCORRENCIAS
    path('ocorrencias/', OcorrenciasList.as_view()),
    path('ocorrencias/ocorrencia/<int:id_ocorrencia>/',views.mostra_ocorrencia,name='mostra_ocorrencia'),
    path('ocorrencias/editar/<int:pk>/', views.editar_ocorrencia, name='editar_ocorrencia'),
    path('ocorrencias/deleteocorrencia/<int:ocorrencia_id>/', delete_ocorrencia, name='delete_ocorrencia'),

    #INSEMINAÇÃO
    path('inseminacoes/', InseminacaoList.as_view()),
    path('inseminacoes/inseminacao/<int:id_inseminacao>/',views.mostra_inseminacao,name='mostra_inseminacao'),
    path('inseminacoes/editar/<int:pk>/', views.editar_inseminacao, name='editar_inseminacao'),
    path('inseminacoes/deleteinseminacao/<int:inseminacao_id>/', delete_inseminacao, name='delete_inseminacao'),

    #MOVIMENTAÇÃO
    path('movimentacoes/', MovimentacaoList.as_view()),
    path('movimentacoes/movimentacao/<int:id_movimentacao>/',views.mostra_movimentacao,name='mostra_movimentacao'),
    path('movimentacoes/editar/<int:pk>/', views.editar_movimentacao, name='editar_movimentacao'),
    path('movimentacoes/deletemovimentacao/<int:movimentacao_id>/', delete_movimentacao, name='delete_movimentacao'),

    #PRODUTO ALIMENTICIO
    path('produtosAlimenticios/', ProdutoAlimenticioList.as_view()),
    path('produtosAlimenticios/produtoAlimenticio/<int:id_produtoAlimenticio>/',views.mostra_produtoAlimenticio,name='mostra_produtoAlimenticio'),
    path('produtosAlimenticios/editar/<int:pk>/', views.editar_produtoAlimenticio, name='editar_produtoAlimenticio'),
    path('produtosAlimenticios/deleteprodutoAlimenticio/<int:produtoAlimenticio_id>/', delete_produtoAlimenticio, name='delete_produtoAlimenticio'),

    #SUPLEMENTACOES
    path('suplementacoes/', SuplementacaoList.as_view()),
    path('suplementacoes/suplementacao/<int:id_suplementacao>/',views.mostra_suplementacao,name='mostra_suplementacao'),
    path('suplementacoes/editar/<int:pk>/', views.editar_suplementacao, name='editar_suplementacao'),
    path('suplementacoes/deletesuplementacao/<int:suplementacao_id>/', delete_suplementacao, name='delete_suplementacao'),

    #PESAGEM
    path('pesagens/', PesagemList.as_view()),
    path('pesagens/pesagem/<int:id_pesagem>/',views.mostra_pesagem,name='mostra_pesagem'),
    path('pesagens/editar/<int:pk>/', views.editar_pesagem, name='editar_pesagem'),
    path('pesagens/deletepesagem/<int:pesagem_id>/', delete_pesagem, name='delete_pesagem'),

    #OUTRAS DESPESAS
    path('outrasDespesas/', OutraDespesaList.as_view()),
    path('outrasDespesas/outraDespesa/<int:id_outraDespesa>/',views.mostra_outraDespesa,name='mostra_outraDespesa'),
    path('outrasDespesas/editar/<int:pk>/', views.editar_outraDespesa, name='editar_outraDespesa'),
    path('outrasDespesas/deleteoutraDespesa/<int:outraDespesa_id>/', delete_outraDespesa, name='delete_outraDespesa'),

    #APLICAR PRODUTOS SANITARIOS
    path('aplicarProdutosSanitarios/', AplicarProdutoSanitarioList.as_view()),
    path('aplicarProdutosSanitarios/aplicarProdutoSanitario/<int:id_aplicarProdutoSanitario>/',views.mostra_aplicarProdutoSanitario,name='mostra_aplicarProdutoSanitario'),
    path('aplicarProdutosSanitarios/editar/<int:pk>/', views.editar_aplicarProdutoSanitario, name='editar_aplicarProdutoSanitario'),
    path('aplicarProdutosSanitarios/deleteaplicarProdutoSanitario/<int:aplicarProdutoSanitario_id>/', delete_aplicarProdutoSanitario, name='delete_aplicarProdutoSanitario'),

    #COMPRA DE PRODUTOS
    path('compraProdutos/', CompraProdutosList.as_view()),
    path('compraProdutos/compraProduto/<int:id_compraProduto>/',views.mostra_compraProdutos,name='mostra_compraProdutos'),
    path('compraProdutos/editar/<int:pk>/', views.editar_compraProduto, name='editar_compraProdutos'),
    path('compraProdutos/deletecompraProduto/<int:compraProduto_id>/', delete_compraProduto, name='delete_compraProdutos'),


]