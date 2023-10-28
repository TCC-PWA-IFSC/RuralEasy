import axios from "axios";

const API_URL = "http://localhost:8000/lotes/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getLotes() {
    return axios.get(`${API_URL}lotes/`);
  }

  // Obter um produtor rural pelo id
  static getLote(id) {
    return axios.get(`${API_URL}lotes/${id}/`);
  }

  // Criar um novo produtor rural
  static addLote(data) {
    return axios.post(`${API_URL}lotes/`, data);
  }

  // Atualizar um produtor rural existente
  static updateLote(id, data) {
    return axios.put(`${API_URL}lotes/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteLote(id) {
    return axios.delete(`${API_URL}lotes/${id}/`);
  }
}