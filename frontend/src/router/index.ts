import { createRouter, createWebHistory } from 'vue-router'
import MovieView from "@/views/MovieView.vue";
import HomeView from "@/views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/movie/:id',
      name: 'movie',
      component: MovieView
    }
  ]
})

export default router
