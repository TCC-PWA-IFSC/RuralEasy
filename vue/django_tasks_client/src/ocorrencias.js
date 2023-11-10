import axios from "axios";

const API_URL = "http://localhost:8000/ocorrencias/";

export class ApiService {
  static getOcorrencias() {
    return axios.get(`${API_URL}ocorrencias/`);
  }

  static getOcorrencia(id) {
    return axios.get(`${API_URL}ocorrencias/${id}/`);
  }

  static addOcorrencia(data) {
    return axios.post(`${API_URL}ocorrencias/`, data);
  }

  static updateOcorrencia(id, data) {
    return axios.put(`${API_URL}ocorrencias/${id}/`, data);
  }

  static deleteOcorrencia(id) {
    return axios.delete(`${API_URL}ocorrencias/${id}/`);
  }
}