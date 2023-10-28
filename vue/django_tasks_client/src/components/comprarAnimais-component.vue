<template>
    <div class="container">
      <h2>Cadastro de Compra de Animal</h2>
      <form @submit.prevent="submitForm">

        <div>
          <label for="observacoesComprarAnimal">Observações da compra do Animal:</label>
          <input type="observacoesComprarAnimal" id="observacoesComprarAnimal" v-model="comprarAnimal.observacoesComprarAnimal" required>
        </div>
        <div>
          <label for="valorComprarAnimal">Valor da compra do Animal:</label>
          <input type="valorComprarAnimal" id="valorComprarAnimal" v-model="comprarAnimal.valorComprarAnimal" required>
        </div>
        <div>
          <label for="dataComprarAnimal">Data da compra do Animal:</label>
          <input type="date" id="dataComprarAnimal" v-model="comprarAnimal.dataComprarAnimal" required>
        </div>
        <div>
        <label for="idComprarAnimal">ID Brinco Animal:</label>
          <select id="idComprarAnimal" v-model="comprarAnimal.idComprarAnimal" required>
            <option value="">Selecione um animal</option>
            <option v-for="idComprarAnimal in animais" :value="idComprarAnimal.id" :key="idComprarAnimal.id">{{ idComprarAnimal.brinco }}</option>
          </select>
        </div>

        <button type="submit">Salvar</button>
        <button v-if="isEdit" @click.prevent="deleteVenda">Excluir</button>
        <!-- <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>-->
      </form>
    </div>
    <div class="table">

      <h1>Lista de Compras de Animais</h1>
      <table>
    <thead>
      <tr>
        <th>Observações da Compra</th>
        <th>Valor da Compra</th>
        <th>Data da Compra</th>
        <th>Brinco do Animal</th>
        <th>Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="comprarAnimal in comprarAnimais" :key="comprarAnimal.id">
        <td>{{ comprarAnimal.observacoesComprarAnimal }}</td>
        <td>{{ comprarAnimal.valorComprarAnimal }}</td>
        <td>{{ comprarAnimal.dataComprarAnimal }}</td>
        <td>{{ comprarAnimal.idComprarAnimal }}</td>
        <td>
          <button @click.prevent="editComprarAnimal(comprarAnimal)">Editar</button>
          <button @click.prevent="confirmDelete(comprarAnimal)">Excluir</button>
        </td>
      </tr>
    </tbody>
  </table>
      
    </div>


    <div v-if="showDeleteModal">
      <h3>Tem certeza que deseja excluir a compra {{ comprarAnimalToDelete.brinco }}?</h3>
      <button @click.prevent="deleteComprarAnimalConfirmed">Sim</button>
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
        comprarAnimal: {
          idComprarAnimal: '',
          dataComprarAnimal: '',
          valorComprarAnimal: '',
          observacoesComprarAnimal: ''
        },
        comprarAnimais: [],
        animais: [],
        isEdit: false,
        showDeleteModal: false,
        propriedadeToDelete: null
      }
    },
    methods: {
  
       //editar 
  editComprarAnimal(comprarAnimal) {
    this.isEdit = true;
    this.comprarAnimal = { ...comprarAnimal};
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      //axios.put(`http://localhost:8000/produtores/${this.produtor.id}/editar/`, this.produtor)
      axios.put(`http://localhost:8000/comprarAnimais/editar/${this.comprarAnimal.id}/`, this.comprarAnimal)
        .then(response => {
          this.comprarAnimais = response.data;
          this.isEdit = false; // Redefinir o estado de edição pra não dar ruim
          this.comprarAnimal = {
            idComprarAnimal:  this.idComprarAnimal.id,
            dataComprarAnimal: '',
            valorComprarAnimal: '',
            observacoesComprarAnimal: ''
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      console.log('Método POST')
      axios.post('http://localhost:8000/comprarAnimais/', this.comprarAnimal)
        .then(response => {
          this.comprarAnimais = response.data;
          this.comprarAnimal = {
            idComprarAnimal:  this.idComprarAnimal.id,
            dataComprarAnimal: '',
            valorComprarAnimal: '',
            observacoesComprarAnimal: ''
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
  
      deleteComprarAnimal() {
        console.log("Pegou o delete?", this.comprarAnimal)
        axios.delete(`http://localhost:8000/comprarAnimais/deletecomprarAnimal/${this.comprarAnimal.id}/`)
          .then(response => {
            this.comprarAnimais= response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(comprarAnimal) {
        console.log("Que tem aqui?", comprarAnimal)
        this.showDeleteModal = true
        this.comprarAnimalToDelete = comprarAnimal
      },
      deleteComprarAnimalConfirmed() {
        console.log("E aqui?", this.comprarAnimalToDelete)
        axios.delete(`http://localhost:8000/comprarAnimais/deletecomprarAnimal/${this.comprarAnimalToDelete.id}/`)
          .then(response => {
            this.comprarAnimais = response.data
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
        window.location.href = '/comprarAnimais'
      },
      fetchComprarAnimal(id) {
        axios.get(`http://localhost:8000/comprarAnimais/${id}/`)
          .then(response => {
            this.comprarAnimal= response.data
          })
          .catch(error => {
            console.log(error)
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
        axios.get('http://localhost:8000/comprarAnimais/')
        .then(response => {
          this.comprarAnimais= response.data
        })
        .catch(error => {
          console.log(error)
        })
        axios.get('http://localhost:8000/animais/')
        .then(response => {
          this.animais= response.data
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
