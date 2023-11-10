import axios from "axios";

const API_URL = "http://localhost:8000/animais/";

export class ApiService {
  static getAnimais() {
    return axios.get(`${API_URL}animais/`);
  }

  static getAnimal(id) {
    return axios.get(`${API_URL}animais/${id}/`);
  }

  static addAnimal(data) {
    return axios.post(`${API_URL}animais/`, data);
  }

  static updateAnimal(id, data) {
    return axios.put(`${API_URL}animais/${id}/`, data);
  }

  static deleteAnimal(id) {
    return axios.delete(`${API_URL}animais/${id}/`);
  }
}