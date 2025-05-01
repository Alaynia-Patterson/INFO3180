<template>
  <div class="login-page">
    <div class="login-container">
      <h1 class="logo">Jam-Date</h1>
      <h2>Login</h2>
      <form @submit.prevent="loginUser">
        <input type="text" v-model="username" placeholder="Username" required>
        <input type="password" v-model="password" placeholder="Password" required>
        <button type="submit">Login</button>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>
  </div>
</template>

<script>
import { login } from '../api';

export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: '',
      message: ''
    };
  },
  methods: {
    async loginUser() {
      try {
        const response = await login(this.username, this.password);
        this.message = 'Login successful';
        localStorage.setItem('token', response.access_token);
        this.$router.push('/profile'); // Adjust as needed
      } catch (error) {
        this.message = error.response?.data?.error || 'Login failed.';
      }
    }
  }
};
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  background-image: url('@/assets/Login.jpg'); 
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-container {
  padding: 40px;
  border-radius: 12px;
  color: white;
  width: 100%;
  max-width: 400px;
  text-align: center;
}

.logo {
  font-size: 32px;
  margin-bottom: 20px;
}

form input {
  display: block;
  width: 100%;
  padding: 12px;
  margin-bottom: 15px;
  border-radius: 6px;
  border: none;
  font-size: 1rem;
}

button {
  padding: 12px;
  width: 100%;
  background-color: rgb(132, 209, 245);
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease;
}

button:hover {
  background-color: rgb(95, 189, 233);
}

p {
margin-top: 15px;
  color: red;
  font-weight: bold;
}
</style>
