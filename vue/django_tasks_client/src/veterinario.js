import axios from "axios";

const API_URL = "http://localhost:8000/veterinarios/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getVeterinarios() {
    return axios.get(`${API_URL}veterinarios/`);
  }

  // Obter um produtor rural pelo id
  static getVeterinarios(id) {
    return axios.get(`${API_URL}veterinarios/${id}/`);
  }

  // Criar um novo produtor rural
  static addVeterinario(data) {
    return axios.post(`${API_URL}veterinarios/`, data);
  }

  // Atualizar um produtor rural existente
  static updateVeterinario(id, data) {
    return axios.put(`${API_URL}veterinarios/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteVeterinario(id) {
    return axios.delete(`${API_URL}veterinarios/${id}/`);
  }
}