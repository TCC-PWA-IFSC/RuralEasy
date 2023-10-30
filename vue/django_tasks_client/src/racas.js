import axios from "axios";

//const API_URL = "http://localhost:8000/racas/"; // URL da sua API Django
const API_URL = "https://8af2-138-186-119-107.ngrok.io/racas/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getRacas() {
    return axios.get(`${API_URL}racas/`);
  }

  // Obter um produtor rural pelo id
  static getRacas(id) {
    return axios.get(`${API_URL}racas/${id}/`);
  }

  // Criar um novo produtor rural
  static addRaca(data) {
    return axios.post(`${API_URL}racas/`, data);
  }

  // Atualizar um produtor rural existente
  static updateRaca(id, data) {
    return axios.put(`${API_URL}racas/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteRaca(id) {
    return axios.delete(`${API_URL}racas/${id}/`);
  }
}