import axios from 'axios';
import type { Movie } from '@/models/Movie';
import type { Review } from '@/models/Review';

const API_BASE_URL = import.meta.env.VUE_APP_API_BASE_URL;

const movieService = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export async function fetchMovies(): Promise<Movie[]> {
    try {
        const response = await movieService.get('/movies/');
        return response.data;
    } catch (error) {
        console.error('Error fetching movies:', error);
        throw error;
    }
}

export async function addReview(review: Review): Promise<void> {
    try {
        await movieService.post('/reviews/', review);
    } catch (error) {
        console.error('Error adding review:', error);
        throw error;
    }
}
