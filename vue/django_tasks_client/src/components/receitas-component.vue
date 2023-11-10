<template>
    <div class="container">
      <h2>Resumo das Receitas</h2>

      <div class="total-em-caixa">
        <h3>Total em caixa: {{ totalEmCaixa.toFixed(2) }}</h3>
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
                <td>{{ venda.idAnimalVenda }}</td>
                <td>
                </td>
              </tr>
            </tbody>
          </table>
      </div>
    </div>
</template>

<script>
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  data() {
    return {
      vendas: [],
      totalEmCaixa: 0
    }
  },
  methods: {
    calculateTotalEmCaixa() {
      let total = 0
      this.vendas.forEach(venda => {
        const dataRecebimento = new Date(venda.dataRecebimento)
        if (dataRecebimento <= new Date()) {
          total += (venda.pesoAnimalVenda/15) * venda.precoAtualArrobaKg
        }
      })
      this.totalEmCaixa = total
    }
  },
  mounted() {
    axios.get('http://localhost:8000/vendas/')
      .then(response => {
        this.vendas = response.data
        this.calculateTotalEmCaixa()
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
    display: inline-block;
    width: 100%;
    text-align: center;
}


h1, h2 {
    width: 100%;
}

</style>

