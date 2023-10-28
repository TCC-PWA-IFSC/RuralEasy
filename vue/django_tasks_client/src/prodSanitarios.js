import axios from "axios";

const API_URL = "http://localhost:8000/prodSanitarios/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getProdSanitarios() {
    return axios.get(`${API_URL}prodSanitarios/`);
  }

  // Obter um produtor rural pelo id
  static getProdSanitarios(id) {
    return axios.get(`${API_URL}prodSanitarios/${id}/`);
  }

  // Criar um novo produtor rural
  static addProdSanitario(data) {
    return axios.post(`${API_URL}prodSanitarios/`, data);
  }

  // Atualizar um produtor rural existente
  static updateProdSanitario(id, data) {
    return axios.put(`${API_URL}prodSanitarios/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteProdSanitario(id) {
    return axios.delete(`${API_URL}prodSanitarios/${id}/`);
  }
}