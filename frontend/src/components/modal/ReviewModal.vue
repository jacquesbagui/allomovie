<template>
  <v-dialog v-model="dialog" max-width="500px">
    <v-card>
      <v-card-title>
        <span class="headline">Ajouter un avis</span>
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="submitReview">
          <v-rating
              v-model="review.rating"
              color="yellow darken-3"
              dense
              length="5"
              half-increments
              required
          ></v-rating>
          <v-textarea
              v-model="review.comment"
              label="Commentaire"
              auto-grow
              outlined
              required
          ></v-textarea>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="close">Annuler</v-btn>
        <v-btn color="blue darken-1" text @click="submitReview">Valider</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'ReviewModal',
  props: {
    movieId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      review: {
        rating: 0,
        comment: '',
      },
      dialog: true,
    };
  },
  methods: {
    close() {
      this.dialog = false;
      this.$emit('close');
    },
    submitReview() {
      this.$emit('submit-review', this.review);
      this.close();
    },
  },
};
</script>

<style scoped></style>
