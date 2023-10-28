import axios from "axios";

const API_URL = "http://localhost:8000/produtores/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getProdutoresRurais() {
    return axios.get(`${API_URL}produtores/`);
  }

  // Obter um produtor rural pelo id
  static getProdutorRural(id) {
    return axios.get(`${API_URL}produtores/${id}/`);
  }

  // Criar um novo produtor rural
  static addProdutorRural(data) {
    return axios.post(`${API_URL}produtores/`, data);
  }

  // Atualizar um produtor rural existente
  static updateProdutorRural(id, data) {
    return axios.put(`${API_URL}produtores/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteProdutorRural(id) {
    return axios.delete(`${API_URL}produtores/${id}/`);
  }
}