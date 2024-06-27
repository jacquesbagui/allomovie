import axios from 'axios';

const API_BASE_URL = import.meta.env.VUE_APP_API_BASE_URL || 'http://localhost:8000/api';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export default api;
