import axios from "axios";

const API_URL = "http://localhost:8000/movimentacoes/"; 

export class ApiService {
  static getLotes() {
    return axios.get(`${API_URL}movimentacoes/`);
  }

  static getLote(id) {
    return axios.get(`${API_URL}movimentacoes/${id}/`);
  }

  static addLote(data) {
    return axios.post(`${API_URL}movimentacoes/`, data);
  }

  static updateLote(id, data) {
    return axios.put(`${API_URL}movimentacoes/${id}/`, data);
  }

  static deleteLote(id) {
    return axios.delete(`${API_URL}movimentacoes/${id}/`);
  }
}