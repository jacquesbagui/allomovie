import { defineStore } from 'pinia';
import api from '@/services/api';
import type {Movie} from "@/models/Movie";
import type {Review} from "@/models/Review";

interface MoviesState {
    movies: Movie[];
    movieDetails: Movie | null;
}

export const useMovieStore = defineStore('movie', {
    state: (): MoviesState => ({
        movies: [],
        movieDetails: null,
    }),
    getters: {
        getMovieById: (state) => (id: number) => {
            return state.movies.find(movie => movie.id === id);
        },
        getReviewsForMovie: (state) => (movieId: number) => {
            const movie = state.movies.find(movie => movie.id === movieId);
            return movie ? movie.reviews : [];
        },
    },
    actions: {
        async fetchMovies() {
            try {
                const response = await api.get('/movies/');
                this.movies = response.data;
            } catch (error) {
                console.error('Failed to fetch movies:', error);
            }
        },
        async fetchMovieDetails(movieId: number) {
            try {
                const response = await api.get(`/movies/${movieId}/`);
                this.movieDetails = {...response.data};
            } catch (error) {
                console.error('Failed to fetch movie details:', error);
            }
        },
        async updateMovie(movieId: number, updatedMovie: Partial<Movie>) {
            try {
                const response = await api.put(`/movies/${movieId}/`, updatedMovie);
                this.movieDetails = {...response.data};
                this.movies = this.movies.map(movie =>
                    movie.id === movieId ? { ...movie, ...updatedMovie } : movie
                );
            } catch (error) {
                console.error('Failed to update movie details:', error);
            }
        },
        async addReview(review: Review) {
            try {
                console.log('review : ', review)
                const response = await api.post(`/reviews/`, review);
                console.log("response.data :", response.data)
                console.log("this.movieDetails :", this.movieDetails)
                if (this.movieDetails) {
                    this.movieDetails.reviews.push(response.data);
                } else {
                    console.warn('Movie details not available.');
                }
            } catch (error) {
                console.error('Failed to add review:', error);
            }
        },
    },
});
