

workbox.routing.registerRoute(
    new RegExp('^http://localhost\\:5000/project'),
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'api-project',
      plugins: [
        new workbox.cacheableResponse.Plugin({
          statuses: [200, 201, 404],
        })
      ]
    })
  );
  

workbox.routing.registerRoute(
    new RegExp('^http://localhost\\:5000/post'),
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'api-post',
      plugins: [
        new workbox.cacheableResponse.Plugin({
          statuses: [200, 201, 404],
        })
      ]
    })
  );
  

workbox.routing.registerRoute(
    new RegExp('^http://localhost\\:5000/comment'),
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'api-comment',
      plugins: [
        new workbox.cacheableResponse.Plugin({
          statuses: [200, 201, 404],
        })
      ]
    })
  );
  

workbox.routing.registerRoute(
    new RegExp('^http://localhost\\:5000/user'),
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'api-user',
      plugins: [
        new workbox.cacheableResponse.Plugin({
          statuses: [200, 201, 404],
        })
      ]
    })
  );
  

