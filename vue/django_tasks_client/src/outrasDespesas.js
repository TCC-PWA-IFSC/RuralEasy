import axios from "axios";

const API_URL = "http://localhost:8000/outrasDespesas/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getPropriedadesRurais() {
    return axios.get(`${API_URL}outrasDespesas/`);
  }

  // Obter um produtor rural pelo id
  static getoutraDespesa(id) {
    return axios.get(`${API_URL}outrasDespesas/${id}/`);
  }

  // Criar um novo produtor rural
  static addoutraDespesa(data) {
    return axios.post(`${API_URL}outrasDespesas/`, data);
  }

  // Atualizar um produtor rural existente
  static updateoutraDespesa(id, data) {
    return axios.put(`${API_URL}outrasDespesas/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteoutraDespesa(id) {
    return axios.delete(`${API_URL}outrasDespesas/${id}/`);
  }
}