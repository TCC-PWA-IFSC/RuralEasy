import axios from "axios";

const API_URL = "http://localhost:8000/lotes/";

export class ApiService {
  static getLotes() {
    return axios.get(`${API_URL}lotes/`);
  }

  static getLote(id) {
    return axios.get(`${API_URL}lotes/${id}/`);
  }

  static addLote(data) {
    return axios.post(`${API_URL}lotes/`, data);
  }

  static updateLote(id, data) {
    return axios.put(`${API_URL}lotes/${id}/`, data);
  }

  static deleteLote(id) {
    return axios.delete(`${API_URL}lotes/${id}/`);
  }
}