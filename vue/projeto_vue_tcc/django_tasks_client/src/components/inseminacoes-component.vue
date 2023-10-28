<template>

    <div class="container">
      <h2>Cadastro de Inseminações</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="dataInseminacao">Data da inseminação:</label>
          <input type="date" id="dataInseminacao" v-model="inseminacao.dataInseminacao" required>
        </div>
        <div>
          <label for="horaCio">Hora do Cio:</label>
          <input type="horaCio" id="horaCio" v-model="inseminacao.horaCio" required>
        </div>
        <div>
          <label for="tecnica">Tecnica:</label>
          <input type="tecnica" id="tecnica" v-model="inseminacao.tecnica" required>
        </div>
        <div>
          <label for="diaGestacao">Dia da gestação:</label>
          <input type="date" id="diaGestacao" v-model="inseminacao.diaGestacao" required>
        </div>
        <div>
          <label for="identificacaoTouro">Identificação do touro:</label>
          <input type="identificacaoTouro" id="identificacaoTouro" v-model="inseminacao.identificacaoTouro" required>
        </div>
        <div>
        <label for="idVaca">Brinco da Vaca:</label>
          <select id="idVaca" v-model="inseminacao.idVaca" required>
            <option value="">Selecione uma vaca</option>
            <option v-for="idAnimal in animais" :value="idAnimal.id" :key="idAnimal.id">{{ idAnimal.brinco }}</option>
          </select>
        </div>
        <div>
        <label for="idInseminador">Nome do Inseminador:</label>
          <select id="idInseminador" v-model="inseminacao.idInseminador" required>
            <option value="">Selecione um inseminador</option>
            <option v-for="idInseminador in veterinarios" :value="idInseminador.id" :key="idInseminador.id">{{ idInseminador.nome }}</option>
          </select>
        </div>
        <button type="submit">Salvar</button>
        <button v-if="isEdit" @click.prevent="deleteInseminacao">Excluir</button>
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>

    <div class="table">
      <h1>Lista de Inseminações</h1>
      <table>
        <thead>
          <tr>
            <th>Data da Inserminação</th>
            <th>Hora do Cio</th>
            <th>Técnica</th>
            <th>Dia da gestação</th>
            <th>Identificação do Touro</th>
            <th>ID Vaca</th>
            <th>ID Inseminador</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="inseminacao in inseminacoes" :key="inseminacao.id">
            <td>{{ inseminacao.dataInseminacao }}</td>
            <td>{{ inseminacao.horaCio }}</td>
            <td>{{ inseminacao.tecnica }}</td>
            <td>{{ inseminacao.diaGestacao }}</td>
            <td>{{ inseminacao.identificacaoTouro }}</td>
            <td>{{ getAnimalNameById(inseminacao.idVaca) }}</td>
            <td>{{ getVeterinarioNameById(inseminacao.idInseminador) }}</td>
            <td>
              <button @click.prevent="editInseminacao(inseminacao)">Editar</button>
              <button @click.prevent="confirmDelete(inseminacao)">Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="botaoConfirmaDelete" v-if="showDeleteModal">
      <h3>Tem certeza que deseja excluir a inseminacao {{ inseminacaoToDelete.inseminacao }}?</h3>
      <button @click.prevent="deleteInseminacaoConfirmed">Sim</button>
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
        inseminacao: {
          dataInseminacao: '',
          horaCio: '',
          tecnica: '',
          diaGestacao: '',
          identificacaoTouro: '',
          idVaca: '',
          idInseminador: ''
        },
        inseminacoes: [],
        animais: [],
        veterinarios: [],
        isEdit: false,
        showDeleteModal: false,
        inseminacaoToDelete: null
      }
    },
    methods: {
  
       //editar 
  editInseminacao(inseminacao) {
    this.isEdit = true;
    this.inseminacao = { ...inseminacao };
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      console.log("Aqui", this.inseminacao.idTouro)
      axios.put(`http://localhost:8000/inseminacoes/editar/${this.inseminacao.id}/`, this.inseminacao)
        .then(response => {
          this.inseminacoes = response.data;
          this.isEdit = false; // Redefinir o estado de edição pra não dar ruim
          this.inseminacao = {
            dataInseminacao: '',
            horaCio: '',
            tecnica: '',
            diaGestacao: '',
            identificacaoTouro: '',
            idVaca: this.idAnimal.id,
            idInseminador: this.idVeterinario.id
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      console.log('Método POST')
      axios.post('http://localhost:8000/inseminacoes/', this.inseminacao)
        .then(response => {
          this.inseminacoes = response.data;
          this.inseminacao = {
            dataInseminacao: '',
            horaCio: '',
            tecnica: '',
            diaGestacao: '',
            identificacaoTouro: '',
            idVaca: this.idAnimal.id,
            idInseminador: this.idVeterinario.id
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
  
      deleteInseminacao() {
        axios.delete(`http://localhost:8000/inseminacoes/deleteinseminacao/${this.inseminacao.id}/`)
          .then(response => {
            this.inseminacoes = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(inseminacao) {
        if (window.confirm("Você tem certeza de que deseja excluir esta propriedade?")) {
          this.inseminacaoToDelete = inseminacao;
          this.deleteInseminacaoConfirmed();
        }
      },
      deleteInseminacaoConfirmed() {
        axios.delete(`http://localhost:8000/inseminacoes/deleteinseminacao/${this.inseminacaoToDelete.id}/`)
          .then(response => {
            this.inseminacoes = response.data
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
        window.location.href = '/inseminacoes'
      },
      fetchInseminacao(id) {
        axios.get(`http://localhost:8000/inseminacoes/${id}/`)
          .then(response => {
            this.inseminacao = response.data
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    
    mounted() {
    axios.get('http://localhost:8000/inseminacoes/')
        .then(response => {
          this.inseminacoes = response.data
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
    axios.get('http://localhost:8000/veterinarios/')
        .then(response => {
          this.veterinarios = response.data
        })
        .catch(error => {
          console.log(error)
        })
      /*axios.get('http://localhost:8000/racas/')
        .then(response => {
          this.racas = response.data
        })
        .catch(error => {
          console.log(error)
        })*/
    },

  computed: {
    getAnimalNameById() {
      return (id) => {
        const animal = this.animais.find(a => a.id === id);
        return animal ? animal.brinco : 'Desconhecido';
      }
    },
    getVeterinarioNameById() {
      return (id) => {
        const veterinario = this.veterinarios.find(v => v.id === id);
        return veterinario ? veterinario.nome : 'Desconhecido';
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
