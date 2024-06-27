import type {Review} from "@/models/Review";

export interface Movie {
    id: number;
    title: string;
    description: string;
    actors: string[];
    averageRating: number;
    reviews: Review[];
}
