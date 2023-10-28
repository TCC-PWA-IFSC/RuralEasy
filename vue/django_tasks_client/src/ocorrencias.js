import axios from "axios";

const API_URL = "http://localhost:8000/ocorrencias/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getOcorrencias() {
    return axios.get(`${API_URL}ocorrencias/`);
  }

  // Obter um produtor rural pelo id
  static getOcorrencia(id) {
    return axios.get(`${API_URL}ocorrencias/${id}/`);
  }

  // Criar um novo produtor rural
  static addOcorrencia(data) {
    return axios.post(`${API_URL}ocorrencias/`, data);
  }

  // Atualizar um produtor rural existente
  static updateOcorrencia(id, data) {
    return axios.put(`${API_URL}ocorrencias/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteOcorrencia(id) {
    return axios.delete(`${API_URL}ocorrencias/${id}/`);
  }
}