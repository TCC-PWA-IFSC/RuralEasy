import axios from "axios";

const API_URL = "http://localhost:8000/suplementacoes/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getSuplementacoes() {
    return axios.get(`${API_URL}suplementacoes/`);
  }

  // Obter um produtor rural pelo id
  static getSuplementacoes(id) {
    return axios.get(`${API_URL}suplementacoes/${id}/`);
  }

  // Criar um novo produtor rural
  static addSuplementacao(data) {
    return axios.post(`${API_URL}suplementacoes/`, data);
  }

  // Atualizar um produtor rural existente
  static updateSuplementacao(id, data) {
    return axios.put(`${API_URL}suplementacoes/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteSuplementacao(id) {
    return axios.delete(`${API_URL}suplementacoes/${id}/`);
  }
}