<template>
    <div class="container">
      <h2>Cadastro de Outra Despesa</h2>
      <form @submit.prevent="submitForm">

        <div class="form-group">
          <label for="descricaoOutraDespesa">Descrição</label>
          <input type="text" id="descricaoOutraDespesa" v-model="outraDespesa.descricaoOutraDespesa" required>
        </div>

        <div class="form-group">
          <label for="motivoGasto">Motivo</label>
          <input type="text" id="motivoGasto" v-model="outraDespesa.motivoGasto" required>
        </div>

        <div class="left-label">
        <label for="propriedade">Propriedade&nbsp;</label>
          <select id="propriedade" v-model="outraDespesa.idPropOutraDespesa" required>
            <option value="">Selecione uma propriedade</option>
            <option v-for="idPropOutraDespesa in propriedades" :value="idPropOutraDespesa.id" :key="idPropOutraDespesa.id">{{ idPropOutraDespesa.nomeProp }}</option>
          </select>
        </div>

        <div class="form-group">
          <label for="valorOutraDespesa">Valor (R$)</label>
          <input type="valorOutraDespesa" id="valorOutraDespesa" v-model="outraDespesa.valorOutraDespesa" required>
        </div>
        
        <div class="form-groupData">
          <label for="dataDespesa">Data</label>
          <input type="date" id="dataDespesa" v-model="outraDespesa.dataDespesa" required>
        </div>

        <button type="submit">Salvar</button>
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>
  <br>

  <div class="table">
  <h1>Lista de Outras Despesas</h1>
  <table>
    <thead>
      <tr>
        <th>Descrição da despesa</th>
        <th>Motivo da despesa</th>
        <th>Valor (R$)</th>
        <th>Data</th>
        <th>Propriedade</th>
        <th>Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="outraDespesa in outrasDespesas" :key="outraDespesa.id">
        <td>{{ outraDespesa.descricaoOutraDespesa }}</td>
        <td>{{ outraDespesa.motivoGasto }}</td>
        <td>{{ outraDespesa.valorOutraDespesa }}</td>
        <td>{{ outraDespesa.dataDespesa }}</td>
        <td>{{ getPropriedadeNameById(outraDespesa.idPropOutraDespesa) }}</td>
        <td>
          <button @click.prevent="editOutraDespesa(outraDespesa)" class="action">Editar</button>
          <button @click.prevent="confirmDelete(outraDespesa)" class="action">Excluir</button>
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
        outraDespesa: {
          dataDespesa: '',
          descricaoOutraDespesa: '',
          motivoGasto: '',
          valorOutraDespesa: '',
          idPropOutraDespesa: ''
        },
        propriedades: [],
        outrasDespesas: [],
        isEdit: false,
        showDeleteModal: false,
        propriedadeToDelete: null
      }
    },
    methods: {
  
  //editar 
  editOutraDespesa(outraDespesa) {
    this.isEdit = true;
    this.outraDespesa = { ...outraDespesa };
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      axios.put(`http://localhost:8000/outrasDespesas/editar/${this.outraDespesa.id}/`, this.outraDespesa)
        .then(response => {
          this.outrasDespesas = response.data;
          this.isEdit = false;
          this.outraDespesa = {
            dataDespesa: '',
            descricaoOutraDespesa: '',
            motivoGasto: '',
            valorOutraDespesa: '',
            idPropOutraDespesa: this.propriedade.id
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      console.log('Método POST')
      axios.post('http://localhost:8000/outrasDespesas/', this.outraDespesa)
        .then(response => {
          this.outrasDespesas = response.data;
          this.outraDespesa = {
            dataDespesa: '',
            descricaoOutraDespesa: '',
            motivoGasto: '',
            valorOutraDespesa: '',
            idPropOutraDespesa: this.propriedade.id
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
  
      deleteOutraDespesa() {
        console.log("Pegou o delete?", this.outraDespesa)
        axios.delete(`http://localhost:8000/outrasDespesas/deleteoutraDespesa/${this.outraDespesa.id}/`)
          .then(response => {
            this.outrasDespesas = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(outraDespesa) {
        if (window.confirm("Você tem certeza de que deseja excluir esta despesa?")) {
          this.outraDespesaToDelete = outraDespesa;
          this.deleteOutraDespesaConfirmed();
        }
      },
      deleteOutraDespesaConfirmed() {
        axios.delete(`http://localhost:8000/outrasDespesas/deleteoutraDespesa/${this.outraDespesaToDelete.id}/`)
          .then(response => {
            this.outrasDespesas = response.data
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
        window.location.href = '/outrasDespesas'
      },
      fetchOutraDespesa(id) {
        axios.get(`http://localhost:8000/outrasDespesas/${id}/`)
          .then(response => {
            this.outraDespesa = response.data
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
      axios.get('http://localhost:8000/outrasDespesas/')
        .then(response => {
          this.outrasDespesas = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },

    computed: {
  getPropriedadeNameById() {
    return (id) => {
      const propriedade = this.propriedades.find(p => p.id === id);
      return propriedade ? propriedade.nomeProp : 'Desconhecido';
    }
  }
}
  
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
  margin-left: 6px; 
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
  margin-right: 490px;
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
    width: 175%;
}

.table {
    width: 175%; 
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