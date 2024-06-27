<template>
  <div v-if="movies.length > 0">
    <v-row>
      <v-col
          v-for="(movie, index) in movies"
          :key="index"
          cols="12"
          sm="6"
          md="4"
      >
        <MovieItem :movie="movie" />
      </v-col>
    </v-row>
    <v-pagination
        v-model="currentPage"
        :length="totalPages"
        @input="handlePageChange"
    ></v-pagination>
  </div>
  <div class="text-center mt-8" v-else>
    <v-card
        class="mx-auto"
        max-width="444"
        subtitle="Chargement en cours ..."
        disabled
        link
    ></v-card>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useMovieStore } from '@/stores/movie';
import MovieItem from './MovieItem.vue';

const store = useMovieStore();

const movies = ref([]);
const currentPage = ref(1);
const totalPages = ref(0);

onMounted(async () => {
  await store.fetchMovies();
  movies.value = store.movies;
  currentPage.value = store.currentPage;
  totalPages.value = store.totalPages;
});

watch(currentPage, async (newPage) => {
  await store.fetchMovies(newPage);
  movies.value = store.movies;
});

const handlePageChange = async (page) => {
  currentPage.value = page;
  store.setCurrentPage(page);
  await store.fetchMovies(page);
  movies.value = store.movies;
};
</script>
