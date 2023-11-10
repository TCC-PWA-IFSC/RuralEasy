import axios from "axios";

const API_URL = "http://localhost:8000/prodSanitarios/";

export class ApiService {
  static getProdSanitarios() {
    return axios.get(`${API_URL}prodSanitarios/`);
  }

  static getProdSanitarios(id) {
    return axios.get(`${API_URL}prodSanitarios/${id}/`);
  }

  static addProdSanitario(data) {
    return axios.post(`${API_URL}prodSanitarios/`, data);
  }

  static updateProdSanitario(id, data) {
    return axios.put(`${API_URL}prodSanitarios/${id}/`, data);
  }

  static deleteProdSanitario(id) {
    return axios.delete(`${API_URL}prodSanitarios/${id}/`);
  }
}