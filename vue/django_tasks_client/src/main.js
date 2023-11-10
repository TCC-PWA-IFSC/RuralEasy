import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css';

const app = createApp(App);
app.use(router);
app.mount('#app');
navigator.serviceWorker.register('/service-worker.js');

if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
      navigator.serviceWorker.register('/service-worker.js').then(function(registration) {
          console.log('ServiceWorker registrado com sucesso com escopo: ', registration.scope);
      }, function(err) {
          console.log('Registro de ServiceWorker falhou: ', err);
      });
  });
}