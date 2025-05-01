import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/AppHome.vue'
import Register from '../components/UserRegister.vue'
import Login from '../components/UserLogin.vue'
import Logout from '../components/UserLogout.vue'
import UserProfiles from '../components/UserProfiles.vue'
import NewProfile from '../components/NewProfile.vue'
import ProfileDetails from '../components/ProfileDetails.vue'
import ProfileFavourites from '../components/ProfileFavourites.vue'
import AppReports from '../components/AppReports.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/register', component: Register },
  { path: '/login', component: Login },
  { path: '/logout', component: Logout },
  { path: '/users/:user_id', component: UserProfiles, props: true },
  { path: '/profiles/new', component: NewProfile },
  { path: '/profiles/:profile_id', component: ProfileDetails, props: true },
  { path: '/profiles/favourites', component: ProfileFavourites },
  { path: '/reports', name: 'reports', component: AppReports }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
