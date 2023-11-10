<template>
    <div class="container">
      <h2>Cadastro de Movimentações</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="motivoMovimentacao">Motivo</label>
          <input type="motivoMovimentacao" id="motivoMovimentacao" v-model="movimentacao.motivoMovimentacao" required>
        </div>
        <div class="left-label">
        <label for="idAnimal">Brinco Animal &nbsp;</label>
          <select id="idAnimal" v-model="movimentacao.idAnimal" required>
            <option value="">Selecione um animal</option>
            <option v-for="idAnimal in animais" :value="idAnimal.id" :key="idAnimal.id">{{ idAnimal.brinco }}</option>
          </select>
        </div>
        <div class="left-label1">
        <label for="idLote">Lote Origem &nbsp;</label>
          <select id="idLote" v-model="movimentacao.idLoteOrigem" required>
            <option value="">Selecione um animal</option>
            <option v-for="idLote in lotes" :value="idLote.id" :key="idLote.id">{{ idLote.nomeLote }}</option>
          </select>
        </div>

        <div class="left-label2">
        <label for="idLote">Lote Destino &nbsp;</label>
          <select id="idLote" v-model="movimentacao.idLoteDestino" required>
            <option value="">Selecione um animal</option>
            <option v-for="idLote in lotes" :value="idLote.id" :key="idLote.id">{{ idLote.nomeLote }}</option>
          </select>  
        </div>

        <div class="form-groupData">
          <label for="dataMovimentacao">Data &nbsp;</label>
          <input type="date" id="dataMovimentacao" v-model="movimentacao.dataMovimentacao" required>
        </div>
        <button type="submit">Salvar</button>
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>
  <br>

  <div class="table">
  <h1>Lista de Movimentações</h1>
  <table>
    <thead>
      <tr>
        <th>Motivo da Movimentação</th>
        <th>Animal</th>
        <th>Lote de Origem</th>
        <th>Lote de Destino</th>
        <th>Data de Movimentação</th>
        <th>Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="movimentacao in movimentacoes" :key="movimentacao.id">
        <td>{{ movimentacao.motivoMovimentacao }}</td>
        <td>{{ getAnimalById(movimentacao.idAnimal) }}</td>
        <td>{{ getLoteById(movimentacao.idLoteOrigem) }}</td>
        <td>{{ getLoteById(movimentacao.idLoteDestino) }}</td>
        <td>{{ movimentacao.dataMovimentacao }}</td>
        <td>
          <button @click.prevent="editMovimentacao(movimentacao)">Editar</button>
          <button @click.prevent="confirmDelete(movimentacao)">Excluir</button>
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
        movimentacao: {
          motivoMovimentacao: '',
          idAnimal: '',
          idLoteOrigem: '',
          idLoteDestino: '',
          dataMovimentacao: ''
        },
        animais: [],
        lotes: [],
        isEdit: false,
        showDeleteModal: false,
        movimentacaoToDelete: null
      }
    },
    methods: {

    getAnimalById(id) {
    let animal = this.animais.find(a => a.id === id);
    return animal ? animal.brinco : '';
  },

    getLoteById(id) {
    let lote = this.lotes.find(l => l.id === id);
    return lote ? lote.nomeLote : '';
  },
  
  //editar 
  editMovimentacao(movimentacao) {
    this.isEdit = true;
    this.movimentacao = { ...movimentacao };
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      axios.put(`http://localhost:8000/movimentacoes/editar/${this.movimentacao.id}/`, this.movimentacao)
        .then(response => {
          this.movimentacoes = response.data;
          this.isEdit = false;
          this.movimentacao = {
            motivoMovimentacao: '',
            idAnimal: this.animal.id,
            idLoteOrigem: this.lote.idLote,
            idLoteDestino: this.lote.idLote,
            dataMovimentacao: ''
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      console.log('Método POST')
      axios.post('http://localhost:8000/movimentacoes/', this.movimentacao)
        .then(response => {
          this.movimentacoes = response.data;
          this.movimentacao = {
            motivoMovimentacao: '',
            idAnimal: this.animal.id,
            idLoteOrigem: this.lote.idLote,
            idLoteDestino: this.lote.idLote,
            dataMovimentacao: ''
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
  
      deleteMovimentacao() {
        console.log("Pegou o delete?", this.movimentacao)
        axios.delete(`http://localhost:8000/movimentacoes/deletemovimentacao/${this.movimentacao.id}/`)
          .then(response => {
            this.movimentacoes = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(movimentacao) {
        if (window.confirm("Você tem certeza de que deseja excluir esta movimentação?")) {
          this.movimentacaoToDelete = movimentacao;
          this.deleteMovimentacaoConfirmed();
        }
      },
      deleteMovimentacaoConfirmed() {
        axios.delete(`http://localhost:8000/movimentacoes/deletemovimentacao/${this.movimentacaoToDelete.id}/`)
          .then(response => {
            this.movimentacoes = response.data
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
        window.location.href = '/movimentacoes'
      },
      fetchMovimentacao(id) {
        axios.get(`http://localhost:8000/movimentacoes/${id}/`)
          .then(response => {
            this.movimentacao = response.data
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    
    mounted() {
      axios.get('http://localhost:8000/movimentacoes/')
        .then(response => {
          this.movimentacoes = response.data
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
      axios.get('http://localhost:8000/animais/')
        .then(response => {
          this.animais = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },

  }
  </script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');

.container {
    font-family: 'Poppins', sans-serif;
    text-align: center;
}

.left-label {
  text-align: left;
  width: auto; 
  font-weight: bold;
  margin-left: -11px; 
}

.left-label1 {
  text-align: left;
  width: auto; 
  font-weight: bold;
  margin-left: 5px; 
}

.left-label2 {
  text-align: left;
  width: auto; 
  font-weight: bold;
  margin-left: 5px; 
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

.form-groupData {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  margin-right: 485px;
}

.form-groupDatainput {
  flex: 1; 
  padding: 5px; 
}

.form-groupData label {
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
    width: 155%;
}

.table {
    width: 155%; 
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
