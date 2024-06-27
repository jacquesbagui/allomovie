<template>
  <v-card class="mx-auto my-5" max-width="344">
    <v-card-title>{{ movie.title }}</v-card-title>
    <v-card-actions>
      <router-link :to="{ name: 'movie', params: { id: movie.id } }">
        <v-btn color="primary">Voir Détails</v-btn>
      </router-link>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      showDetails: false
    };
  },
  methods: {
    exploreMovie() {
      console.log('Explore movie:', this.movie);
    },
    toggleDetails() {
      this.showDetails = !this.showDetails;
    }
  }
};
</script>

<style scoped>
</style>
