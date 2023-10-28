<template>
  <div class="app-container">
    <div class="container">
      <h2>Cadastro de Compra de Produto</h2>
      <form @submit.prevent="submitForm">

        <div>
        <label for="idProduto">Produto:</label>
          <select id="idProduto" v-model="compraProduto.idProduto" required>
            <option value="">Selecione um produto</option>
            <option v-for="idProduto in produtos" :value="idProduto.nome" :key="idProduto.nome">{{ idProduto.nome }}</option>
          </select>
        </div>
        <div>
          <label for="valorUnitario">Valor unitário do produto:</label>
          <input type="valorUnitario" id="valorUnitario" v-model="compraProduto.valorUnitario" required>
        </div>

        <div>
          <label for="qtdComprada">Quantidade comprada:</label>
          <input type="qtdComprada" id="qtdComprada" v-model="compraProduto.qtdComprada" required>
        </div>

        <div>
          <label for="dataCompra">Data da compra:</label>
          <input type="date" id="dataCompra" v-model="compraProduto.dataCompra" required>
        </div>

        <div>
          <label for="descricao">Descrição:</label>
          <input type="descricao" id="descricao" v-model="compraProduto.descricao" required>
        </div>

        <div>
          <label for="valorTotal">Valor total do produto:</label>
          <input type="valorTotal" id="valorTotal" v-model="compraProduto.valorTotal" required>
        </div>

        <div>
          <label for="validade">Validade:</label>
          <input type="date" id="validade" v-model="compraProduto.validade" required>
        </div>

        <button type="submit">Salvar</button>
        <button v-if="isEdit" @click.prevent="deleteCompraProduto">Excluir</button>
        <!-- <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>-->
      </form>
    </div>

    <div class="table">
      <h1>Lista de Compras de Produtos</h1>
      <table>
    <thead>
      <tr>
        <th>Produto</th>
        <th>Valor unitário</th>
        <th>Quantidade comprada</th>
        <th>Data da compra</th>
        <th>Descrição</th>
        <th>Valor total do produto</th>
        <th>Validade</th>
        <th>Ações</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="compraProduto in compraProdutos" :key="compraProduto.id">
        <td>{{ compraProduto.idProduto }}</td>
        <td>{{ compraProduto.valorUnitario }}</td>
        <td>{{ compraProduto.qtdComprada }}</td>
        <td>{{ compraProduto.dataCompra }}</td>
        <td>{{ compraProduto.descricao }}</td>
        <td>{{ compraProduto.valorTotal }}</td>
        <td>{{ compraProduto.validade }}</td>
        <td>
          <button @click.prevent="editCompraProduto(compraProduto)">Editar</button>
          <button @click.prevent="confirmDelete(compraProduto)">Excluir</button>
        </td>
      </tr>
    </tbody>
  </table>
      
    </div>

    <div class="botaoConfirmaDelete" v-if="showDeleteModal">
      <h3>Tem certeza que deseja excluir a compra do produto {{ compraProdutoToDelete.descricao }}?</h3>
      <button @click.prevent="deleteCompraProdutoConfirmed">Sim</button>
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
        compraProduto: {
          idProduto: '',
          valorUnitario: '',
          qtdComprada: '',
          dataCompra: '',
          descricao: '',
          valorTotal: '',
          validade: ''
        },
        compraProdutos: [],
        prodSanitarios: [],
        produtosAlimenticios: [],
        produtos: [],
        isEdit: false,
        showDeleteModal: false,
        compraProdutoToDelete: null
      }
    },

    methods: {



       //editar 
  editCompraProduto(compraProduto) {
    this.isEdit = true;
    this.compraProduto = { ...compraProduto};
  },
      
  atualizarProdutos() {
        this.produtos = [...this.produtosAlimenticios, ...this.prodSanitarios];
    },

  //adicionar
  submitForm() {
    if (this.isEdit) {
      axios.put(`http://localhost:8000/compraProdutos/editar/${this.compraProduto.id}/`, this.compraProduto)
        .then(response => {
          this.compraProdutos = response.data;
          this.isEdit = false; // Redefinir o estado de edição pra não dar ruim
          this.compraProdutos = {
            idProduto: '',
            valorUnitario: '',
            qtdComprada: '',
            dataCompra: '',
            descricao: '',
            valorTotal: '',
            validade: ''
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      console.log('Método POST')
      axios.post('http://localhost:8000/compraProdutos/', this.compraProduto)
        .then(response => {
          this.compraProdutos = response.data;
          this.compraProduto = {
            idProduto: '',
            valorUnitario: '',
            qtdComprada: '',
            dataCompra: '',
            descricao: '',
            valorTotal: '',
            validade: ''
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
  
      deleteCompraProduto() {
        console.log("Pegou o delete?", this.compraProduto)
        axios.delete(`http://localhost:8000/compraProdutos/deletecompraProduto/${this.compraProduto.id}/`)
          .then(response => {
            this.compraProdutos = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(compraProduto) {
        console.log("Que tem aqui?", compraProduto)
        this.showDeleteModal = true
        this.compraProdutoToDelete = compraProduto
      },
      deleteCompraProdutoConfirmed() {
        console.log("E aqui?", this.compraProdutoToDelete)
        axios.delete(`http://localhost:8000/compraProdutos/deletecompraProduto/${this.compraProdutoToDelete.id}/`)
          .then(response => {
            this.compraProdutos = response.data
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
        window.location.href = '/compraProdutos'
      },
      fetchCompraProduto(id) {
        axios.get(`http://localhost:8000/compraProdutos/${id}/`)
          .then(response => {
            this.compraProduto = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },


      getProductNameById(id) {
        let product = this.produtos.find(p => p.id === id);
        return product ? product.nome : '';
    },

    },

  mounted() {
    axios.get('http://localhost:8000/compraProdutos/')
    .then(response => {
      this.compraProdutos = response.data;
    })
    .catch(error => {
      console.log(error);
    });

    axios.get('http://localhost:8000/produtosAlimenticios/')
    .then(response => {
      this.produtosAlimenticios = response.data;
      this.atualizarProdutos();
    })
    .catch(error => {
      console.log(error);
    });

    axios.get('http://localhost:8000/prodSanitarios/')
    .then(response => {
      this.prodSanitarios = response.data;
      this.atualizarProdutos();
    })
    .catch(error => {
      console.log(error);
    });
  },


    /*mounted() {
      const urlParams = new URLSearchParams(window.location.search);
      const id = urlParams.get('id');
      if (id) {
        this.isEdit = true
        this.fetchProdutor(id)
      }
    }*/
    
    /*mounted() {
        axios.get('http://localhost:8000/compraProdutos/')
        .then(response => {
          this.compraProdutos = response.data
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
        axios.get('http://localhost:8000/prodSanitarios/')
        .then(response => {
          this.prodSanitarios = response.data
        })
        .catch(error => {
          console.log(error)
        })

    }*/
  
  }




</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');

/* Base para aplicar a fonte em todo o componente */
.container {
    font-family: 'Poppins', sans-serif;
    text-align: center;
    margin: 0 auto;
    max-width: 100%;
}

.app-container {
    width: 100%;
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
