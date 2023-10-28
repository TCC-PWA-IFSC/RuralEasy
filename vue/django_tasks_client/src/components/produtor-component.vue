<template>
    <div class="container">
      <h2>Cadastro de Produtor Rural</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="nomeProd">Nome:</label>
          <input type="text" id="nomeProd" v-model="produtor.nomeProd" required>
        </div>
        <div>
          <label for="cpf">CPF</label>
          <input type="cpf" id="cpf" v-model="produtor.cpf" required>
        </div>
        <div>
          <label for="email">E-mail:</label>
          <input type="email" id="email" v-model="produtor.email" required>
        </div>
        <div>
          <label for="telefone">Telefone:</label>
          <input type="telefone" id="telefone" v-model="produtor.telefone" required>
        </div>
        <div>
          <label for="user">Usuário:</label>
          <input type="user" id="user" v-model="produtor.user" required>
        </div>
        <div>
          <label for="password">Senha:</label>
          <input type="password" id="password" v-model="produtor.password" required>
        </div>
        <button type="submit">Salvar</button>
        <!--<button v-if="isEdit" @click.prevent="deletePropriedade">Excluir</button>-->
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>
  <br>

  <div class="table">
  <h1>Lista de Produtores</h1>
  <table>
    <thead>
      <tr>
        <th>Nome</th>
        <th>CPF</th>
        <th>E-mail</th>
        <th>Telefone</th>
        <th>Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="produtor in produtores" :key="produtor.id">
        <td>{{ produtor.nomeProd }}</td>
        <td>{{ produtor.cpf }}</td>
        <td>{{ produtor.email }}</td>
        <td>{{ produtor.telefone }}</td>
        <td>
          <button @click.prevent="editProdutor(produtor)">Editar</button>
          <button @click.prevent="confirmDelete(produtor)">Excluir</button>
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
        produtor: {
          nomeProd: '',
          cpf: '',
          email: '',
          telefone: '',
          user: '',
          password: ''
        },
        produtores: [],
        isEdit: false,
        showDeleteModal: false,
        propriedadeToDelete: null
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
      axios.put(`http://localhost:8000/produtores/editar/${this.produtor.id}/`, this.produtor)
        .then(response => {
          this.produtores = response.data;
          this.isEdit = false;
          this.produtor = {
            nomeProd: '',
            cpf: '',
            email: '',
            telefone: '',
            user: '',
            password: ''
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
            cpf: '',
            email: '',
            telefone: '',
            user: '',
            password: ''
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
  
      deleteProdutor() {
        console.log("Pegou o delete?", this.produtor)
        axios.delete(`http://localhost:8000/produtores/deleteprodutor/${this.produtor.id}/`)
          .then(response => {
            this.produtores = response.data
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
      confirmDelete(produtor) {
        if (window.confirm("Você tem certeza de que deseja excluir este produtor?")) {
          this.produtorToDelete = produtor;
          this.deleteProdutorConfirmed();
        }
      },
      deleteProdutorConfirmed() {
        console.log("E aqui?", this.produtorToDelete)
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
      }, 1000);
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
