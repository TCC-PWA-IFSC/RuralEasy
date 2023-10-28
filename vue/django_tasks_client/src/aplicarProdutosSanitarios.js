import axios from "axios";

const API_URL = "http://localhost:8000/aplicarProdutosSanitarios/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getAplicarProdutoSanitarios() {
    return axios.get(`${API_URL}aplicarProdutosSanitarios/`);
  }

  // Obter um produtor rural pelo id
  static getAplicarProdutoSanitario(id) {
    return axios.get(`${API_URL}aplicarProdutosSanitarios/${id}/`);
  }

  // Criar um novo produtor rural
  static addAplicarProdutoSanitario(data) {
    return axios.post(`${API_URL}aplicarProdutosSanitarios/`, data);
  }

  // Atualizar um produtor rural existente
  static updateAplicarProdutoSanitario(id, data) {
    return axios.put(`${API_URL}aplicarProdutosSanitarios/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteAplicarProdutoSanitario(id) {
    return axios.delete(`${API_URL}aplicarProdutosSanitarios/${id}/`);
  }
}