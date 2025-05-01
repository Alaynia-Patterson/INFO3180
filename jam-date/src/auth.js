import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000'; // Adjust if Flask backend runs on a different URL

export async function login(username, password) {
  const response = await axios.post(`${API_URL}/login`, {
    username,
    password
  });
  return response.data;
}

export async function register(data) {
  const response = await axios.post(`${API_URL}/register`, data);
  return response.data;
}

export async function logout(token) {
  const response = await axios.post(`${API_URL}/logout`, {}, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });
  return response.data;
}
