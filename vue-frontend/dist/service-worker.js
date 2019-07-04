importScripts("/precache-manifest.92ccab52fee08443471a8a2347e670ea.js", "https://storage.googleapis.com/workbox-cdn/releases/3.6.3/workbox-sw.js");


console.log("Hi");


workbox.routing.registerRoute(
    new RegExp('^http://localhost\\:5000/project'),
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'api-project',
      plugins: [
        new workbox.cacheableResponse.Plugin({
          statuses: [200, 201, 404],
        //   headers: {
        //     'X-Is-Cacheable': 'true',
        //   },
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
        //   headers: {
        //     'X-Is-Cacheable': 'true',
        //   },
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
        //   headers: {
        //     'X-Is-Cacheable': 'true',
        //   },
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
        //   headers: {
        //     'X-Is-Cacheable': 'true',
        //   },
        })
      ]
    })
  );
  

  
