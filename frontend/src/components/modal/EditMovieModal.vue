<template>
  <v-dialog v-model="dialog" max-width="600px">
    <v-card>
      <v-card-title>
        <span class="headline">Éditer le film</span>
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="save">
          <v-text-field
              v-model="localMovie.title"
              label="Titre"
              outlined
              required
          ></v-text-field>
          <v-textarea
              v-model="localMovie.description"
              label="Description"
              outlined
              auto-grow
              required
          ></v-textarea>
          <v-text-field
              v-model="actorsText"
              label="Acteurs (séparés par des virgules)"
              outlined
              required
          ></v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="close">Annuler</v-btn>
        <v-btn color="blue darken-1" text @click="save">Sauvegarder</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'EditMovieModal',
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      localMovie: {},
      dialog: true,
      actorsText: '',
    };
  },
  watch: {
    movie: {
      handler(newMovie) {
        this.localMovie = {
          ...newMovie
        };
        this.actorsText = newMovie.actors.map(actor => `${actor.first_name} ${actor.last_name}`).join(', ');
      },
      immediate: true,
    },
  },
  methods: {
    close() {
      this.dialog = false;
      this.$emit('close');
    },
    save() {
      const actorNames = this.actorsText.split(',').map(name => name.trim());

      this.localMovie.actors = actorNames.map(name => {
        const names = name.split(' ');
        const firstName = names.shift();
        const lastName = names.join(' ');
        return { first_name: firstName, last_name: lastName };
      });

      this.$emit('save', this.localMovie);
      this.close();
    },
  },
};
</script>

<style scoped></style>
