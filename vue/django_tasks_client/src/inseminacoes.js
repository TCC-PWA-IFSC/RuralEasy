import axios from "axios";

const API_URL = "http://localhost:8000/inseminacoes/";

export class ApiService {
  static getInseminacaos() {
    return axios.get(`${API_URL}inseminacoes/`);
  }

  static getInseminacao(id) {
    return axios.get(`${API_URL}inseminacoes/${id}/`);
  }

  static addInseminacao(data) {
    return axios.post(`${API_URL}inseminacoes/`, data);
  }

  static updateInseminacao(id, data) {
    return axios.put(`${API_URL}inseminacoes/${id}/`, data);
  }

  static deleteInseminacao(id) {
    return axios.delete(`${API_URL}inseminacoes/${id}/`);
  }
}