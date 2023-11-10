import axios from "axios";

const API_URL = "http://localhost:8000/propriedades/";

export class ApiService {
  static getPropriedadesRurais() {
    return axios.get(`${API_URL}propriedades/`);
  }

  static getPropriedadeRural(id) {
    return axios.get(`${API_URL}propriedades/${id}/`);
  }

  static addPropriedadeRural(data) {
    return axios.post(`${API_URL}propriedades/`, data);
  }

  static updatePropriedadeRural(id, data) {
    return axios.put(`${API_URL}propriedades/${id}/`, data);
  }

  static deletePropriedadeRural(id) {
    return axios.delete(`${API_URL}propriedades/${id}/`);
  }
}