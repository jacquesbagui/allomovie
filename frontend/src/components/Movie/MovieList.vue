<template>
  <div>
    <v-row>
      <v-col
          v-for="(movie, index) in paginatedMovies"
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
</template>

<script>
import MovieItem from './MovieItem.vue';

export default {
  name: 'MovieList',
  components: {
    MovieItem,
  },
  props: {
    movies: {
      type: Array,
      required: true,
    },
    itemsPerPage: {
      type: Number,
      default: 5,
    },
  },
  data() {
    return {
      currentPage: 1,
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.movies.length / this.itemsPerPage);
    },
    paginatedMovies() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      return this.movies.slice(start, start + this.itemsPerPage);
    },
  },
  methods: {
    handlePageChange(page) {
      this.currentPage = page;
    },
  },
};
</script>

<style scoped>
</style>
