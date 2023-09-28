import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap/dist/js/bootstrap';
import 'bootstrap-icons/font/bootstrap-icons.css'
import '/src/style.css'
import '/src/bootstrap-custom.scss'


const app = createApp(App)
app.use(router)
app.mount('#app')
