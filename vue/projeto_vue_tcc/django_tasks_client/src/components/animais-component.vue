<template>

    <div class="container">
      <h2>Cadastro de Animal</h2>
      <form @submit.prevent="submitForm">
        <div>
        <label for="raca">Raça:</label>
          <select id="raca" v-model="animal.idRaca" required>
            <option value="">Selecione uma raça</option>
            <option v-for="idRaca in racas" :value="idRaca.id" :key="idRaca.id">{{ idRaca.nomeRaca }}</option>
          </select>
        </div>
        <div>
          <label for="observacoesRaca">Observações (Raça):</label>
          <input type="observacoesRaca" id="observacoesRaca" v-model="animal.observacoesRaca" required>
        </div>
        <div>
          <label for="sexo">Sexo:</label>
          <input type="sexo" id="sexo" v-model="animal.sexo" required>
        </div>
        <div>
          <label for="peso">Peso:</label>
          <input type="peso" id="peso" v-model="animal.peso" required>
        </div>
        <div>
          <label for="dataNascimento">Data de Nascimento:</label>
          <input type="date" id="dataNascimento" v-model="animal.dataNascimento" required>
        </div>
        <div>
          <label for="dataMorte">Data de Óbito:</label>
          <input type="date" id="dataMorte" v-model="animal.dataMorte" required>
        </div>
        <div>
          <label for="observacoes">Observações gerais sobre o animal:</label>
          <input type="observacoes" id="observacoes" v-model="animal.observacoes" required>
        </div>
        <div>
          <label for="rfid">RFID:</label>
          <input type="rfid" id="rfid" v-model="animal.rfid" required>
        </div>
        <div>
        <label for="propriedade">Propriedade:</label>
          <select id="propriedade" v-model="animal.idProp" required>
            <option value="">Selecione uma propriedade</option>
            <option v-for="idProp in propriedades" :value="idProp.id" :key="idProp.id">{{ idProp.nomeProp }}</option>
          </select>
        </div>
        <div>
        <label for="idAnimalMae">Mãe do Animal:</label>
          <select id="idAnimalMae" v-model="animal.idAnimalMae" required>
            <option value="">Selecione um animal:</option>
            <option v-for="idAnimalMae in animais" :value="idAnimalMae.id" :key="idAnimalMae.id">{{ idAnimalMae.brinco }}</option>
          </select>
        </div>
        <div>
          <label for="animal_Pai">Pai do Animal:</label>
          <input type="animal_Pai" id="animal_Pai" v-model="animal.animal_Pai">
        </div>
        <div>
          <label for="numeroGestacoes">Número de Gestações:</label>
          <input type="number" id="numeroGestacoes" v-model="animal.numeroGestacoes">
        </div>
        <div>
        <label for="lote">Lote:</label>
          <select id="lote" v-model="animal.idLote" required>
            <option value="">Selecione o lote:</option>
            <option v-for="idLote in lotes" :value="idLote.id" :key="idLote.id">{{ idLote.nomeLote }}</option>
          </select>
        </div>
        <div>
          <label for="brinco">Brinco:</label>
          <input type="brinco" id="brinco" v-model="animal.brinco" required>
        </div>
        <button type="submit">Salvar</button>
        <button v-if="isEdit" @click.prevent="deleteAnimal">Excluir</button>
        <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
      </form>
    </div>

    <div class="table">
      <h1>Lista de Animais</h1>
      <table>
        <thead>
          <tr>
            <th>Raça</th>
            <th>Observações Raça</th>
            <th>Sexo</th>
            <th>Peso</th>
            <th>Nascimento</th>
            <th>Óbito</th>
            <th>Observações gerais</th>
            <th>RFID</th>
            <th>Propriedade</th>
            <th>Animal mãe</th>
            <th>Animal pai</th>
            <th>Número de Gestações</th>
            <th>Lote</th>
            <th>Brinco</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="animal in animais" :key="animal.id">
            <td>{{ getRacaById(animal.idRaca) }}</td>
            <td>{{ animal.observacoesRaca }}</td>
            <td>{{ animal.sexo }}</td>
            <td>{{ animal.peso }}</td>
            <td>{{ animal.dataNascimento }}</td>
            <td>{{ animal.dataMorte }}</td>
            <td>{{ animal.observacoes }}</td>
            <td>{{ animal.rfid }}</td>
            <td>{{ getPropById(animal.idProp) }}</td>
            <td>{{ getAnimalById(animal.idAnimalMae) }}</td>
            <td>{{ getLoteById(animal.idLote) }}</td>
            <td>{{ animal.brinco }}</td>
            
            <td>
              <button @click.prevent="editAnimal(animal)">Editar</button>
              <button @click.prevent="confirmDelete(animal)">Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    
    <div class="botaoConfirmaDelete" v-if="showDeleteModal">
      <h3>Tem certeza que deseja excluir o animal {{ animalToDelete.brinco }}?</h3>
      <button @click.prevent="deleteAnimalConfirmed">Sim</button>
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
        animal: {
          idRaca: '',
          observacoesRaca: '',
          sexo: '',
          peso: '',
          dataNascimento: '',
          dataMorte: '',
          observacoes: '',
          rfid: '',
          idProp: '',
          idAnimalMae: '',
          idLote: '',
          brinco: '',
          animal_Pai: '',
          numeroGestacoes:''
        },
        animais: [],
        racas: [],
        lotes: [],
        propriedades: [],
        isEdit: false,
        showDeleteModal: false,
        propriedadeToDelete: null
      }
    },
    methods: {
  
       //editar 
  editAnimal(animal) {
    this.isEdit = true;
    this.animal = { ...animal};
  },
      
  //adicionar
  submitForm() {
    if (this.isEdit) {
      //axios.put(`http://localhost:8000/produtores/${this.produtor.id}/editar/`, this.produtor)
      axios.put(`http://localhost:8000/animais/editar/${this.animal.id}/`, this.animal)
        .then(response => {
          this.animais = response.data;
          this.isEdit = false; // Redefinir o estado de edição pra não dar ruim
          this.animal = {
            idRaca: this.raca.id,
            observacoesRaca: '',
            sexo: '',
            peso: '',
            dataNascimento: '',
            dataMorte: '',
            observacoes: '',
            rfid: '',
            idProp: this.idProp.id,
            idAnimalMae: this.idAnimalMae.id,
            idLote: this.idLote.id,
            brinco: '',
            animal_Pai: '',
            numeroGestacoes:''
          };
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      console.log('Método POST')
      axios.post('http://localhost:8000/animais/', this.animal)
        .then(response => {
          this.animais = response.data;
          this.animal = {
            idRaca: this.raca.id,
            observacoesRaca: '',
            sexo: '',
            peso: '',
            dataNascimento: '',
            dataMorte: '',
            observacoes: '',
            rfid: '',
            idProp: this.idProp.id,
            idAnimalMae: this.idAnimalMae.id,
            idLote: this.idLote.id,
            brinco: '',
            animal_Pai: '',
            numeroGestacoes:''
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
        console.log("Pegou o delete?", this.animal)
        axios.delete(`http://localhost:8000/animais/deleteanimal/${this.animal.id}/`)
          .then(response => {
            this.animais= response.data
          })
          .catch(error => {
            console.log(error)
          })
      },
      confirmDelete(animal) {
        console.log("Que tem aqui?", animal)
        this.showDeleteModal = true
        this.animalToDelete = animal
      },
      deleteAnimalConfirmed() {
        console.log("E aqui?", this.animalToDelete)
        axios.delete(`http://localhost:8000/animais/deleteanimal/${this.animalToDelete.id}/`)
          .then(response => {
            this.animais = response.data
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
        window.location.href = '/animais'
      },
      fetchAnimal(id) {
        axios.get(`http://localhost:8000/animais/${id}/`)
          .then(response => {
            this.animal= response.data
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
      axios.get('http://localhost:8000/animais/')
        .then(response => {
          this.animais= response.data
        })
        .catch(error => {
          console.log(error)
        })
      axios.get('http://localhost:8000/racas/')
        .then(response => {
          this.racas = response.data
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
      axios.get('http://localhost:8000/propriedades/')
        .then(response => {
          this.propriedades = response.data
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
  getAnimalById() {
      return (id) => {
        const animal = this.animais.find(a => a.id === id);
        return animal ? animal.brinco : 'Desconhecido';
      }
    },
  getLoteById() {
      return (id) => {
        const lote = this.lotes.find(l => l.id === id);
        return lote ? lote.nomeLote : 'Desconhecido';
      }
    },

  getPropById() {
        return (id) => {
            const prop = this.propriedades.find(p => p.id === id);
            return prop ? prop.nomeProp : 'Desconhecido';
        }
    },

  getRacaById() {
        return (id) => {
            const raca = this.racas.find(r => r.id === id);
            return raca ? raca.nomeRaca: 'Desconhecido';
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
    width: max-content; /* Isso faz com que a div contenha exatamente a largura da tabela */
    margin: 0 auto; /* Isso centraliza a div em relação à página */
    text-align: center;
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
    text-align: center;
}

</style>
