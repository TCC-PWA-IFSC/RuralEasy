import axios from "axios";

const API_URL = "http://localhost:8000/veterinarios/";

export class ApiService {
  static getVeterinarios() {
    return axios.get(`${API_URL}veterinarios/`);
  }

  static getVeterinarios(id) {
    return axios.get(`${API_URL}veterinarios/${id}/`);
  }

  static addVeterinario(data) {
    return axios.post(`${API_URL}veterinarios/`, data);
  }

  static updateVeterinario(id, data) {
    return axios.put(`${API_URL}veterinarios/${id}/`, data);
  }

  static deleteVeterinario(id) {
    return axios.delete(`${API_URL}veterinarios/${id}/`);
  }
}