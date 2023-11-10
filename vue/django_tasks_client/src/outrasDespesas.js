import axios from "axios";

const API_URL = "http://localhost:8000/outrasDespesas/";

export class ApiService {
  static getPropriedadesRurais() {
    return axios.get(`${API_URL}outrasDespesas/`);
  }

  static getoutraDespesa(id) {
    return axios.get(`${API_URL}outrasDespesas/${id}/`);
  }

  static addoutraDespesa(data) {
    return axios.post(`${API_URL}outrasDespesas/`, data);
  }

  static updateoutraDespesa(id, data) {
    return axios.put(`${API_URL}outrasDespesas/${id}/`, data);
  }

  static deleteoutraDespesa(id) {
    return axios.delete(`${API_URL}outrasDespesas/${id}/`);
  }
}