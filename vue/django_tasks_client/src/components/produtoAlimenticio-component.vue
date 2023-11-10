<template>
    <div class="container">
      <h2>Cadastro de Produtos Alimentícios</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="nome">Nome</label>
          <input type="nome" id="nome" v-model="produtoAlimenticio.nome" required>
        </div>
        <div class="form-group">
          <label for="tipoProdutoAlimenticio">Tipo</label>
          <input type="tipoProdutoAlimenticio" id="tipoProdutoAlimenticio" v-model="produtoAlimenticio.tipoProdutoAlimenticio" required>
        </div>
        <button type="submit">Salvar</button>
        <button v-if="isEdit" @click.prevent="deleteProdutoAlimenticio">Excluir</button>
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>

    <div class="table">
      <h1>Lista de Produtos Alimentícios</h1>
      <table>
    <thead>
      <tr>
        <th>Nome do Produto</th>
        <th>Tipo do Produto</th>
        <th>Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="produtoAlimenticio in produtosAlimenticios" :key="produtoAlimenticio.id">
        <td>{{ produtoAlimenticio.nome }}</td>
        <td>{{ produtoAlimenticio.tipoProdutoAlimenticio }}</td>
        <td>
          <button @click.prevent="editProdutoAlimenticio(produtoAlimenticio)">Editar</button>
          <button @click.prevent="confirmDelete(produtoAlimenticio)">Excluir</button>
        </td>
      </tr>
    </tbody>
  </table>
</div>

<div class="botaoConfirmaDelete" v-if="showDeleteModal">
      <h3>Tem certeza que deseja excluir o produto {{ produtoAlimenticioToDelete.nomeProdutoAlimenticio }}?</h3>
      <div class="buttons-container">
      <button @click.prevent="deleteProdutoAlimenticioConfirmed">Sim</button>
      <button @click.prevent="cancelDelete">Não</button>
    </div>
</div>
  </template>
  
  <script>
  import axios from 'axios'
  
  axios.defaults.xsrfCookieName = 'csrftoken';
  axios.defaults.xsrfHeaderName = 'X-CSRFToken';
  
  export default {
    data() {
      return {
        produtoAlimenticio: {
          nome: '',
          tipoProdutoAlimenticio: ''
        },
        produtosAlimenticios: [],
        isEdit: false,
        showDeleteModal: false,
        produtoAlimenticioToDelete: null
      }
    },
    methods: {
  
  //editar 
  editProdutoAlimenticio(produtoAlimenticio) {
    this.isEdit = true;
    this.produtoAlimenticio = { ...produtoAlimenticio };
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      axios.put(`http://localhost:8000/produtosAlimenticios/editar/${this.produtoAlimenticio.id}/`, this.produtoAlimenticio)
        .then(response => {
          this.produtosAlimenticios = response.data;
          this.isEdit = false; // Redefinir o estado de edição pra não dar ruim
          this.produtoAlimenticio = {
            nome: '',
            tipoProdutoAlimenticio: ''
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      console.log('Método POST')
      axios.post('http://localhost:8000/produtosAlimenticios/', this.produtoAlimenticio)
        .then(response => {
          this.produtosAlimenticios = response.data;
          this.produtoAlimenticio = {
            nome: '',
            tipoProdutoAlimenticio: ''
          };
        })
        .catch(error => {
          console.log(error);
        });
    }
    setTimeout(function() {
      location.reload();
    }, 2000);
  },
  
      deleteProdutoAlimenticio() {
        axios.delete(`http://localhost:8000/produtosAlimenticios/deleteprodutoAlimenticio/${this.produtoAlimenticio.id}/`)
          .then(response => {
            this.produtosAlimenticios = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(produtoAlimenticio) {
        this.showDeleteModal = true
        this.produtoAlimenticioToDelete = produtoAlimenticio
      },
      deleteProdutoAlimenticioConfirmed() {
        axios.delete(`http://localhost:8000/produtosAlimenticios/deleteprodutoAlimenticio/${this.produtoAlimenticioToDelete.id}/`)
          .then(response => {
            this.produtosAlimenticios = response.data
            this.showDeleteModal = false
          })
          .catch(error => {
            console.log(error)
          })
          setTimeout(function() {
      location.reload();
      }, 2000);
      },
      cancelDelete() {
        this.showDeleteModal = false
      },
      cancelEdit() {
        window.location.href = '/produtosAlimenticios'
      },
      fetchProdutoAlimenticio(id) {
        axios.get(`http://localhost:8000/produtosAlimenticios/${id}/`)
          .then(response => {
            this.produtoAlimenticio = response.data
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    
    mounted() {
      axios.get('http://localhost:8000/produtosAlimenticios/')
        .then(response => {
          this.produtosAlimenticios = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  
  }
  </script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');

.container {
    font-family: 'Poppins', sans-serif;
    text-align: center;
}

.form-group {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.form-group input {
  flex: 1; 
  padding: 5px; 
}

.form-group label {
  width: 100px; 
  text-align: right;
  margin-right: 10px; 
  font-weight: bold;
}

button {
    padding: 10px 20px;
    margin-right: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s;
    background-color: #28a745; 
    color: #FFF;
    font-weight: 500;
    box-shadow: 0 2px 8px rgba(40, 167, 69, 0.1); 

    &:hover {
        background-color: #218838; 
        box-shadow: 0 4px 12px rgba(33, 136, 56, 0.2); 
    }
}

div {
    justify-content: center;
}

.botaoConfirmaDelete {
    background-color: rgba(0,0,0,0.7);
    color: #FFF;
}

.buttons-container {
    padding: 20px;
}

h1 {
    justify-content: center;
    text-align: center;
    color: #333;
    font-weight: 600;
    
}

table {
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    width: 100%;
}

.table {
    width: 90%; 
    margin: 0 auto; 
}

th, td {
    font-weight: 400;
}

th {
    background-color: #28a745; 
    color: #FFF;
}

tr:nth-child(odd) {
    background-color: #e6f4ea;
}

tr:hover {
    background-color: #d1ecd5; 
}

.container {
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    background-color: #FFF;
}

form, .table, .botaoConfirmaDelete {  
    width: 100%;
    text-align: center;
}


h1, h2 {
    width: 100%;
}

h2 {
  text-align: center;
}

</style>