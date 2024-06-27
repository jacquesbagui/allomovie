import { defineStore } from 'pinia';
import api from '@/services/api';
import type { Movie } from '@/models/Movie';
import type { Review } from '@/models/Review';

interface MoviesState {
    movies: Movie[];
    movieDetails: Movie | null;
    currentPage: number;
    totalPages: number;
    itemsPerPage: number;
}

export const useMovieStore = defineStore('movie', {
    state: (): MoviesState => ({
        movies: [],
        movieDetails: null,
        currentPage: 1,
        totalPages: 0,
        itemsPerPage: 5,
    }),
    getters: {
        getMovieById: (state) => (id: number) => {
            return state.movies.find((movie) => movie.id === id);
        },
        getReviewsForMovie: (state) => (movieId: number) => {
            const movie = state.movies.find((movie) => movie.id === movieId);
            return movie ? movie.reviews : [];
        },
    },
    actions: {
        async fetchMovies(page: number = this.currentPage) {
            try {
                const response = await api.get('/movies/', {
                    params: {
                        page,
                        page_size: this.itemsPerPage,
                    },
                });
                this.movies = response.data.results;
                this.totalPages = Math.ceil(response.data.count / this.itemsPerPage);
                this.currentPage = page;
            } catch (error) {
                console.error('Failed to fetch movies:', error);
            }
        },
        async fetchMovieDetails(movieId: number) {
            try {
                const response = await api.get(`/movies/${movieId}/`);
                this.movieDetails = { ...response.data };
            } catch (error) {
                console.error('Failed to fetch movie details:', error);
            }
        },
        async updateMovie(movieId: number, updatedMovie: Partial<Movie>) {
            try {
                const response = await api.put(`/movies/${movieId}/`, updatedMovie);
                this.movieDetails = { ...response.data };
                this.movies = this.movies.map((movie) =>
                    movie.id === movieId ? { ...movie, ...updatedMovie } : movie
                );
            } catch (error) {
                console.error('Failed to update movie details:', error);
            }
        },
        async addReview(review: Review) {
            try {
                const response = await api.post(`/reviews/`, review);
                if (this.movieDetails) {
                    this.movieDetails.reviews.push(response.data);
                } else {
                    console.warn('Movie details not available.');
                }
            } catch (error) {
                console.error('Failed to add review:', error);
            }
        },
        setCurrentPage(page: number) {
            this.currentPage = page;
        },
    },
});
