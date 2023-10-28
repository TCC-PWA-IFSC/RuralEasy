<template>

    <div class="container">
      <h2>Cadastro de Produto Sanitario</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="nome">Descrição:</label>
          <input type="nome" id="nome" v-model="prodSanitario.nome" required>
        </div>
        <div>
          <label for="loteProdSanitario">Lote:</label>
          <input type="loteProdSanitario" id="loteProdSanitario" v-model="prodSanitario.loteProdSanitario" required>
        </div>
        <div>
          <label for="valorProdSanitario">Valor:</label>
          <input type="valorProdSanitario" id="valorProdSanitario" v-model="prodSanitario.valorProdSanitario" required>
        </div>
        <div>
          <label for="dataCompraProdSanitario">Data da Compra:</label>
          <input type="date" id="dataCompraProdSanitario" v-model="prodSanitario.dataCompraProdSanitario" required>
        </div>
        <button type="submit">Salvar</button>
        <button v-if="isEdit" @click.prevent="deleteProdSanitario">Excluir</button>
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>

    <div class="table">
      <h1>Lista de Produto Sanitario</h1>
      <table>
        <thead>
          <tr>
            <th>Descrição</th>
            <th>Lote</th>
            <th>Valor</th>
            <th>Data da Compra</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="prodSanitario in prodSanitarios" :key="prodSanitario.id">
            <td>{{ prodSanitario.nome }}</td>
            <td>{{ prodSanitario.loteProdSanitario }}</td>
            <td>{{ prodSanitario.valorProdSanitario }}</td>
            <td>{{ prodSanitario.dataCompraProdSanitario }}</td>
            <td>
              <button @click.prevent="editProdSanitario(prodSanitario)">Editar</button>
              <button @click.prevent="confirmDelete(prodSanitario)">Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="botaoConfirmaDelete" v-if="showDeleteModal">
      <h3>Tem certeza que deseja excluir o produto sanitario {{ prodSanitario.nomeProdSanitario }}?</h3>
      <button @click.prevent="deleteProdSanitarioConfirmed">Sim</button>
      <button @click.prevent="cancelDelete">Não</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  axios.defaults.xsrfCookieName = 'csrftoken';
  axios.defaults.xsrfHeaderName = 'X-CSRFToken';
  
  export default {
    data() {
      return {
        prodSanitario: {
          nome: '',
          loteProdSanitario: '',
          valorProdSanitario: '',
          dataCompraProdSanitario: ''
        },
        prodSanitarios: [],
        isEdit: false,
        showDeleteModal: false,
        prodSanitarioToDelete: null
      }
    },
    methods: {
  
       //editar 
  editProdSanitario(prodSanitario) {
    this.isEdit = true;
    this.prodSanitario = { ...prodSanitario };
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      console.log("Aqui", this.prodSanitario.id)
      axios.put(`http://localhost:8000/prodSanitarios/editar/${this.prodSanitario.id}/`, this.prodSanitario)
        .then(response => {
          this.prodSanitarios = response.data;
          this.isEdit = false; // Redefinir o estado de edição pra não dar ruim
          this.prodSanitario = {
            nome: '',
            loteProdSanitario: '',
            valorProdSanitario: '',
            dataCompraProdSanitario: ''
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      console.log('Método POST')
      axios.post('http://localhost:8000/prodSanitarios/', this.prodSanitario)
        .then(response => {
          this.prodSanitarios = response.data;
          this.prodSanitario = {
            nome: '',
            loteProdSanitario: '',
            valorProdSanitario: '',
            dataCompraProdSanitario: ''
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
  
      deleteProdSanitario() {
        axios.delete(`http://localhost:8000/prodSanitarios/deleteprodSanitario/${this.prodSanitario.id}/`)
          .then(response => {
            this.prodSanitarios = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(prodSanitario) {
        if (window.confirm("Você tem certeza de que deseja excluir esta propriedade?")) {
          this.prodSanitarioToDelete = prodSanitario;
          this.deleteProdSanitarioConfirmed();
        }
      },
      deleteProdSanitarioConfirmed() {
        axios.delete(`http://localhost:8000/prodSanitarios/deleteprodSanitario/${this.prodSanitarioToDelete.id}/`)
          .then(response => {
            this.prodSanitarios = response.data
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
        window.location.href = '/prodSanitarios'
      },
      fetchProdSanitario(id) {
        axios.get(`http://localhost:8000/prodSanitarios/${id}/`)
          .then(response => {
            this.prodSanitario = response.data
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    
    mounted() {
      axios.get('http://localhost:8000/prodSanitarios/')
        .then(response => {
          this.prodSanitarios = response.data
        })
        .catch(error => {
          console.log(error)
        })
      /*axios.get('http://localhost:8000/racas/')
        .then(response => {
          this.racas = response.data
        })
        .catch(error => {
          console.log(error)
        })*/
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
