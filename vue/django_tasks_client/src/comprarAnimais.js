import axios from "axios";

const API_URL = "http://localhost:8000/comprarAnimais/";

export class ApiService {
  static getComprarAnimals() {
    return axios.get(`${API_URL}comprarAnimais/`);
  }

  static getComprarAnimal(id) {
    return axios.get(`${API_URL}comprarAnimais/${id}/`);
  }

  static addComprarAnimal(data) {
    return axios.post(`${API_URL}comprarAnimais/`, data);
  }

  static updateComprarAnimal(id, data) {
    return axios.put(`${API_URL}comprarAnimais/${id}/`, data);
  }

  static deleteComprarAnimal(id) {
    return axios.delete(`${API_URL}comprarAnimais/${id}/`);
  }
}