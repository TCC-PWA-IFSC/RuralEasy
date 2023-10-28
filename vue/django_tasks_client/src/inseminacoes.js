import axios from "axios";

const API_URL = "http://localhost:8000/inseminacoes/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getInseminacaos() {
    return axios.get(`${API_URL}inseminacoes/`);
  }

  // Obter um produtor rural pelo id
  static getInseminacao(id) {
    return axios.get(`${API_URL}inseminacoes/${id}/`);
  }

  // Criar um novo produtor rural
  static addInseminacao(data) {
    return axios.post(`${API_URL}inseminacoes/`, data);
  }

  // Atualizar um produtor rural existente
  static updateInseminacao(id, data) {
    return axios.put(`${API_URL}inseminacoes/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteInseminacao(id) {
    return axios.delete(`${API_URL}inseminacoes/${id}/`);
  }
}