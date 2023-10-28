<template>
        <div class="container">
            <h2>Cadastro de Pesagem</h2>
            <form @submit.prevent="submitForm">
                <div>
                        <label for="idAnimal">ID Brinco Animal:</label>
                        <select id="idAnimal" v-model="pesagem.idAnimal" required>
                        <option value="">Selecione um animal</option>
                        <option v-for="idAnimal in animais" :value="idAnimal.id" :key="idAnimal.id">{{ idAnimal.brinco }}</option>
                        </select>
                </div>
            <div>
                    <label for="peso">Peso (KG):</label>
                    <input type="peso" id="peso" v-model="pesagem.peso" required>
                </div>
                <div>
                    <label for="dataPesagem">Data da pesagem:</label>
                    <input type="date" id="dataPesagem" v-model="pesagem.dataPesagem" required>
                </div>
                <button type="submit">Salvar</button>
                <button v-if="isEdit" @click.prevent="cancelEdit">Cancelar</button>
            </form>
        </div>
    <br>

    <div class="table">
    <h1>Lista de Pesagens</h1>
    <table>
        <thead>
            <tr>
                <th>ID Brinco Animal</th>
                <th>Peso</th>
                <th>Data da pesagem</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="pesagem in pesagens" :key="pesagem.id">
                <td>{{ pesagem.idAnimal }}</td>
                <td>{{ pesagem.peso }}</td>
                <td>{{ pesagem.dataPesagem }}</td>
                <td>
                    <button @click.prevent="editPesagem(pesagem)">Editar</button>
                    <button @click.prevent="confirmDelete(pesagem)">Excluir</button>
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
                pesagem: {
                    idAnimal: '',
                    peso: '',
                    dataPesagem: '',
                },
                pesagens: [],
                animais: [],
                isEdit: false,
                showDeleteModal: false,
                pesagemToDelete: null
            }
        },

        methods: {

    getAnimalById(id) {
        // Procura o animal com base no ID
        let animal = this.animais.find(a => a.id === id);
        // Retorna o brinco do animal se encontrado; caso contrário, retorna uma string vazia
        return animal ? animal.brinco : '';
    },
    
             //editar 
    editPesagem(pesagem) {
        this.isEdit = true;
        this.pesagem = { ...pesagem };
    },
            
    //adicionar
    submitForm() {
        if (this.isEdit) {
            axios.put(`http://localhost:8000/pesagens/editar/${this.pesagem.id}/`, this.pesagem)
                .then(response => {
                    this.pesagens = response.data;
                    this.isEdit = false;
                    this.pesagem = {
                        idAnimal: 'this.animal.idAnimal',
                        peso: '',
                        dataPesagem: ''
                    };
                })
                .catch(error => {
                    console.log(error);
                });
        } else {
            axios.post('http://localhost:8000/pesagens/', this.pesagem)
                .then(response => {
                    this.pesagens = response.data;
                    this.pesagem = {
                        idAnimal: 'this.animal.idAnimal',
                        peso: '',
                        dataPesagem: ''
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
    
            deletePesagem() {
                axios.delete(`http://localhost:8000/pesagens/deletepesagem/${this.pesagem.id}/`)
                    .then(response => {
                        this.pesagens = response.data
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
            confirmDelete(pesagem) {
                if (window.confirm("Você tem certeza de que deseja excluir esta pesagem?")) {
                    this.pesagemToDelete = pesagem;
                    this.deletePesagemConfirmed();
                }
            },
            deletePesagemConfirmed() {
                axios.delete(`http://localhost:8000/pesagens/deletepesagem/${this.pesagemToDelete.id}/`)
                    .then(response => {
                        this.pesagens = response.data
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
            fetchPesagem(id) {
                axios.get(`http://localhost:8000/pesagens/${id}/`)
                    .then(response => {
                        this.pesagem = response.data;
                    })
                    .catch(error => {
                        console.log(error);
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
        axios.get('http://localhost:8000/pesagens/')
            .then(response => {
                    this.pesagens = response.data
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
