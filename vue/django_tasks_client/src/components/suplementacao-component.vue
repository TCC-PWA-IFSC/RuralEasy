<template>
    <div class="container">
      <h2>Cadastro de Suplementação</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="kgConsumoSuplementacao">KG de consumo</label>
          <input type="kgConsumoSuplementacao" id="kgConsumoSuplementacao" v-model="suplementacao.kgConsumoSuplementacao" required>
        </div>
        <div class="form-groupData">
          <label for="dataAplicacaoSuplementacao">Data da aplicação</label>
          <input type="date" id="dataAplicacaoSuplementacao" v-model="suplementacao.dataAplicacaoSuplementacao" required>
        </div>
        <div class="left-label">
        <label for="idLoteSuplAplicado">Lote&nbsp;&nbsp;</label>
          <select id="idLoteSuplAplicado" v-model="suplementacao.idLoteSuplAplicado" required>
            <option value="">Selecione um lote</option>
            <option v-for="idLoteSuplAplicado in lotes" :value="idLoteSuplAplicado.id" :key="idLoteSuplAplicado.id">{{ idLoteSuplAplicado.nomeLote }}</option>
          </select>
        </div>

        <div class="left-label1">
        <label for="idProdutoAlimenticio">Produto&nbsp;&nbsp;</label>
          <select id="idProdutoAlimenticio" v-model="suplementacao.idProdutoAlimenticio" required>
            <option value="">Selecione um produto</option>
            <option v-for="idProdutoAlimenticio in produtosAlimenticios" :value="idProdutoAlimenticio.id" :key="idProdutoAlimenticio.id">{{ idProdutoAlimenticio.nome }}</option>
          </select>
        </div>
        <button type="submit">Salvar</button>
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>
  <br>

  <div class="table">
  <h1>Lista de Suplementaçoes</h1>
  <table>
    <thead>
      <tr>
        <th>KG de Consumo</th>
        <th>Data da aplicação</th>
        <th>Lote</th>
        <th>Produto alimenticio</th>
        <th>Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="suplementacao in suplementacoes" :key="suplementacao.id">
        <td>{{ suplementacao.kgConsumoSuplementacao }}</td>
        <td>{{ suplementacao.dataAplicacaoSuplementacao }}</td>
        <td>{{ getLoteById(suplementacao.idLoteSuplAplicado) }}</td>
        <td>{{ getProdutoAlimenticioById(suplementacao.idProdutoAlimenticio) }}</td>
        <td>
          <button @click.prevent="editSuplementacao(suplementacao)">Editar</button>
          <button @click.prevent="confirmDelete(suplementacao)">Excluir</button>
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
        suplementacao: {
          kgConsumoSuplementacao: '',
          dataAplicacaoSuplementacao: '',
          idLoteSuplAplicado: '',
          idProdutoAlimenticio: ''
        },
        suplementacoes: [],
        lotes: [],
        produtosAlimenticios: [],
        isEdit: false,
        showDeleteModal: false,
        suplementacaoToDelete: null
      }
    },

    methods: {

    getLoteById(id) {
    let lote = this.lotes.find(l => l.id === id);
    return lote ? lote.nomeLote : '';
  },

  getProdutoAlimenticioById(id) {
    let produtoAlimenticio = this.produtosAlimenticios.find(p => p.id === id);
    return produtoAlimenticio ? produtoAlimenticio.nome : '';
  },
  
       //editar 
  editSuplementacao(suplementacao) {
    this.isEdit = true;
    this.suplementacao = { ...suplementacao };
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      axios.put(`http://localhost:8000/suplementacoes/editar/${this.suplementacao.id}/`, this.suplementacao)
        .then(response => {
          this.suplementacoes = response.data;
          this.isEdit = false;
          this.suplementacao = {
            kgConsumoSuplementacao: '',
            dataAplicacaoSuplementacao: '',
            idLoteSuplAplicado: 'this.lote.idLote',
            idProdutoAlimenticio: 'this.produtoAlimenticio.id'
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      axios.post('http://localhost:8000/suplementacoes/', this.suplementacao)
        .then(response => {
          this.suplementacoes = response.data;
          this.suplementacao = {
            kgConsumoSuplementacao: '',
            dataAplicacaoSuplementacao: '',
            idLoteSuplAplicado: 'this.lote.idLote',
            idProdutoAlimenticio: 'this.produtoAlimenticio.id'
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
  
      deleteSuplementacao() {
        axios.delete(`http://localhost:8000/suplementacoes/deletesuplementacao/${this.suplementacao.id}/`)
          .then(response => {
            this.suplementacoes = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(suplementacao) {
        if (window.confirm("Você tem certeza de que deseja excluir esta suplementacao?")) {
          this.suplementacaoToDelete = suplementacao;
          this.deleteSuplementacaoConfirmed();
        }
      },
      deleteSuplementacaoConfirmed() {
        axios.delete(`http://localhost:8000/suplementacoes/deletesuplementacao/${this.suplementacaoToDelete.id}/`)
          .then(response => {
            this.suplementacoes = response.data
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
        window.location.href = '/suplementacoes'
      },
      fetchSuplementacao(id) {
        axios.get(`http://localhost:8000/suplementacoes/${id}/`)
          .then(response => {
            this.suplementacao = response.data;
          })
          .catch(error => {
            console.log(error);
          })
      }
    },
    
    mounted() {
	axios.get('http://localhost:8000/suplementacoes/')
        .then(response => {
          this.suplementacoes = response.data
        })
        .catch(error => {
          console.log(error)
        })
      axios.get('http://localhost:8000/produtosAlimenticios/')
        .then(response => {
          this.produtosAlimenticios = response.data
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
  margin-left: 70px; 
}

.left-label1 {
  text-align: left;
  width: auto;
  font-weight: bold;
  margin-left: 40px; 
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
    width: 100%;
}

.table {
    width: 90%; 
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