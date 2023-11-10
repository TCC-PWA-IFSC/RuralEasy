import axios from "axios";

const API_URL = "http://localhost:8000/suplementacoes/";

export class ApiService {
  static getSuplementacoes() {
    return axios.get(`${API_URL}suplementacoes/`);
  }

  static getSuplementacoes(id) {
    return axios.get(`${API_URL}suplementacoes/${id}/`);
  }

  static addSuplementacao(data) {
    return axios.post(`${API_URL}suplementacoes/`, data);
  }

  static updateSuplementacao(id, data) {
    return axios.put(`${API_URL}suplementacoes/${id}/`, data);
  }

  static deleteSuplementacao(id) {
    return axios.delete(`${API_URL}suplementacoes/${id}/`);
  }
}