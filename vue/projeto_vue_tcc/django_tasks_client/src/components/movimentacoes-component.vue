<template>
    <div class="container">
      <h2>Cadastro de Movimentações</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="motivoMovimentacao">Motivo da Movimentação</label>
          <input type="motivoMovimentacao" id="motivoMovimentacao" v-model="movimentacao.motivoMovimentacao" required>
        </div>
        <div>
        <label for="idAnimal">ID Brinco Animal:</label>
          <select id="idAnimal" v-model="movimentacao.idAnimal" required>
            <option value="">Selecione um animal</option>
            <option v-for="idAnimal in animais" :value="idAnimal.id" :key="idAnimal.id">{{ idAnimal.brinco }}</option>
          </select>
        </div>
        <div>
        <label for="idLote">Lote Origem:</label>
          <select id="idLote" v-model="movimentacao.idLoteOrigem" required>
            <option value="">Selecione um animal</option>
            <option v-for="idLote in lotes" :value="idLote.id" :key="idLote.id">{{ idLote.nomeLote }}</option>
          </select>
        </div>

        <div>
        <label for="idLote">Lote Destino:</label>
          <select id="idLote" v-model="movimentacao.idLoteDestino" required>
            <option value="">Selecione um animal</option>
            <option v-for="idLote in lotes" :value="idLote.id" :key="idLote.id">{{ idLote.nomeLote }}</option>
          </select>  
        </div>

        <div>
          <label for="dataMovimentacao">Data da movimentação do Animal:</label>
          <input type="date" id="dataMovimentacao" v-model="movimentacao.dataMovimentacao" required>
        </div>
        <button type="submit">Salvar</button>
        <!--<button v-if="isEdit" @click.prevent="deletePropriedade">Excluir</button>-->
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
      //confirmDelete(propriedade) {
      //  console.log("Que tem aqui?", propriedade)
      //  this.showDeleteModal = true
      //  this.propriedadeToDelete = propriedade
      //}
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
    /*mounted() {
      const urlParams = new URLSearchParams(window.location.search);
      const id = urlParams.get('id');
      if (id) {
        this.isEdit = true
        this.fetchProdutor(id)
      }
    }*/
    
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
