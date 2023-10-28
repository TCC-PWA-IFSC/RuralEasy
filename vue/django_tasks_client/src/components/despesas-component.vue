<template>
    <div class="container">
      <h1>Despesas Totais</h1>
      <p>Total de despesas em produtos: {{ totalProdutos }}</p>
      <p>Total de despesas em animais: {{ totalAnimais }}</p>
      <p>Total de outras despesas: {{ totalOutrasDespesas }}</p>
      <h2>Soma das despesas: {{ totalGeral }}</h2>

      <h3>Detalhes das Despesas</h3>
    <table>
      <thead>
        <tr>
          <th>Data da Despesa</th>
          <th>Valor da Despesa</th>
          <th>Observações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="despesa in despesas" :key="despesa.id">
          <td>{{ despesa.data }}</td>
          <td>{{ despesa.valor }}</td>
          <td>{{ despesa.observacao }}</td>
        </tr>
      </tbody>
    </table>

    </div>
  </template>
  
  <script>
import axios from 'axios';

export default {
  data() {
    return {
      compraProdutos: [],
      comprarAnimais: [],
      totalProdutos: 0,
      totalAnimais: 0,
      totalOutrasDespesas: 0,
      totalGeral: 0,
      despesas: []
    };
  },
  methods: {
    fetchDespesas() {

      axios.get('http://localhost:8000/outrasDespesas/')
  .then(response => {
    const outrasDespesas = response.data;
    this.totalOutrasDespesas = outrasDespesas.reduce((acc, despesa) => acc + despesa.valorOutraDespesa, 0);

    outrasDespesas.forEach(despesa => {
      this.despesas.push({
        id: despesa.id,
        data: despesa.dataDespesa,
        valor: despesa.valorOutraDespesa,
        observacao: despesa.descricaoOutraDespesa
      });
    });
    this.calculateTotalGeral();
  })
  .catch(error => {
    console.log(error);
  });
      axios.get('http://localhost:8000/compraProdutos/')
        .then(response => {
          this.compraProdutos = response.data;
          this.totalProdutos = this.compraProdutos.reduce((acc, compraProduto) => acc + (compraProduto.valorUnitario * compraProduto.qtdComprada), 0);

          this.compraProdutos.forEach(prod => {
            this.despesas.push({
              id: prod.id,
              data: prod.dataCompra,
              valor: prod.valorUnitario * prod.qtdComprada,
              observacao: prod.descricao
            });
          });
          this.calculateTotalGeral();
        })
        .catch(error => {
          console.log(error);
        });

      axios.get('http://localhost:8000/comprarAnimais/')
        .then(response => {
          this.comprarAnimais = response.data;
          this.totalAnimais = this.comprarAnimais.reduce((acc, comprarAnimal) => acc + comprarAnimal.valorComprarAnimal, 0);

          this.comprarAnimais.forEach(animal => {
            this.despesas.push({
              id: animal.id,
              data: animal.dataComprarAnimal,
              valor: animal.valorComprarAnimal,
              observacao: animal.observacoesComprarAnimal
            });
          });
          this.calculateTotalGeral();
        })
        .catch(error => {
          console.log(error);
        });
    },
    calculateTotalGeral() {
      this.totalGeral = this.totalProdutos + this.totalAnimais + this.totalOutrasDespesas;
    }
  },
  mounted() {
    this.fetchDespesas();
  }
};
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
