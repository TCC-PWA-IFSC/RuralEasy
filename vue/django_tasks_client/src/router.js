//import Vue from 'vue'
//import * as Vue from 'vue';
//import Router from 'vue-router'
import PropriedadesComponent from './components/propriedades-component.vue';
import LotesComponent from './components/lotes-component.vue';
import RacasComponent from './components/racas-component.vue';
import OcorrenciasComponent from './components/ocorrencias-component.vue'
import VeterinarioComponent from './components/veterinario-component.vue'
import ProdSanitariosComponent from './components/prodSanitarios-component.vue'
import VendasComponent from './components/vendas-component.vue'
import InseminacoesComponent from './components/inseminacoes-component.vue'
import AnimaisComponent from './components/animais-component.vue'
import ProdutoresComponent from './components/produtor-component.vue'
import MovimentacoesComponent from './components/movimentacoes-component.vue'
import ProdutosAlimenticiosComponent from './components/produtoAlimenticio-component.vue'
import ComprarAnimaisComponent from './components/comprarAnimais-component.vue'
import SuplementacoesComponent from './components/suplementacao-component.vue'
import PesagensComponent from './components/pesagens-component.vue'
import LoginComponent from './components/Login-component.vue'
import OutrasDespesasComponent from './components/outrasDespesas-component.vue'
import ReceitasComponent from './components/receitas-component.vue'
import DespesasComponent from './components/despesas-component.vue'
import AplicarProdutosSanitariosComponent from './components/aplicarProdutosSanitarios-component.vue'
import CompraProdutosComponent from './components/compraProdutos-component.vue'
import { createRouter, createWebHistory } from 'vue-router';

//Vue.use(Router);

const routes = [

  //{ path: '/:pathMatch(.*)*', redirect: '/' },
  /*{
    path: '/service-worker.js',
    beforeEnter() { location.replace('/service-worker.js') }
  },*/
  {
    path: '/',
    redirect: '/produtores'
  },
  {
    path: '/outrasdespesas',
    name: 'OutraDespesaList',
    //component: PropriedadeRuralList
    component: OutrasDespesasComponent,
    //meta: { requiresAuth: true }
  },
  {
    path: '/despesas',
    name: 'DespesaList',
    //component: PropriedadeRuralList
    component: DespesasComponent,
    //meta: { requiresAuth: true }
  },
  {
    path: '/aplicarProdutosSanitarios',
    name: 'AplicarProdutoSanitarioList',
    //component: PropriedadeRuralList
    component: AplicarProdutosSanitariosComponent,
    //meta: { requiresAuth: true }
  },
  {
    path: '/receitas',
    name: 'ReceitasList',
    //component: PropriedadeRuralList
    component: ReceitasComponent,
    //meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'LoginList',
    //component: PropriedadeRuralList
    component: LoginComponent
  },
  {
    path: '/suplementacoes',
    name: 'SuplementacaoList',
    //component: PropriedadeRuralList
    component: SuplementacoesComponent
  },
  {
    path: '/comprarAnimais',
    name: 'ComprarAnimaisList',
    //component: PropriedadeRuralList
    component: ComprarAnimaisComponent
  },
  {
    path: '/propriedades',
    name: 'PropriedadeRuralList',
    //component: PropriedadeRuralList
    component: PropriedadesComponent
  },
  {
    path: '/produtores',
    name: 'ProdutorRuralList',
    //component: PropriedadeRuralList
    component: ProdutoresComponent
  },
  {
    path: '/lotes',
    name: 'LoteList',
    //component: PropriedadeRuralList
    component: LotesComponent
  },
  {
    path: '/racas',
    name: 'RacaList',
    //component: PropriedadeRuralList
    component: RacasComponent
  },
  {
    path: '/ocorrencias',
    name: 'OcorrenciasList',
    //component: PropriedadeRuralList
    component: OcorrenciasComponent
  },
  {
    path: '/veterinario',
    name: 'VeterinarioList',
    //component: PropriedadeRuralList
    component: VeterinarioComponent
  },
  {
    path: '/prodSanitarios',
    name: 'ProdSanitariosList',
    //component: PropriedadeRuralList
    component: ProdSanitariosComponent
  },
  {
    path: '/vendas',
    name: 'VendasList',
    //component: PropriedadeRuralList
    component: VendasComponent
  },
  {
    path: '/inseminacoes',
    name: 'InseminacoesList',
    //component: PropriedadeRuralList
    component: InseminacoesComponent
  },
  {
    path: '/movimentacoes',
    name: 'MovimentacoesList',
    //component: PropriedadeRuralList
    component: MovimentacoesComponent
  },
  {
    path: '/animais',
    name: 'AnimaisList',
    //component: PropriedadeRuralList
    component: AnimaisComponent
  },
  {
    path: '/produtosAlimenticios',
    name: 'ProdutosAlimenticiosList',
    //component: PropriedadeRuralList
    component: ProdutosAlimenticiosComponent
  },
  {
    path: '/pesagens',
    name: 'PesagemList',
    //component: PropriedadeRuralList
    component: PesagensComponent
  },
  {
    path: '/compraProdutos',
    name: 'CompraProdutosList',
    //component: PropriedadeRuralList
    component: CompraProdutosComponent
  }

]

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth) && !localStorage.getItem('access_token')) {
      next('/login');
  } else {
      next();
  }
});

export default router;