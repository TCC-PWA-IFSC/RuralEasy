import axios from "axios";

const API_URL = "http://localhost:8000/compraProdutos/";

export class ApiService {
  static getCompraProdutos() {
    return axios.get(`${API_URL}compraProdutos/`);
  }

  static getCompraProduto(id) {
    return axios.get(`${API_URL}compraProdutos/${id}/`);
  }

  static addCompraProduto(data) {
    return axios.post(`${API_URL}compraProdutos/`, data);
  }

  static updateCompraProduto(id, data) {
    return axios.put(`${API_URL}compraProduto/${id}/`, data);
  }

  static deleteCompraProduto(id) {
    return axios.delete(`${API_URL}compraProdutos/${id}/`);
  }
}