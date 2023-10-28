<template>
    <div class="container">
      <h2>Cadastro de Suplementação</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="kgConsumoSuplementacao">KG de consumo:</label>
          <input type="kgConsumoSuplementacao" id="kgConsumoSuplementacao" v-model="suplementacao.kgConsumoSuplementacao" required>
        </div>
	<div>
          <label for="dataAplicacaoSuplementacao">Data da aplicação:</label>
          <input type="date" id="dataAplicacaoSuplementacao" v-model="suplementacao.dataAplicacaoSuplementacao" required>
        </div>
	<div>
        <label for="idLoteSuplAplicado">Lote:</label>
          <select id="idLoteSuplAplicado" v-model="suplementacao.idLoteSuplAplicado" required>
            <option value="">Selecione um lote</option>
            <option v-for="idLoteSuplAplicado in lotes" :value="idLoteSuplAplicado.id" :key="idLoteSuplAplicado.id">{{ idLoteSuplAplicado.nomeLote }}</option>
          </select>
        </div>
	<div>
        <label for="idProdutoAlimenticio">Produto Alimenticio</label>
          <select id="idProdutoAlimenticio" v-model="suplementacao.idProdutoAlimenticio" required>
            <option value="">Selecione um produto</option>
            <option v-for="idProdutoAlimenticio in produtosAlimenticios" :value="idProdutoAlimenticio.id" :key="idProdutoAlimenticio.id">{{ idProdutoAlimenticio.nomeProdutoAlimenticio }}</option>
          </select>
        </div>
        <button type="submit">Salvar</button>
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>
  <br>

  <div class="table">
  <h1>Lista de Suplementaçoes</h1>
  <table>
    <thead>
      <tr>
        <th>KG de Consumo</th>
        <th>Data da aplicação</th>
        <th>Lote</th>
        <th>Produto alimenticio</th>
        <th>Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="suplementacao in suplementacoes" :key="suplementacao.id">
        <td>{{ suplementacao.kgConsumoSuplementacao }}</td>
        <td>{{ suplementacao.dataAplicacaoSuplementacao }}</td>
        <td>{{ getLoteById(suplementacao.idLoteSuplAplicado) }}</td>
        <td>{{ getProdutoAlimenticioById(suplementacao.idProdutoAlimenticio) }}</td>
        <td>
          <button @click.prevent="editSuplementacao(suplementacao)">Editar</button>
          <button @click.prevent="confirmDelete(suplementacao)">Excluir</button>
        </td>
      </tr>
    </tbody>
  </table>
</div>


  </template>
  
  <script>
  import axios from 'axios'
  
  axios.defaults.xsrfCookieName = 'csrftoken';
  axios.defaults.xsrfHeaderName = 'X-CSRFToken';
  
  export default {
    data() {
      return {
        suplementacao: {
          kgConsumoSuplementacao: '',
          dataAplicacaoSuplementacao: '',
          idLoteSuplAplicado: '',
          idProdutoAlimenticio: ''
        },
        suplementacoes: [],
        lotes: [],
        produtosAlimenticios: [],
        isEdit: false,
        showDeleteModal: false,
        suplementacaoToDelete: null
      }
    },

    methods: {

    getLoteById(id) {
    // Procura o lote com base no ID
    let lote = this.lotes.find(l => l.id === id);
    // Retorna o nome do lote se encontrado; caso contrário, retorna uma string vazia
    return lote ? lote.nomeLote : '';
  },

  getProdutoAlimenticioById(id) {
    // Procura o produto alimentício com base no ID
    let produtoAlimenticio = this.produtosAlimenticios.find(p => p.id === id);
    // Retorna o nome do produto alimentício se encontrado; caso contrário, retorna uma string vazia
    return produtoAlimenticio ? produtoAlimenticio.nomeProdutoAlimenticio : '';
  },
  
       //editar 
  editSuplementacao(suplementacao) {
    this.isEdit = true;
    this.suplementacao = { ...suplementacao };
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      axios.put(`http://localhost:8000/suplementacoes/editar/${this.suplementacao.id}/`, this.suplementacao)
        .then(response => {
          this.suplementacoes = response.data;
          this.isEdit = false;
          this.suplementacao = {
            kgConsumoSuplementacao: '',
            dataAplicacaoSuplementacao: '',
            idLoteSuplAplicado: 'this.lote.idLote',
            idProdutoAlimenticio: 'this.produtoAlimenticio.id'
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      axios.post('http://localhost:8000/suplementacoes/', this.suplementacao)
        .then(response => {
          this.suplementacoes = response.data;
          this.suplementacao = {
            kgConsumoSuplementacao: '',
            dataAplicacaoSuplementacao: '',
            idLoteSuplAplicado: 'this.lote.idLote',
            idProdutoAlimenticio: 'this.produtoAlimenticio.id'
          };
        })
        .catch(error => {
          console.log(error);
        });
    }
    setTimeout(function() {
      location.reload();
    }, 1000);
  },
  
      deleteSuplementacao() {
        axios.delete(`http://localhost:8000/suplementacoes/deletesuplementacao/${this.suplementacao.id}/`)
          .then(response => {
            this.suplementacoes = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      //confirmDelete(propriedade) {
      //  console.log("Que tem aqui?", propriedade)
      //  this.showDeleteModal = true
      //  this.propriedadeToDelete = propriedade
      //}
      confirmDelete(suplementacao) {
        if (window.confirm("Você tem certeza de que deseja excluir esta suplementacao?")) {
          this.suplementacaoToDelete = suplementacao;
          this.deleteSuplementacaoConfirmed();
        }
      },
      deleteSuplementacaoConfirmed() {
        axios.delete(`http://localhost:8000/suplementacoes/deletesuplementacao/${this.suplementacaoToDelete.id}/`)
          .then(response => {
            this.suplementacoes = response.data
            this.showDeleteModal = false
          })
          .catch(error => {
            console.log(error)
          })
          setTimeout(function() {
      location.reload();
      }, 1000);
      },
      cancelDelete() {
        this.showDeleteModal = false
      },
      cancelEdit() {
        window.location.href = '/suplementacoes'
      },
      fetchSuplementacao(id) {
        axios.get(`http://localhost:8000/suplementacoes/${id}/`)
          .then(response => {
            this.suplementacao = response.data;
          })
          .catch(error => {
            console.log(error);
          })
      }
    },
    /*mounted() {
      const urlParams = new URLSearchParams(window.location.search);
      const id = urlParams.get('id');
      if (id) {
        this.isEdit = true
        this.fetchProdutor(id)
      }
    }*/
    
    mounted() {
	axios.get('http://localhost:8000/suplementacoes/')
        .then(response => {
          this.suplementacoes = response.data
        })
        .catch(error => {
          console.log(error)
        })
      axios.get('http://localhost:8000/produtosAlimenticios/')
        .then(response => {
          this.produtosAlimenticios = response.data
        })
        .catch(error => {
          console.log(error)
        })
      axios.get('http://localhost:8000/lotes/')
        .then(response => {
          this.lotes = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }

  }
  </script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');

/* Base para aplicar a fonte em todo o componente */
.container {
    font-family: 'Poppins', sans-serif;
    text-align: center;
}

button {
    padding: 10px 20px;
    margin-right: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s;
    background-color: #28a745; /* verde */
    color: #FFF;
    font-weight: 500;
    box-shadow: 0 2px 8px rgba(40, 167, 69, 0.1); /* verde */

    &:hover {
        background-color: #218838; /* verde escuro */
        box-shadow: 0 4px 12px rgba(33, 136, 56, 0.2); /* verde escuro */
    }
}

div {
    justify-content: center;
}

.botaoConfirmaDelete {
    /* ... estilos existentes ... */
    background-color: rgba(0,0,0,0.7);
    color: #FFF;
}

.buttons-container {
    /* ... estilos existentes ... */
    padding: 20px;
}

h1 {
    justify-content: center;
    text-align: center;
    color: #333;
    font-weight: 600;
    
}

table {
    /* ... estilos existentes ... */
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    width: 100%;
}

.table {
    width: 90%; /* Isso limita a tabela a 90% da largura do viewport, mas você pode ajustar conforme preferir */
    margin: 0 auto; /* Isso centraliza a div da tabela */
}

th, td {
    /* ... estilos existentes ... */
    font-weight: 400;
}

th {
    background-color: #28a745; /* verde */
    color: #FFF;
}

tr:nth-child(odd) {
    background-color: #e6f4ea; /* verde claro */
}

tr:hover {
    background-color: #d1ecd5; /* verde mais claro */
}

.container {
    /* ... estilos existentes ... */
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    background-color: #FFF;
}

form, .table, .botaoConfirmaDelete {
    display: inline-block;
    width: 100%;
    text-align: center;
}


h1, h2 {
    width: 100%;
}

</style>
