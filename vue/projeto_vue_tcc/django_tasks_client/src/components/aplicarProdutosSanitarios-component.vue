<template>

    <div class="container">
      <h2>Cadastro de Aplicação Sanitária</h2>
      <form @submit.prevent="submitForm">

        <div>
        <label for="idProduto">Produto:</label>
          <select id="idProduto" v-model="aplicarProdutoSanitario.idProduto" required>
            <option value="">Selecione um produto</option>
            <option v-for="idProduto in prodSanitarios" :value="idProduto.id" :key="idProduto.id">{{ idProduto.nomeProdSanitario }}</option>
          </select>
        </div>

        <div>
        <label for="idAnimal">ID Brinco Animal:</label>
          <select id="idAnimal" v-model="aplicarProdutoSanitario.idAnimal" required>
            <option value="">Selecione um animal</option>
            <option v-for="idAnimal in animais" :value="idAnimal.id" :key="idAnimal.id">{{ idAnimal.brinco }}</option>
          </select>
        </div>

        <div>
          <label for="dataAplicacao">Data da aplicação:</label>
          <input type="date" id="dataAplicacao" v-model="aplicarProdutoSanitario.dataAplicacao" required>
        </div>

        <div>
          <label for="dosagem">Dosagem:</label>
          <input type="dosagem" id="dosagem" v-model="aplicarProdutoSanitario.dosagem" required>
        </div>

        <div>
          <label for="observacao">Observação:</label>
          <input type="observacao" id="observacao" v-model="aplicarProdutoSanitario.observacao" required>
        </div>

        <button type="submit">Salvar</button>
        <button v-if="isEdit" @click.prevent="deleteVenda">Excluir</button>
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>

    <div class="table">
      <h1>Lista de Aplicações</h1>
        <table>
          <thead>
            <tr>
              <th>Produto Aplicado</th>
              <th>ID Animal</th>
              <th>Data Aplicação</th>
              <th>Dosagem</th>
              <th>Observação</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="aplicarProdutoSanitario in aplicarProdutosSanitarios" :key="aplicarProdutoSanitario.id">
              <td>{{ getProdSanitarioNomeById(aplicarProdutoSanitario.idProduto) }}</td>
              <td>{{ getAnimalBrincoById(aplicarProdutoSanitario.idAnimal) }}</td>
              <td>{{ aplicarProdutoSanitario.dataAplicacao }}</td>
              <td>{{ aplicarProdutoSanitario.dosagem }}</td>
              <td>{{ aplicarProdutoSanitario.observacao }}</td>
              
              <td>
                <button @click.prevent="editAplicarProdutoSanitario(aplicarProdutoSanitario)">Editar</button>
                <button @click.prevent="confirmDelete(aplicarProdutoSanitario)">Excluir</button>
              </td>
            </tr>
          </tbody>
      </table>
    </div>

    <div class="botaoConfirmaDelete" v-if="showDeleteModal">
      <h3>Tem certeza que deseja excluir a aplicação {{ aplicarProdutoSanitarioToDelete.id }}?</h3>
      <button @click.prevent="deleteAplicarProdutoSanitarioConfirmed">Sim</button>
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
        aplicarProdutoSanitario: {
idProduto: '',
            idAnimal: '',
            dataAplicacao: '',
            dosagem: '',
            observacao: '',
        },
        aplicarProdutosSanitarios: [],
	prodSanitarios: [],
        animais: [],
        isEdit: false,
        showDeleteModal: false,
        aplicarProdutoSanitarioToDelete: null
      }
    },

    methods: {
  
       //editar 
  editAplicarProdutoSanitario(aplicarProdutoSanitario) {
    this.isEdit = true;
    this.aplicarProdutoSanitario = { ...aplicarProdutoSanitario};
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      axios.put(`http://localhost:8000/aplicarProdutosSanitarios/editar/${this.aplicarProdutoSanitario.id}/`, this.aplicarProdutoSanitario)
        .then(response => {
          this.plicarProdutosSanitarios = response.data;
          this.isEdit = false; // Redefinir o estado de edição pra não dar ruim
          this.aplicarProdutoSanitario = {
	idProduto: 'this.prodSanitario.id',
            idAnimal: 'this.idAnimal.id',
            dataAplicacao: '',
            dosagem: '',
            observacao: '',
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      axios.post('http://localhost:8000/aplicarProdutosSanitarios/', this.aplicarProdutoSanitario)
        .then(response => {
          this.aplicarProdutosSanitarios = response.data;
          this.aplicarProdutoSanitario = {
            idProduto: 'this.prodSanitario.id',
            idAnimal: 'this.idAnimal.id',
            dataAplicacao: '',
            dosagem: '',
            observacao: '',
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
  
      deleteAplicarProdutoSanitario() {
        axios.delete(`http://localhost:8000/aplicarProdutosSanitarios/deleteaplicarProdutoSanitario/${this.aplicarProdutoSanitario.id}/`)
          .then(response => {
            this.aplicarProdutosSanitarios = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(aplicarProdutoSanitario) {
        this.showDeleteModal = true
        this.aplicarProdutoSanitarioToDelete = aplicarProdutoSanitario
      },
      deleteAplicarProdutoSanitarioConfirmed() {
        axios.delete(`http://localhost:8000/aplicarProdutosSanitarios/deleteaplicarProdutoSanitario/${this.aplicarProdutoSanitarioToDelete.id}/`)
          .then(response => {
            this.aplicarProdutosSanitarios = response.data
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
        window.location.href = '/aplicarProdutosSanitarios'
      },
      fetchAplicarProdutoSanitario(id) {
        axios.get(`http://localhost:8000/aplicarProdutoSanitarios/${id}/`)
          .then(response => {
            this.aplicarProdutoSanitario= response.data
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
        axios.get('http://localhost:8000/aplicarProdutosSanitarios/')
        .then(response => {
          this.aplicarProdutosSanitarios= response.data
        })
        .catch(error => {
          console.log(error)
        })
        axios.get('http://localhost:8000/prodSanitarios/')
        .then(response => {
          this.prodSanitarios= response.data
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

    },

    computed: {
        getProdSanitarioNomeById() {
            return (id) => {
                const prodSanitario = this.prodSanitarios.find(prod => prod.id === id);
                return prodSanitario ? prodSanitario.nomeProdSanitario : 'Desconhecido';
            }
        },
        getAnimalBrincoById() {
            return (id) => {
                const animal = this.animais.find(a => a.id === id);
                return animal ? animal.brinco : 'Desconhecido';
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
