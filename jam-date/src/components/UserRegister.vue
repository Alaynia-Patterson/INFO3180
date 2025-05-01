<template>
  <div class="register-page">
    <div class="register-container">
      <h1 class="logo">Jam-Date</h1>
      <h2>Register</h2>
      <form @submit.prevent="registerUser">
        <input type="text" v-model="form.username" placeholder="Username" required>
        <input type="password" v-model="form.password" placeholder="Password" required>
        <input type="text" v-model="form.name" placeholder="Full Name" required>
        <input type="email" v-model="form.email" placeholder="Email" required>
        
        <!-- Accept only JPG/JPEG/PNG -->
        <input
          type="file"
          accept=".jpg,.jpeg,.png"
          @change="handlePhoto"
          required
        >

        <button type="submit">Register</button>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>
  </div>
</template>

<script>
import { register } from '../api';

export default {
  name: 'RegisterPage',
  data() {
    return {
      form: {
        username: '',
        password: '',
        name: '',
        email: '',
        photo: ''  // Will hold base64 or file name if needed
      },
      message: ''
    };
  },
  methods: {
    handlePhoto(event) {
      const file = event.target.files[0];
      if (file && ['image/jpeg', 'image/png', 'image/jpg'].includes(file.type)) {
        this.form.photo = file;
      } else {
        this.message = 'Please upload a JPG, JPEG, or PNG image.';
        event.target.value = null;
      }
    },
    async registerUser() {
      try {
        const formData = new FormData();
        formData.append('username', this.form.username);
        formData.append('password', this.form.password);
        formData.append('name', this.form.name);
        formData.append('email', this.form.email);
        formData.append('photo', this.form.photo);

        const response = await register(formData);
        this.message = response.message;
        this.$router.push('/login');
      } catch (error) {
        this.message = error.response?.data?.error || 'Registration failed.';
      }
    }
  }
};
</script>

<style scoped>
.register-page {
  min-height: 100vh;
  background-image: url('@/assets/Registration.jpeg'); 
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.register-container {
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

form input[type="file"] {
  padding: 10px;
  background-color: white;
}

button {
  padding: 12px;
  width: 100%;
  background-color:rgb(132, 209, 245);
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease;
}

button:hover {
  background-color:rgb(132, 209, 245);
}

p {
  margin-top: 15px;
  color: red;
  font-weight: bold;
}
</style>

