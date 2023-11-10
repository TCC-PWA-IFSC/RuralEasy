import axios from "axios";

const API_URL = "http://localhost:8000/aplicarProdutosSanitarios/";

export class ApiService {
  static getAplicarProdutoSanitarios() {
    return axios.get(`${API_URL}aplicarProdutosSanitarios/`);
  }

  static getAplicarProdutoSanitario(id) {
    return axios.get(`${API_URL}aplicarProdutosSanitarios/${id}/`);
  }

  static addAplicarProdutoSanitario(data) {
    return axios.post(`${API_URL}aplicarProdutosSanitarios/`, data);
  }

  static updateAplicarProdutoSanitario(id, data) {
    return axios.put(`${API_URL}aplicarProdutosSanitarios/${id}/`, data);
  }

  static deleteAplicarProdutoSanitario(id) {
    return axios.delete(`${API_URL}aplicarProdutosSanitarios/${id}/`);
  }
}