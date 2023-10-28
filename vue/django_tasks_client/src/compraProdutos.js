import axios from "axios";

const API_URL = "http://localhost:8000/compraProdutos/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getCompraProdutos() {
    return axios.get(`${API_URL}compraProdutos/`);
  }

  // Obter um produtor rural pelo id
  static getCompraProduto(id) {
    return axios.get(`${API_URL}compraProdutos/${id}/`);
  }

  // Criar um novo produtor rural
  static addCompraProduto(data) {
    return axios.post(`${API_URL}compraProdutos/`, data);
  }

  // Atualizar um produtor rural existente
  static updateCompraProduto(id, data) {
    return axios.put(`${API_URL}compraProduto/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteCompraProduto(id) {
    return axios.delete(`${API_URL}compraProdutos/${id}/`);
  }
}