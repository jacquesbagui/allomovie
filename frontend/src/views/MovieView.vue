<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title>
            <h1>{{ movie.title }}</h1>
            <v-btn color="primary" @click="showEditModal = true">Éditer</v-btn>
          </v-card-title>
          <v-card-subtitle>{{ movie.description }}</v-card-subtitle>
          <v-card-text>{{ movie.actors }}</v-card-text>
        </v-card>

        <v-card class="mt-4">
          <v-card-title>Notes et Avis</v-card-title>
          <v-card-text>
            <div v-for="review in movie.reviews" :key="review.id">
              <v-rating :value="review.rating" color="yellow darken-3" dense readonly></v-rating>
              <p>{{ review.comment }}</p>
              <v-divider></v-divider>
            </div>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="showReviewModal = true">Ajouter un avis</v-btn>
          </v-card-actions>
        </v-card>

        <EditMovieModal
            v-if="showEditModal"
            :movie="movie"
            @close="showEditModal = false"
            @save="updateMovie"
        />

        <ReviewModal
            v-if="showReviewModal"
            :movieId="movie.id"
            @close="showReviewModal = false"
            @submit-review="addReview"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useMovieStore } from '@/stores/movie';
import EditMovieModal from '@/components/modal/EditMovieModal.vue';
import ReviewModal from '@/components/modal/ReviewModal.vue';

const store = useMovieStore();
const movie = computed(() => store.movieDetails);
const showEditModal = ref(false);
const showReviewModal = ref(false);

const updateMovie = (updatedMovie) => {
  store.updateMovie(movie.value.id, updatedMovie);
  showEditModal.value = false;
};

const addReview = (review) => {
  store.addReview(movie.value.id, review);
  showReviewModal.value = false;
};
</script>

<style scoped></style>
