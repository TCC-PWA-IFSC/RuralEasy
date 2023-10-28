import axios from "axios";

const API_URL = "http://localhost:8000/animais/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getAnimais() {
    return axios.get(`${API_URL}animais/`);
  }

  // Obter um produtor rural pelo id
  static getAnimal(id) {
    return axios.get(`${API_URL}animais/${id}/`);
  }

  // Criar um novo produtor rural
  static addAnimal(data) {
    return axios.post(`${API_URL}animais/`, data);
  }

  // Atualizar um produtor rural existente
  static updateAnimal(id, data) {
    return axios.put(`${API_URL}animais/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteAnimal(id) {
    return axios.delete(`${API_URL}animais/${id}/`);
  }
}