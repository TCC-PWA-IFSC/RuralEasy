import axios from "axios";

const API_URL = "http://localhost:8000/comprarAnimais/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getComprarAnimals() {
    return axios.get(`${API_URL}comprarAnimais/`);
  }

  // Obter um produtor rural pelo id
  static getComprarAnimal(id) {
    return axios.get(`${API_URL}comprarAnimais/${id}/`);
  }

  // Criar um novo produtor rural
  static addComprarAnimal(data) {
    return axios.post(`${API_URL}comprarAnimais/`, data);
  }

  // Atualizar um produtor rural existente
  static updateComprarAnimal(id, data) {
    return axios.put(`${API_URL}comprarAnimais/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteComprarAnimal(id) {
    return axios.delete(`${API_URL}comprarAnimais/${id}/`);
  }
}