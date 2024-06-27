<template>
  <v-container>
    <v-btn color="blue darken-1" text @click="goBack">
      Home Page
    </v-btn>
    <v-row v-if="movie" class="mt-4">
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title>
            <h1>{{ movie.title }}</h1>
          </v-card-title>
          <v-card-subtitle>{{ movie.description }}</v-card-subtitle>
          <v-card-text>
            <strong>Acteurs :</strong>
            <ul class="mx-10 my-5">
              <li v-for="(actor, index) in movie.actors" :key="index">
                {{ actor.first_name }} {{ actor.last_name }}
              </li>
            </ul>
          </v-card-text>

          <div class="mx-5 my-5">
            <v-btn color="blue darken-1" @click="showEditModal = true">Éditer</v-btn>
          </div>
        </v-card>

        <v-card class="mt-4">
          <v-card-title>Notes et Avis</v-card-title>

          <div class="d-flex align-center flex-column my-auto">
            <div class="text-h2 mt-5">
              {{ movie.averageRating }}
              <span class="text-h6 ml-n3">/5</span>
            </div>
            <Rating v-model="movie.averageRating" readonly/>
            <div class="px-3">{{ movie.reviews ? movie.reviews.length : 0 }} ratings</div>
          </div>
          <v-card-text>
            <div v-for="review in movie.reviews" :key="review.id" class="my-10">
              <Rating v-model="review.grade" readonly/>
              <p class="mt-4">{{ review.comment }}</p>
              <v-divider></v-divider>
            </div>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="addingReview = true">Ajouter un avis</v-btn>
          </v-card-actions>
        </v-card>

        <EditMovieModal
            v-if="showEditModal"
            :movie="movie"
            @close="showEditModal = false"
            @save="updateMovie"
        />

        <v-dialog v-model="addingReview" max-width="500px">
          <v-card>
            <v-card-title>
              <span class="headline">Ajouter un avis</span>
            </v-card-title>
            <v-card-text>
              <v-form @submit.prevent="submitReview">
                <Rating v-model="newReview.grade" dense></Rating>
                <v-alert v-if="gradeError" type="error" class="mt-2">La note est obligatoire.</v-alert>
                <div class="mt-4">
                  <v-textarea
                      v-model="newReview.comment"
                      label="Commentaire"
                      auto-grow
                      outlined
                      required
                  ></v-textarea>
                </div>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeAddingReview">Annuler</v-btn>
              <v-btn color="blue darken-1" text @click="submitReview">Valider</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import Rating from 'primevue/rating';
import { useRoute, useRouter } from 'vue-router';
import { ref, onMounted, computed, watchEffect } from 'vue';
import { useMovieStore } from '@/stores/movie';
import EditMovieModal from '@/components/modal/EditMovieModal.vue';

const store = useMovieStore();
const route = useRoute();
const router = useRouter();
const showEditModal = ref(false);
const addingReview = ref(false);
const newReview = ref({ grade: 0, comment: '' });
const gradeError = ref(false);

watchEffect(() => {
  const movieId = Number(route.params.id);
  if (movieId) {
    store.fetchMovieDetails(movieId);
  }
});

const movie = computed(() => store.movieDetails);

const updateMovie = (updatedMovie) => {
  store.updateMovie(movie.value.id, updatedMovie);
  showEditModal.value = false;
};

const submitReview = async () => {
  if (newReview.value.grade === 0) {
    gradeError.value = true;
    return;
  }
  gradeError.value = false;

  try {
    await store.addReview({
      movie: movie.value.id,
      grade: newReview.value.grade,
      comment: newReview.value.comment,
    });
    addingReview.value = false;
    newReview.value = { grade: 0, comment: '' }; // Reset the form
    showSnackbar('Avis ajouté avec succès', 'success');
  } catch (error) {
    console.error('Failed to add review:', error);
    showSnackbar('Erreur lors de l\'ajout de l\'avis', 'error');
  }
};

const closeAddingReview = () => {
  addingReview.value = false;
  newReview.value = { grade: 0, comment: '' }; // Reset the form
  gradeError.value = false;
};

// Gestion de la snackbar
const snackbar = ref({
  show: false,
  message: '',
  color: '',
  timeout: 3000,
  showClose: true,
});

const showSnackbar = (message, color) => {
  snackbar.value.message = message;
  snackbar.value.color = color;
  snackbar.value.show = true;
};

const goBack = () => {
  router.go(-1);
};
</script>

<style scoped></style>
