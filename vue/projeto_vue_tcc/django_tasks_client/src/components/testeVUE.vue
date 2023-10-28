<template>
  <div>
    <h2>Cadastro de Produtor Rural</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="nomeProd">Nome:</label>
        <input type="text" id="nomeProd" v-model="produtor.nomeProd" required>
      </div>
      <div>
        <label for="cpf">CPF:</label>
        <input type="text" id="cpf" v-model="produtor.cpf" required>
      </div>
      <div>
        <label for="email">E-mail:</label>
        <input type="email" id="email" v-model="produtor.email" required>
      </div>
      <div>
        <label for="telefone">Telefone:</label>
        <input type="telefone" id="telefone" v-model="produtor.telefone" required>
      </div>
      <button type="submit">Salvar</button>
      <button v-if="isEdit" @click.prevent="deleteProdutor">Excluir</button>
      <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
    </form>
  </div>
  <div>
    <h1>Lista de Produtores Rurais</h1>
    <ul style="text-align: center; list-style: none;">
      <li v-for="produtor in produtores" :key="produtor.id">
        {{ produtor.nomeProd }}
        <button @click.prevent="editProdutor(produtor)">Editar</button>
        <button @click.prevent="confirmDelete(produtor)">Excluir</button>
      </li>
    </ul>
  </div>
  <div v-if="showDeleteModal">
    <h3>Tem certeza que deseja excluir o produtor {{ produtorToDelete.nomeProd }}?</h3>
    <button @click.prevent="deleteProdutorConfirmed">Sim</button>
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
      produtor: {
        nomeProd: '',
        cpf: null,
        email: '',
        telefone: ''
        //produtores: []
      },
      produtores: [],
      isEdit: false,
      showDeleteModal: false,
      produtorToDelete: null
    }
  },
  methods: {

     //editar 
editProdutor(produtor) {
  this.isEdit = true;
  this.produtor = { ...produtor };
},
    
//adicionar
submitForm() {
  if (this.isEdit) {
    //axios.put(`http://localhost:8000/produtores/${this.produtor.id}/editar/`, this.produtor)
    axios.put(`http://localhost:8000/produtores/editar/${this.produtor.id}/`, this.produtor)
      .then(response => {
        this.produtores = response.data;
        this.isEdit = false; // Redefinir o estado de edição pra não dar ruim
        this.produtor = {
          nomeProd: '',
          cpf: null,
          email: '',
          telefone: ''
        };
      })
      .catch(error => {
        console.log(error);
      });
  } else {
    console.log('Método POST')
    axios.post('http://localhost:8000/produtores/', this.produtor)
      .then(response => {
        this.produtores = response.data;
        this.produtor = {
          nomeProd: '',
          cpf: null,
          email: '',
          telefone: ''
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

    deleteProdutor() {
      axios.delete(`http://localhost:8000/produtores/deleteprodutor/${this.produtor.id}/`)
        .then(response => {
          this.produtores = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    confirmDelete(produtor) {
      this.showDeleteModal = true
      this.produtorToDelete = produtor
    },
    deleteProdutorConfirmed() {
      axios.delete(`http://localhost:8000/produtores/deleteprodutor/${this.produtorToDelete.id}/`)
        .then(response => {
          this.produtores = response.data
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
      window.location.href = '/produtores'
    },
    fetchProdutor(id) {
      axios.get(`http://localhost:8000/produtores/${id}/`)
        .then(response => {
          this.produtor = response.data
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
    axios.get('http://localhost:8000/produtores/')
      .then(response => {
        this.produtores = response.data
      })
      .catch(error => {
        console.log(error)
      })

      /*post
      axios.post('/api/produtores/', this.form)
      .then(response => {
        this.form = response.data
      })
      catch(error => {
        console.log(error)
      })

      axios.put(`http://localhost:8000/produtores/${this.produtor.id}/`, this.produtor)
      .then(response => {
        // Atualização bem-sucedida
        console.log(response.data);
        this.produtor = {
          nomeProd: '',
          cpf: null,
          email: ''
        }; // Limpar o objeto de produtor após a edição
        this.isEdit = false; // Redefinir o estado de edição
      })
      .catch(error => {
        // Erro ao atualizar
        console.log(error);
      }); */
  }

}
</script>