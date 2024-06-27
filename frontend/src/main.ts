import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});

const vuetify = createVuetify({
    icons: {
        iconfont: 'md',
    },
    components,
    directives
})

app.use(createPinia())
app.use(router)
app.use(vuetify)

app.mount('#app')
