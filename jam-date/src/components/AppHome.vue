<template>
  <div class="home">
    <nav class="navbar">
      <h2 class="logo">Jam-Date</h2>
      <ul>
        <li><router-link to="/login">Login</router-link></li>
        <li><router-link to="/register">Register</router-link></li>
        <li><router-link to="/reports">Reports</router-link></li>
      </ul>
    </nav>

    <div class="overlay">
      <transition name="fade">
        <div class="overlay-content">
          <h1>Welcome to Jam-Date</h1>
          <p>Find your perfect match!</p>
          <div class="buttons">
            <router-link to="/login"><button>Login</button></router-link>
            <router-link to="/register"><button>Register</button></router-link>
            <router-link to="/reports"><button>View Reports</button></router-link>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AppHome',
  mounted() {
    // force transition on mount
    this.$nextTick(() => {
      document.querySelector('.overlay-content').classList.add('visible');
    });
  }
};
</script>

<style scoped>
.home {
  height: 100vh;
  width: 100%;
  background-image: url('@/assets/Homepage.jpg');
  background-size: cover;
  background-position: center;
  position: relative;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  background-color: rgba(0, 0, 0, 0.6);
  position: absolute;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 1;
  flex-wrap: wrap;
}

.logo {
  font-size: 24px;
  font-weight: bold;
  color: #fff;
}

.navbar ul {
  list-style: none;
  display: flex;
  gap: 15px;
  margin: 0;
  padding: 0;
}

.navbar li {
  display: inline;
}

.navbar a {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
}

.navbar a:hover {
  text-decoration: underline;
}

.overlay {
  text-align: center;
  background-color: rgba(0, 0, 0, 0.55);
  padding: 40px;
  border-radius: 12px;
  z-index: 0;
  max-width: 90%;
  animation: fadeIn 2s ease-in;
}

.overlay-content {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 1s ease, transform 1s ease;
}

.overlay-content.visible {
  opacity: 1;
  transform: translateY(0);
}

.buttons {
  margin-top: 20px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
}

.buttons button {
  padding: 12px 24px;
  font-size: 1rem;
  cursor: pointer;
  border: none;
  border-radius: 6px;
  background-color: #ff3366;
  color: white;
  transition: background 0.3s ease;
}

.buttons button:hover {
  background-color: #cc0044;
}

/* Fade transition for <transition name="fade"> */
.fade-enter-active, .fade-leave-active {
  transition: opacity 1s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
    align-items: flex-start;
    padding: 10px 20px;
  }

  .logo {
    margin-bottom: 10px;
  }

  .navbar ul {
    flex-direction: column;
    gap: 10px;
  }

  .overlay {
    padding: 20px;
  }

  .overlay h1 {
    font-size: 1.8rem;
  }

  .overlay p {
    font-size: 1rem;
  }

  .buttons button {
    width: 100%;
    max-width: 200px;
  }
}
</style>
