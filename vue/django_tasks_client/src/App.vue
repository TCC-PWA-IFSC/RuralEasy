<template>
  <meta name="viewport" content="width=device-width, initial-scale=1"> <!-- para ajustar em disp movel-->
 
  <div class="container-fluid h-100">

  <div :class="['app-container', showMobileMenu ? 'menu-open' : '']">

    <nav class="navbar navbar-expand-lg navbar-dark bg-success px-3">
      <!--MENU CELULAR-->
      <button @click="toggleMobileMenu" class="navbar-toggler" type="button" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
      <!--MENU CELULAR-->
      <a class="navbar-brand d-flex align-items-center">
        <img src="./assets/img/logo1.png" class="img-fluid mr-2" width="60" alt="RuralEasy">
        RuralEasy
      </a>
      <div class="navbar-text ml-auto d-flex align-items-center">
        <img src="./assets/img/user1.png" class="img-fluid mr-2" width="30" alt="User">
        <strong>User</strong>
      </div>
    </nav>

    <div class="row h-100">
      <aside :class="showMobileMenu ? 'show-menu' : 'hide-menu'" class="col-md-3 p-3 bg-light">
        <div :class="{show: showMobileMenu}" id="navbarNav">
    
        <div @click="toggleMenu('cadastrosBasicos')" class="menu-option">Cadastros Básicos</div>
        <div v-if="menus.cadastrosBasicos" class="submenu">
        
        <a href="#produtor">
          <div class="icon-text">
            <img src="./assets/img/farmer1.png" class="iconSideBar">
            <router-link to="/produtores">Produtor</router-link>
          </div>
        </a>

          <a href="#propriedades">
            <div class="icon-text">
              <img src="./assets/img/farm1.png" class="iconSideBar">
              <router-link to="/propriedades">Propriedades</router-link>
            </div>
          </a>

        <a href="#veterinario">
          <div class="icon-text">
            <img src="./assets/img/doctor1.png" class="iconSideBar">
            <router-link to="/veterinario">Veterinário</router-link>
          </div>
        </a>

        <a href="#racas">
          <div class="icon-text">
            <img src="./assets/img/cow1.png" class="iconSideBar">
            <router-link to="/racas">Raças</router-link>
          </div>
        </a>

      </div>

      <div @click="toggleMenu('registroAnimais')" class="menu-option">Registro de Animais</div>
      <div v-if="menus.registroAnimais" class="submenu">
        <a href="#animais">
          <div class="icon-text">
            <img src="./assets/img/animal1.png" class="iconSideBar">
            <router-link to="/animais">Animais</router-link>
          </div>
        </a>

        <a href="#ocorrencias">
          <div class="icon-text">
            <img src="./assets/img/ocurrences1.png" class="iconSideBar">
            <router-link to="/ocorrencias">Ocorrências</router-link>
          </div>
        </a>

        <a href="#movimentacoes">
          <div class="icon-text">
            <img src="./assets/img/cowmov1.png" class="iconSideBar">
            <router-link to="/movimentacoes">Movimentações de Animais</router-link>
          </div>
        </a>

        <a href="#lotes">
          <div class="icon-text">
            <img src="./assets/img/cerca1.png" class="iconSideBar">
            <router-link to="/lotes">Lotes</router-link>
          </div>
        </a>

        <a href="#compras">
          <div class="icon-text">
            <img src="./assets/img/buyanimal1.png" class="iconSideBar">
            <router-link to="/comprarAnimais">Compra de Animais</router-link>
          </div>
        </a>

        <a href="#vendas">
          <div class="icon-text">
            <img src="./assets/img/sellanimal1.png" class="iconSideBar">
            <router-link to="/vendas">Venda de Animais</router-link>
          </div>
        </a>


      </div>

      <div @click="toggleMenu('manejoAnimais')" class="menu-option">Manejo dos Animais</div>
      <div v-if="menus.manejoAnimais" class="submenu">

        <a href="#inseminacoes">
          <div class="icon-text">
            <img src="./assets/img/insemination1.png" class="iconSideBar">
            <router-link to="/inseminacoes">Inseminações</router-link>
          </div>
        </a>

        <a href="#suplementacoes">
          <div class="icon-text">
            <img src="./assets/img/supplement1.png" class="iconSideBar">
            <router-link to="/suplementacoes">Suplementações</router-link>
          </div>
        </a>

        <a href="#aplicarProdutosSanitarios">
          <div class="icon-text">
            <img src="./assets/img/sanitaryproduct.png" class="iconSideBar">
            <router-link to="/aplicarProdutosSanitarios">Aplicações Sanitárias</router-link>
          </div>
        </a>


        <a href="#prodSanitarios">
          <div class="icon-text">
            <img src="./assets/img/frasco.png" class="iconSideBar2">
            <router-link to="/prodSanitarios">Produtos Sanitários</router-link>
          </div>
        </a>

        <a href="#prodAlimenticios">
          <div class="icon-text">
            <img src="./assets/img/feedproducts.png" class="iconSideBar">
            <router-link to="/produtosAlimenticios">Produtos Alimentícios</router-link>
          </div>
        </a>

        <a href="#pesagens">
          <div class="icon-text">
            <img src="./assets/img/weighing.png" class="iconSideBar">
            <router-link to="/pesagens">Pesagens</router-link>
          </div>
        </a>

      </div>

      <div @click="toggleMenu('financeiro')" class="menu-option">Financeiro</div>
      <div v-if="menus.financeiro" class="submenu">

        <a href="#despesas">
          <div class="icon-text">
            <img src="./assets/img/expense.png" class="iconSideBar">
            <router-link to="/despesas">Despesas</router-link>
          </div>
        </a>

        <a href="#receitas">
          <div class="icon-text">
            <img src="./assets/img/revenue.png" class="iconSideBar">
            <router-link to="/receitas">Receitas</router-link>
          </div>
        </a>

        <a href="#compraProdutos">
          <div class="icon-text">
            <img src="./assets/img/shop.png" class="iconSideBar">
            <router-link to="/compraProdutos">Compras</router-link>
          </div>
        </a>

        <a href="#outrasdespesas">
          <div class="icon-text">
            <img src="./assets/img/bill1.png" class="iconSideBar">
            <router-link to="/outrasdespesas">Outras Despesas</router-link>
          </div>
        </a>
      </div>
    </div>
      </aside>
    

      <main class="col-md-9 p-3">
    <div class="inner-content">
        <router-view></router-view>
    </div>
</main>


    </div>

  </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menus: {
        cadastrosBasicos: false,
        registroAnimais: false,
        manejoAnimais: false,
        financeiro: false
      },
      showMobileMenu: false
    };
  },
  methods: {
    toggleMenu(menu) {
      this.menus[menu] = !this.menus[menu];
    },
    toggleMobileMenu() {
  this.showMobileMenu = !this.showMobileMenu;
    console.log(this.showMobileMenu);
  
  if (this.showMobileMenu) {
    this.menus = {
      cadastrosBasicos: false,
      registroAnimais: false,
      manejoAnimais: false,
      financeiro: false
    };
  }
}
  }
};
</script>

<style>
.menu-option, .submenu {
  margin: 0;
  padding: 0;
}

.inner-content {
  width: 100%;
  max-width: 800px; /* Ajuste este valor conforme o desejado */
  margin: 0 auto; /* Isso centraliza horizontalmente */
}

.menu-option {
  cursor: pointer;
  padding: 7px;
  background-color: #f1f1f1;
  
}

.submenu a {
  display: block;
  margin-bottom: 3px;
  
}

.iconSideBar {
  width: 20px;
  height: 20px;
  margin-right: 10px;
  justify-content: left;
}

.iconSideBar2 {
  width: 20px;
  height: 20px;
  margin-right: 10px;
  margin-left: 3px;
  justify-content: left;
}

html, body {
  height: 100%;
  margin: 0;
}

.container-fluid {
  height: 100%; 
}

.icon-text {
  display: flex;
  align-items: center;
  justify-content: left;
}

body aside {
    display: block; 
}

body aside.hide-menu {
    display: none; /* Esconde o menu */
}

@media (max-width: 992px) {
    aside {
        width: 100%;
        display: none; 
    }
    aside.show-menu {
        display: block;
    }
}

.navbar-toggler {
  display: block !important;
}

.row {
  display: flex;
  flex-wrap: nowrap;
  height: 100%;
}

main {
  flex-grow: 1;
  display: flex;
  align-items: center; /* centraliza verticalmente */
  justify-content: center; /* centraliza horizontalmente */
}

</style>
