import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000'; // Update if using a different backend URL or port

// Create an Axios instance with default settings
const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Attach the token if it exists
export function setAuthToken(token) {
  if (token) {
    apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  } else {
    delete apiClient.defaults.headers.common['Authorization'];
  }
}

// GET request
export function get(endpoint) {
  return apiClient.get(endpoint);
}

// POST request
export function post(endpoint, data) {
  return apiClient.post(endpoint, data);
}

// PUT request
export function put(endpoint, data) {
  return apiClient.put(endpoint, data);
}

// DELETE request
export function remove(endpoint) {
  return apiClient.delete(endpoint);
}
