import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/';

export default {
  getProdutores() {
    return axios.get(BASE_URL + 'produtor/');
  },
  getProdutor(id) {
    return axios.get(BASE_URL + `produtor/${id}/`);
  },
  createProdutor(data) {
    return axios.post(BASE_URL + 'produtor/', data);
  },
  updateProdutor(id, data) {
    return axios.put(BASE_URL + `produtor/${id}/`, data);
  },
  deleteProdutor(id) {
    return axios.delete(BASE_URL + `produtor/${id}/`);
  },
  getPropriedades() {
    return axios.get(BASE_URL + 'propriedade/');
  },
  getPropriedade(id) {
    return axios.get(BASE_URL + `propriedade/${id}/`);
  },
  createPropriedade(data) {
    return axios.post(BASE_URL + 'propriedade/', data);
  },
  updatePropriedade(id, data) {
    return axios.put(BASE_URL + `propriedade/${id}/`, data);
  },
  deletePropriedade(id) {
    return axios.delete(BASE_URL + `propriedade/${id}/`);
  },
};