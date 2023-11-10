import axios from "axios";

const API_URL = "http://localhost:8000/pesagens/"; 

export class ApiService {
  static getPesagens() {
    return axios.get(`${API_URL}pesagens/`);
  }

  static getPesagem(id) {
    return axios.get(`${API_URL}pesagens/${id}/`);
  }

  static addPesagem(data) {
    return axios.post(`${API_URL}pesagens/`, data);
  }

  static updatePesagem(id, data) {
    return axios.put(`${API_URL}pesagens/${id}/`, data);
  }

  static deletePesagem(id) {
    return axios.delete(`${API_URL}pesagens/${id}/`);
  }
}