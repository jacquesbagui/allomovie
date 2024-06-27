import { createPinia, defineStore } from 'pinia';
import type { Movie } from '@/models/Movie';
import type { Review } from '@/models/Review';

interface MoviesState {
    movies: Movie[];
}

export const useMoviesStore = defineStore({
    id: 'movies',
    state: (): MoviesState => ({
        movies: [],
    }),
    getters: {
        getMovieById: (state) => (id: number) => {
            return state.movies.find(movie => movie.id === id);
        },
    },
    actions: {
        fetchMovies() {
            const movies: Movie[] = []; // Fetch movies
            this.movies = movies;
        },
        addReview(review: Review) {
            console.log('Adding review:', review);
        },
    },
});

export const initializeStore = () => {
    return createPinia();
};
