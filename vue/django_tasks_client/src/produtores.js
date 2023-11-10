import axios from "axios";

const API_URL = "http://localhost:8000/produtores/";

export class ApiService {
  static getProdutoresRurais() {
    return axios.get(`${API_URL}produtores/`);
  }

  static getProdutorRural(id) {
    return axios.get(`${API_URL}produtores/${id}/`);
  }

  static addProdutorRural(data) {
    return axios.post(`${API_URL}produtores/`, data);
  }

  static updateProdutorRural(id, data) {
    return axios.put(`${API_URL}produtores/${id}/`, data);
  }

  static deleteProdutorRural(id) {
    return axios.delete(`${API_URL}produtores/${id}/`);
  }
}