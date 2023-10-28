<template>
  <div>
    <h1>Produtor Rural</h1>
    <ul>
      <li v-for="produtor in produtores" :key="produtor.id">
        {{ produtor.nomeProd }} - {{ produtor.cpf }} - {{ produtor.email }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      produtores: [],
    };
  },
  mounted() {
    axios
      .get('http://localhost:8000/api/produtores/') // endpoint da API do Django
      .then((response) => {
        this.produtores = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>