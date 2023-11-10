import axios from "axios";

const API_URL = "http://localhost:8000/vendas/";

export class ApiService {
  static getVendas() {
    return axios.get(`${API_URL}vendas/`);
  }

  static getVenda(id) {
    return axios.get(`${API_URL}vendas/${id}/`);
  }

  static addVenda(data) {
    return axios.post(`${API_URL}vendas/`, data);
  }

  static updateVenda(id, data) {
    return axios.put(`${API_URL}vendas/${id}/`, data);
  }

  static deleteVenda(id) {
    return axios.delete(`${API_URL}vendas/${id}/`);
  }
}