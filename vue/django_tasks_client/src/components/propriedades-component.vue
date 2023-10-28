<template>
    <div class="container">
      <h2>Cadastro de Propriedade Rural</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="nomeProp">Nome:</label>
          <input type="text" id="nomeProp" v-model="propriedade.nomeProp" required>
        </div>

        <div>
        <label for="produtor">Produtor:</label>
          <select id="produtor" v-model="propriedade.produtor" required>
            <option value="">Selecione um produtor</option>
            <option v-for="produtor in produtores" :value="produtor.id" :key="produtor.id">{{ produtor.nomeProd }}</option>
          </select>
        </div>

        <div>
          <label for="endereco">Endereço</label>
          <input type="endereco" id="endereco" v-model="propriedade.endereco" required>
        </div>
        
        <div>
          <label for="latitude">Latitude:</label>
          <input type="latitude" id="latitude" v-model="propriedade.latitude" required>
        </div>
        <div>
          <label for="longitude">Longitude:</label>
          <input type="longitude" id="longitude" v-model="propriedade.longitude" required>
        </div>
        <div>
          <label for="tamanhoAreaProducao">Tamanho da área de produção:</label>
          <input type="tamanhoAreaProducao" id="tamanhoAreaProducao" v-model="propriedade.tamanhoAreaProducao" required>
        </div>
        <button type="submit">Salvar</button>
        <!--<button v-if="isEdit" @click.prevent="deletePropriedade">Excluir</button>-->
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>
  <br>

  <div class="table">
  <h1>Lista de Propriedades Rurais</h1>
  <table>
    <thead>
      <tr>
        <th>Nome</th>
        <th>Endereço</th>
        <th>Latitude</th>
        <th>Longitude</th>
        <th>Produtor Responsável</th>
        <th>Tamanho Area de Produção</th>
        <th>Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="propriedade in propriedades" :key="propriedade.id">
        <td>{{ propriedade.nomeProp }}</td>
        <td>{{ propriedade.endereco }}</td>
        <td>{{ propriedade.latitude }}</td>
        <td>{{ propriedade.longitude }}</td>
        <td>{{ getProdutorNameById(propriedade.produtor) }}</td>
        <td>{{ propriedade.tamanhoAreaProducao }}</td>
        <td>
          <button @click.prevent="editPropriedade(propriedade)">Editar</button>
          <button @click.prevent="confirmDelete(propriedade)">Excluir</button>
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
        propriedade: {
          nomeProp: '',
          produtor: '',
          endereco: '',
          latitude: '',
          longitude: '',
          tamanhoAreaProducao: ''
        },
        propriedades: [],
        produtores: [],
        isEdit: false,
        showDeleteModal: false,
        propriedadeToDelete: null
      }
    },
    methods: {
  
       //editar 
  editPropriedade(propriedade) {
    this.isEdit = true;
    this.propriedade = { ...propriedade };
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      axios.put(`http://localhost:8000/propriedades/editar/${this.propriedade.id}/`, this.propriedade)
        .then(response => {
          this.propriedades = response.data;
          this.isEdit = false;
          this.propriedade = {
            nomeProp: '',
            produtor: this.produtor.id, 
            endereco: '',
            latitude: '',
            longitude: '',
            tamanhoAreaProducao: ''
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      console.log('Método POST')
      axios.post('http://localhost:8000/propriedades/', this.propriedade)
        .then(response => {
          this.propriedades = response.data;
          this.propriedade = {
            nomeProp: '',
            produtor: this.produtor.id,
            endereco: '',
            latitude: '',
            longitude: '',
            tamanhoAreaProducao: ''
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
  
      deletePropriedade() {
        console.log("Pegou o delete?", this.propriedade)
        axios.delete(`http://localhost:8000/propriedades/deletepropriedade/${this.propriedade.id}/`)
          .then(response => {
            this.propriedades = response.data
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
      confirmDelete(propriedade) {
        if (window.confirm("Você tem certeza de que deseja excluir esta propriedade?")) {
          this.propriedadeToDelete = propriedade;
          this.deletePropriedadeConfirmed();
        }
      },
      deletePropriedadeConfirmed() {
        console.log("E aqui?", this.propriedadeToDelete)
        axios.delete(`http://localhost:8000/propriedades/deletepropriedade/${this.propriedadeToDelete.id}/`)
          .then(response => {
            this.propriedades = response.data
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
        window.location.href = '/propriedades'
      },
      fetchPropriedade(id) {
        axios.get(`http://localhost:8000/propriedades/${id}/`)
          .then(response => {
            this.propriedade = response.data
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
      axios.get('http://localhost:8000/propriedades/')
        .then(response => {
          this.propriedades = response.data
        })
        .catch(error => {
          console.log(error)
        })
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

    computed: {
  getProdutorNameById() {
    return (id) => {
      const produtor = this.produtores.find(p => p.id === id);
      return produtor ? produtor.nomeProd : 'Desconhecido';
    }
  }
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
