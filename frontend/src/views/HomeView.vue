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
<script>
import MovieList from '@/components/Movie/MovieList.vue';

export default {
  components: {
    MovieList,
  },
  data() {
    return {
      movies: [
        { title: 'Film 1', description: 'Description du film 1' },
        { title: 'Film 2', description: 'Description du film 2' },
        { title: 'Film 3', description: 'Description du film 3' },
        { title: 'Film 4', description: 'Description du film 4' },
        { title: 'Film 5', description: 'Description du film 5' },
        { title: 'Film 6', description: 'Description du film 6' },
        { title: 'Film 7', description: 'Description du film 7' },
        { title: 'Film 8', description: 'Description du film 8' },
        { title: 'Film 9', description: 'Description du film 9' },
        { title: 'Film 10', description: 'Description du film 10' },
      ]
    };
  }
};
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
