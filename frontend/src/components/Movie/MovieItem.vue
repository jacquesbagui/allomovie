<template>
  <v-card class="mx-auto my-5" max-width="344">
    <v-card-title>{{ movie.title }}</v-card-title>
    <v-card-actions>
      <v-btn color="green-lighten-2" @click="exploreMovie">Voir plus</v-btn>
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
