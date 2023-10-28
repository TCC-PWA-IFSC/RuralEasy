import axios from "axios";

const API_URL = "http://localhost:8000/vendas/"; // URL da sua API Django

export class ApiService {
  // Obter todos os produtores rurais
  static getVendas() {
    return axios.get(`${API_URL}vendas/`);
  }

  // Obter um produtor rural pelo id
  static getVenda(id) {
    return axios.get(`${API_URL}vendas/${id}/`);
  }

  // Criar um novo produtor rural
  static addVenda(data) {
    return axios.post(`${API_URL}vendas/`, data);
  }

  // Atualizar um produtor rural existente
  static updateVenda(id, data) {
    return axios.put(`${API_URL}vendas/${id}/`, data);
  }

  // Excluir um produtor rural
  static deleteVenda(id) {
    return axios.delete(`${API_URL}vendas/${id}/`);
  }
}