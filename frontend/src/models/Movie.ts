import type {Review} from "@/models/Review";
import type {Actor} from "@/models/Actor";

export interface Movie {
    id: number;
    title: string;
    description: string;
    actors: Actor[];
    averageRating: number;
    reviews: Review[];
}
