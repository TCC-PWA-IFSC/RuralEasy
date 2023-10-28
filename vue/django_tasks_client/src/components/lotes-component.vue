<template>
    <div class="container">
      <h2>Cadastro de Lotes</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="nomeLote">Nome:</label>
          <input type="text" id="nomeLote" v-model="lote.nomeLote" required>
        </div>
        <div>
        <label for="tipoCultivo">Tipo do Cultivo:</label>
          <select id="tipoCultivo" v-model="lote.tipoCultivo" required>
            <option value="">Selecione um tipo de cultivo</option>
            <option v-for="cultivo in tiposDeCultivo" :value="cultivo" :key="cultivo">{{ cultivo }}</option>
          </select>
        </div>
        <div>
        <label for="propriedade">Propriedade:</label>
          <select id="propriedade" v-model="lote.idProp" required>
            <option value="">Selecione uma propriedade</option>
            <option v-for="idProp in propriedades" :value="idProp.id" :key="idProp.id">{{ idProp.nomeProp }}</option>
          </select>
        </div>
        <button type="submit">Salvar</button>
        <!-----<button v-if="isEdit" @click.prevent="deleteLote">Excluir</button>-->
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>

    <div class="table">
  <h1>Lista de Lotes</h1>
  <table>
    <thead>
      <tr>
        <th>Lote</th>
        <th>Tipo de Cultivo</th>
        <th>Propriedade</th>
        <th>Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="lote in lotes" :key="lote.id">
        <td>{{ lote.nomeLote }}</td>
        <td>{{ lote.tipoCultivo }}</td>
        <td>{{ getPropNameById(lote.idProp) }}</td>
        <td>
          <button @click.prevent="editLote(lote)">Editar</button>
          <button @click.prevent="confirmDelete(lote)">Excluir</button>
        </td>
      </tr>
    </tbody>
  </table>

   <div class="botaoConfirmaDelete" v-if="showDeleteModal">
      <h3>Tem certeza que deseja excluir o lote {{ loteToDelete.nomeLote}}?</h3>
      <div class="buttons-container">
      <button @click.prevent="deleteLoteConfirmed(loteToDelete)">Sim</button>
      <button @click.prevent="cancelDelete">Não</button>
      </div>
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
        lote: {
          nomeLote: '',
          idProp: ''
        },
        lotes: [],
        propriedades: [],
        tiposDeCultivo: ['Confinamento', 'Semiconfinamento', 'Lavoura', 'Campo Nativo'],
        isEdit: false,
        showDeleteModal: false,
        loteToDelete: null
      }
    },
    methods: {
  
       //editar 
  editLote(lote) {
    this.isEdit = true;
    this.lote = { ...lote};
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) { 
        console.log("Aqui", this.lote.id)
      axios.put(`http://localhost:8000/lotes/editar/${this.lote.id}/`, this.lote)
        .then(response => {
          this.lotes = response.data;
          this.isEdit = false; // Redefinir o estado de edição pra não dar ruim
          this.lote = {
            nomeLote: '',
            tipoCultivo: '',
            idProp: this.idProp.id
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      console.log('Método POST')
      axios.post('http://localhost:8000/lotes/', this.lote)
        .then(response => {
          this.lotes = response.data;
          this.lote = {
            nomeLote: '',
            tipoCultivo: '',
            idProp: this.idProp.id
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
  
      deleteLote() {
        axios.delete(`http://localhost:8000/lotes/deletelote/${this.lote.id}/`)
          .then(response => {
            this.lotes = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(lote) {
        console.log("Ó o lote aqui:", lote)
        this.showDeleteModal = true
        this.loteToDelete = lote
        console.log("confirmDelete:", this.loteToDelete)
      },

      deleteLoteConfirmed(loteToDelete) {
        console.log("deleteLoteConfirmed:", loteToDelete)
        axios.delete(`http://localhost:8000/lotes/deletelote/${loteToDelete.id}/`)
          .then(response => {
            this.lotes = response.data
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
        window.location.href = '/lotes'
      },
      fetchLote(id) {
        axios.get(`http://localhost:8000/lotes/${id}/`)
          .then(response => {
            this.lote = response.data
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    
    mounted() {
        axios.get('http://localhost:8000/propriedades/')
        .then(response => {
          this.propriedades = response.data
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
    },

    computed: {
    getPropNameById() {
        return (id) => {
            const prop = this.propriedades.find(p => p.id === id);
            return prop ? prop.nomeProp : 'Desconhecido';
        }
    }
},
  
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
