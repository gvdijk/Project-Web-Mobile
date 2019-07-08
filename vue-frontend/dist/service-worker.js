importScripts("/precache-manifest.0e8711f1b000c3d60c07283fcfc65f62.js", "https://storage.googleapis.com/workbox-cdn/releases/3.6.3/workbox-sw.js");

workbox.skipWaiting();
workbox.clientsClaim();

workbox.precaching.precacheAndRoute(self.__precacheManifest);
workbox.routing.registerNavigationRoute('/index.html');

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
  
