import axios from "axios";

const API_URL = "http://localhost:8000/produtosAlimenticios/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getProdutosAlimenticios() {
    return axios.get(`${API_URL}produtosAlimenticios/`);
  }

  // Obter um produtor rural pelo id
  static getProdutosAlimenticios(id) {
    return axios.get(`${API_URL}produtosAlimenticios/${id}/`);
  }

  // Criar um novo produtor rural
  static addProdutoAlimenticio(data) {
    return axios.post(`${API_URL}produtosAlimenticios/`, data);
  }

  // Atualizar um produtor rural existente
  static updateProdutoAlimenticio(id, data) {
    return axios.put(`${API_URL}produtosAlimenticios/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteProdutoAlimenticio(id) {
    return axios.delete(`${API_URL}produtosAlimenticios/${id}/`);
  }
}