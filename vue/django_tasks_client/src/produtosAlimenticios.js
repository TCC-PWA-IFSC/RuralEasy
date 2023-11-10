import axios from "axios";

const API_URL = "http://localhost:8000/produtosAlimenticios/";

export class ApiService {
  static getProdutosAlimenticios() {
    return axios.get(`${API_URL}produtosAlimenticios/`);
  }

  static getProdutosAlimenticios(id) {
    return axios.get(`${API_URL}produtosAlimenticios/${id}/`);
  }

  static addProdutoAlimenticio(data) {
    return axios.post(`${API_URL}produtosAlimenticios/`, data);
  }

  static updateProdutoAlimenticio(id, data) {
    return axios.put(`${API_URL}produtosAlimenticios/${id}/`, data);
  }

  static deleteProdutoAlimenticio(id) {
    return axios.delete(`${API_URL}produtosAlimenticios/${id}/`);
  }
}