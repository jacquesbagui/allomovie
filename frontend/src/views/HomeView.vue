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
      <MovieList />
    </v-container>
  </main>
</template>

<script setup>
import {ref, onMounted} from 'vue';
import {useMovieStore} from '@/stores/movie';
import MovieList from '@/components/Movie/MovieList.vue';
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
