import axios from "axios";

const API_URL = "http://localhost:8000/pesagens/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getPesagens() {
    return axios.get(`${API_URL}pesagens/`);
  }

  // Obter um produtor rural pelo id
  static getPesagem(id) {
    return axios.get(`${API_URL}pesagens/${id}/`);
  }

  // Criar um novo produtor rural
  static addPesagem(data) {
    return axios.post(`${API_URL}pesagens/`, data);
  }

  // Atualizar um produtor rural existente
  static updatePesagem(id, data) {
    return axios.put(`${API_URL}pesagens/${id}/`, data);
  }

  // Excluir um produtor rural
  static deletePesagem(id) {
    return axios.delete(`${API_URL}pesagens/${id}/`);
  }
}