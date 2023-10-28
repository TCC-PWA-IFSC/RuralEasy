<template>

    <div class="container">
      <h2>Cadastro de Venda de Animal</h2>
      <form @submit.prevent="submitForm">

        <div>
          <label for="finalidadeAnimalVenda">Finalidade do Animal:</label>
          <input type="finalidadeAnimalVenda" id="finalidadeAnimalVenda" v-model="venda.finalidadeAnimalVenda" required>
        </div>
        <div>
          <label for="valorAnimalVenda">Valor do Animal:</label>
          <input type="valorAnimalVenda" id="valorAnimalVenda" v-model="venda.valorAnimalVenda" required>
        </div>
        <div>
          <label for="dataVenda">Data da venda do Animal:</label>
          <input type="date" id="dataVenda" v-model="venda.dataVenda" required>
        </div>
        <div>
          <label for="dataRecebimento">Data do recebimento do dinheiro:</label>
          <input type="date" id="dataRecebimento" v-model="venda.dataRecebimento" required>
        </div>
        <div>
          <label for="pesoAnimalVenda">Peso atual do Animal:</label>
          <input type="pesoAnimalVenda" id="pesoAnimalVenda" v-model="venda.pesoAnimalVenda" required>
        </div>
        <div>
          <label for="precoAtualArrobaKg">Preço atual da @:</label>
          <input type="precoAtualArrobaKg" id="precoAtualArrobaKg" v-model="venda.precoAtualArrobaKg" required>
        </div>
        <div>
          <label for="observacaoVenda">Observações da venda:</label>
          <input type="observacaoVenda" id="observacaoVenda" v-model="venda.observacaoVenda" required>
        </div>
        <div>
        <label for="idAnimalVenda">ID Brinco Animal:</label>
          <select id="idAnimalVenda" v-model="venda.idAnimalVenda" required>
            <option value="">Selecione um animal</option>
            <option v-for="idAnimalVenda in animais" :value="idAnimalVenda.id" :key="idAnimalVenda.id">{{ idAnimalVenda.brinco }}</option>
          </select>
        </div>

        <button type="submit">Salvar</button>
        <button v-if="isEdit" @click.prevent="deleteVenda">Excluir</button>
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>

    <div class="table">
      <h1>Lista de Vendas</h1>
        <table>
          <thead>
            <tr>
              <th>Finalidade</th>
              <th>Valor</th>
              <th>Data da venda</th>
              <th>Data do recebimento</th>
              <th>Peso ao ser vendido</th>
              <th>Arroba</th>
              <th>Observações</th>
              <th>ID Brinco</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="venda in vendas" :key="venda.id">
              <td>{{ venda.finalidadeAnimalVenda }}</td>
              <td>{{ venda.valorAnimalVenda }}</td>
              <td>{{ venda.dataVenda }}</td>
              <td>{{ venda.dataRecebimento }}</td>
              <td>{{ venda.pesoAnimalVenda }}</td>
              <td>{{ venda.precoAtualArrobaKg }}</td>
              <td>{{ venda.observacaoVenda }}</td>
              <td>{{ getAnimalBrincoById(venda.idAnimalVenda) }}</td>
              <td>
                <button @click.prevent="editVenda(venda)">Editar</button>
                <button @click.prevent="confirmDelete(venda)">Excluir</button>
              </td>
            </tr>
          </tbody>
      </table>
    </div>

    <div class="botaoConfirmaDelete" v-if="showDeleteModal">
      <h3>Tem certeza que deseja excluir a venda {{ vendaToDelete.brinco }}?</h3>
      <button @click.prevent="deleteVendaConfirmed">Sim</button>
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
        venda: {
          finalidadeAnimalVenda: '',
          valorAnimalVenda: '',
          dataVenda: '',
          dataRecebimento: '',
          pesoAnimalVenda: '',
          precoAtualArrobaKg: '',
          observacaoVenda: '',
          idAnimalVenda: ''
        },
        vendas: [],
        animais: [],
        isEdit: false,
        showDeleteModal: false,
        propriedadeToDelete: null
      }
    },
    methods: {
  
       //editar 
  editVenda(venda) {
    this.isEdit = true;
    this.venda = { ...venda};
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      //axios.put(`http://localhost:8000/produtores/${this.produtor.id}/editar/`, this.produtor)
      axios.put(`http://localhost:8000/vendas/editar/${this.venda.id}/`, this.venda)
        .then(response => {
          this.vendas = response.data;
          this.isEdit = false; // Redefinir o estado de edição pra não dar ruim
          this.venda = {
            finalidadeAnimalVenda: '',
            valorAnimalVenda: '',
            dataVenda: '',
            dataRecebimento: '',
            pesoAnimalVenda: '',
            precoAtualArrobaKg: '',
            observacaoVenda: '',
            idAnimalVenda: this.idAnimalVenda.id
            //idAnimalVenda: this.venda.idAnimalVenda
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      axios.post('http://localhost:8000/vendas/', this.venda)
        .then(response => {
          this.vendas = response.data;
          this.venda = {
            finalidadeAnimalVenda: '',
            valorAnimalVenda: '',
            dataVenda: '',
            dataRecebimento: '',
            pesoAnimalVenda: '',
            precoAtualArrobaKg: '',
            observacaoVenda: '',
            idAnimalVenda: this.idAnimalVenda.id
            //idAnimalVenda: this.venda.idAnimalVenda
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
  
      deletePropriedade() {
        console.log("Pegou o delete?", this.venda)
        axios.delete(`http://localhost:8000/vendas/deletevenda/${this.venda.id}/`)
          .then(response => {
            this.vendas= response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(venda) {
        console.log("Que tem aqui?", venda)
        this.showDeleteModal = true
        this.vendaToDelete = venda
      },
      deleteVendaConfirmed() {
        console.log("E aqui?", this.vendaToDelete)
        axios.delete(`http://localhost:8000/vendas/deletevenda/${this.vendaToDelete.id}/`)
          .then(response => {
            this.vendas = response.data
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
        window.location.href = '/vendas'
      },
      fetchVenda(id) {
        axios.get(`http://localhost:8000/vendas/${id}/`)
          .then(response => {
            this.venda= response.data
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
        axios.get('http://localhost:8000/vendas/')
        .then(response => {
          this.vendas= response.data
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
