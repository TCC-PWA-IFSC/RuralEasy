// Versão do cache - você pode atualizar isso para refletir as mudanças no conteúdo do app
const CACHE_VERSION = 'v1';

// Recursos a serem armazenados em cache durante a instalação do Service Worker
const CACHE_RESOURCES = [
  '/',
  '/index.html',
  //'/css/styles.css',
  //'/js/app.js',
  //'/img/logo.png',
  // Adicione outros recursos conforme necessário
];

// Evento de instalação
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_VERSION)
      .then((cache) => {
        return cache.addAll(CACHE_RESOURCES);
      })
  );
});

// Evento de ativação
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (CACHE_VERSION !== cacheName) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Evento de fetch (recuperação)
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        return response || fetch(event.request);
      })
  );
});
