import axios from "axios";

const API_URL = "http://localhost:8000/propriedades/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getPropriedadesRurais() {
    return axios.get(`${API_URL}propriedades/`);
  }

  // Obter um produtor rural pelo id
  static getPropriedadeRural(id) {
    return axios.get(`${API_URL}propriedades/${id}/`);
  }

  // Criar um novo produtor rural
  static addPropriedadeRural(data) {
    return axios.post(`${API_URL}propriedades/`, data);
  }

  // Atualizar um produtor rural existente
  static updatePropriedadeRural(id, data) {
    return axios.put(`${API_URL}propriedades/${id}/`, data);
  }

  // Excluir um produtor rural
  static deletePropriedadeRural(id) {
    return axios.delete(`${API_URL}propriedades/${id}/`);
  }
}