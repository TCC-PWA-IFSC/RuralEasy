import axios from "axios";

const API_URL = "http://localhost:8000/racas/";

export class ApiService {
  static getRacas() {
    return axios.get(`${API_URL}racas/`);
  }

  static getRacas(id) {
    return axios.get(`${API_URL}racas/${id}/`);
  }

  static addRaca(data) {
    return axios.post(`${API_URL}racas/`, data);
  }

  static updateRaca(id, data) {
    return axios.put(`${API_URL}racas/${id}/`, data);
  }

  static deleteRaca(id) {
    return axios.delete(`${API_URL}racas/${id}/`);
  }
}