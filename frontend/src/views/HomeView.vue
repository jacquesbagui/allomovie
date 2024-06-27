<template>
  <main>

    <div class="greetings">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" class="text-center">
            <h1 class="green">AlloMovie !</h1>
            <h3>Explorez, Regardez, Partagez: Bienvenue sur Allo Movie</h3>
          </v-col>
        </v-row>
      </v-container>
    </div>

    <v-container>
      <MovieList :movies="movies" :items-per-page="5" />
    </v-container>
  </main>
</template>
<script setup>
import { ref, onMounted } from 'vue';
import { useMovieStore } from '@/stores/movie';
import MovieList from '@/components/Movie/MovieList.vue';

const store = useMovieStore();
const movies = ref([]);

onMounted(async () => {
  await store.fetchMovies();
  movies.value = store.movies;
});
</script>

<style scoped>
  .green {
    color: #4caf50;
  }
  .greetings {
    margin-top: 40px;
    margin-bottom: 40px;
  }
</style>
