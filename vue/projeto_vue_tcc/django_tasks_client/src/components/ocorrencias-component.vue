<template>

    <div class="container">
      <h2>Cadastro de Ocorrências</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="ocorrencia">Descrição da ocorrência:</label>
          <input type="text" id="ocorrencia" v-model="ocorrencia.ocorrencia" required>
        </div>
        <div>
        <label for="idAnimal">ID Brinco Animal:</label>
          <select id="idAnimal" v-model="ocorrencia.idAnimal" required>
            <option value="">Selecione um animal</option>
            <option v-for="idAnimal in animais" :value="idAnimal.id" :key="idAnimal.id">{{ idAnimal.brinco }}</option>
          </select>
        </div>
        <button type="submit">Salvar</button>
        <!--<button v-if="isEdit" @click.prevent="deleteOcorrencia">Excluir</button>-->
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>


    <div class="table">
      <h1>Lista de Ocorrências</h1>
      <table>
        <thead>
          <tr>
            <th>Descrição da ocorrência</th>
            <th>ID Brinco</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="ocorrencia in ocorrencias" :key="ocorrencia.id">
            <td>{{ ocorrencia.ocorrencia }}</td>
            <td>{{ ocorrencia.idAnimal }}</td>
            <td>
              <button @click.prevent="editOcorrencia(ocorrencia)">Editar</button>
              <button @click.prevent="confirmDelete(ocorrencia)">Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>

      <div class="botaoConfirmaDelete" v-if="showDeleteModal">
        <h3>Tem certeza que deseja excluir a ocorrência {{ ocorrenciaToDelete.ocorrencia }}?</h3>
        <button @click.prevent="deleteOcorrenciaConfirmed">Sim</button>
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
        ocorrencia: {
          ocorrencia: '',
          idAnimal: ''
        },
        ocorrencias: [],
        animais: [],
        isEdit: false,
        showDeleteModal: false,
        ocorrenciaToDelete: null
      }
    },
    methods: {
  
       //editar 
  editOcorrencia(ocorrencia) {
    this.isEdit = true;
    this.ocorrencia = { ...ocorrencia };
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      console.log("Aqui", this.ocorrencia.id)
      axios.put(`http://localhost:8000/ocorrencias/editar/${this.ocorrencia.id}/`, this.ocorrencia)
        .then(response => {
          this.ocorrencias = response.data;
          this.isEdit = false; // Redefinir o estado de edição pra não dar ruim
          this.ocorrencia = {
            ocorrencia: '',
            idAnimal: this.idAnimal.id
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      console.log('Método POST')
      axios.post('http://localhost:8000/ocorrencias/', this.ocorrencia)
        .then(response => {
          this.ocorrencias = response.data;
          this.ocorrencia = {
            ocorrencia: '',
            idAnimal: this.idAnimal.id
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
  
      deleteOcorrencia() {
        axios.delete(`http://localhost:8000/ocorrencias/deleteocorrencia/${this.ocorrencia.id}/`)
          .then(response => {
            this.ocorrencias = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(ocorrencia) {
        if (window.confirm("Você tem certeza de que deseja excluir esta propriedade?")) {
          this.ocorrenciaToDelete = ocorrencia;
          this.deleteOcorrenciaConfirmed();
        }
      },
      deleteOcorrenciaConfirmed() {
        axios.delete(`http://localhost:8000/ocorrencias/deleteocorrencia/${this.ocorrenciaToDelete.id}/`)
          .then(response => {
            this.ocorrencias = response.data
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
        window.location.href = '/ocorrencias'
      },
      fetchOcorrencia(id) {
        axios.get(`http://localhost:8000/ocorrencias/${id}/`)
          .then(response => {
            this.ocorrencia = response.data
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    
    mounted() {
    axios.get('http://localhost:8000/ocorrencias/')
        .then(response => {
          this.ocorrencias = response.data
        })
        .catch(error => {
          console.log(error)
        })
    axios.get('http://localhost:8000/animais/')
        .then(response => {
          this.animais = response.data
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
