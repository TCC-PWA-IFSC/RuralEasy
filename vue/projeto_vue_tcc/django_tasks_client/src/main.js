import { createApp } from 'vue'
// import the root component App from a single-file component.
import App from './App.vue'
//import axios from 'axios'
//import Vue from 'vue'
import router from './router'
//import "./assets/main.scss";
import 'bootstrap/dist/css/bootstrap.min.css';


//import VueRouter from 'vue-router'
//import {routes} from './router.js'
//import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

//import 'bootstrap/dist/css/bootstrap.css'
//import 'bootstrap-vue/dist/bootstrap-vue.css'

//Vue.use(VueRouter)

/*const router = new VueRouter({
  routes
});


*/

/*createApp(App).use(router);

//const app = createApp(App);
app.config.globalProperties.axios=axios
app.mount('#app');*/

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
/*new Vue({
  router,
  render: h => h(App)
}).$mount('#app')*/

/*const app = createApp(App)
/*app.use(BootstrapVue)
app.use(BootstrapVueIcons)*///
//app.use(router)
///////////////////////////////////app.config.globalProperties.axios=axios
//app.mount('#app')