importScripts("/precache-manifest.8e116a3b831841ee279324c86f2aaf9c.js", "https://storage.googleapis.com/workbox-cdn/releases/3.6.3/workbox-sw.js");



workbox.precaching.precacheAndRoute(self.__precacheManifest);
workbox.routing.registerNavigationRoute('/index.html');

const bodyConstructor = (text) => {
    return {
        body: text,
        icon: '/img/icons/android-chrome-192x192.png',
        image: '/img/autumn-forest.png',
        vibrate: [300, 200, 300],
        badge: '/img/icons/plint-badge-96x96.png'
    }
}

const bgSyncPlugin = new workbox.backgroundSync.Plugin('myQueueName', {
    maxRetentionTime: 60,
    callbacks: {
        requestWillEnqueue: (storableRequest) => {
            self.registration.showNotification('Je bent offline', bodyConstructor(
                'De actie is lokaal verwerkt en zal naar de server worden verzonden wanneer de verbinding is herstelt'
            ));
        },
        requestWillReplay: (storableRequest) => {},
        queueDidReplay: (storableRequestArray) => {
            self.registration.showNotification('Verbinding herstelt', bodyConstructor(
                'De actie is verzonden naar de server.'
            ));
        },
    },
});

workbox.routing.registerRoute(
    new RegExp('^http://localhost\\:5000'),
    new workbox.strategies.NetworkFirst({
        cacheName: 'api-get',
        plugins: [
            new workbox.cacheableResponse.Plugin({
                statuses: [200, 201, 404],
            })
        ]
    }),
    'GET'
);

workbox.routing.registerRoute(
    new RegExp('^http://localhost\\:5000'),
    new workbox.strategies.NetworkOnly({
        cacheName: 'api-post',
        plugins: [bgSyncPlugin]
    }),
    'POST'
);

workbox.routing.registerRoute(
    new RegExp('^http://localhost\\:5000'),
    new workbox.strategies.NetworkOnly({
        cacheName: 'api-put',
        plugins: [bgSyncPlugin]
    }),
    'PUT'
);

workbox.routing.registerRoute(
    new RegExp('^http://localhost\\:5000'),
    new workbox.strategies.NetworkOnly({
        cacheName: 'api-delete',
        plugins: [bgSyncPlugin]
    }),
    'DELETE'
);

// workbox.routing.registerRoute(
//     new RegExp('^http://localhost\\:5000/project'),
//     new workbox.strategies.NetworkOnly({
//         cacheName: 'api-post-project',
//         plugins: [bgSyncPlugin]
//     }),
//     'POST'
// );

// workbox.routing.registerRoute(
//     new RegExp('^http://localhost\\:5000/post'),
//     new workbox.strategies.NetworkOnly({
//         cacheName: 'api-post-post',
//         plugins: [bgSyncPlugin]
//     }),
//     'POST'
// );

// workbox.routing.registerRoute(
//     new RegExp('^http://localhost\\:5000/comment'),
//     new workbox.strategies.NetworkOnly({
//         cacheName: 'api-post-comment',
//         plugins: [bgSyncPlugin]
//     }),
//     'POST'
// );

// workbox.routing.registerRoute(
//     new RegExp('^http://localhost\\:5000/user'),
//     new workbox.strategies.NetworkOnly({
//         cacheName: 'api-post-user',
//         plugins: [bgSyncPlugin]
//     }),
//     'POST'
// );



workbox.routing.registerRoute(
  /\.(?:js|css)$/,
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'static-resources',
  })
);

workbox.routing.registerRoute(
    /\.(?:png|gif|jpg|jpeg|webp|svg)$/,
    new workbox.strategies.CacheFirst({
      cacheName: 'images',
      plugins: [
        new workbox.expiration.Plugin({
          maxEntries: 60,
          maxAgeSeconds: 30 * 24 * 60 * 60, // 30 Days
        }),
      ],
    })
  );




// workbox.routing.registerRoute(
//     new RegExp('^http://localhost\\:5000/project'),
//     new workbox.strategies.NetworkFirst({
//         cacheName: 'api-get-project',
//         plugins: [
//             new workbox.cacheableResponse.Plugin({
//                 statuses: [200, 201, 404],
//             })
//         ]
//     }),
//     'GET'
// );


// workbox.routing.registerRoute(
//     new RegExp('^http://localhost\\:5000/post'),
//     new workbox.strategies.NetworkFirst({
//         cacheName: 'api-get-post',
//         plugins: [
//             new workbox.cacheableResponse.Plugin({
//                 statuses: [200, 201, 404],
//             })
//         ]
//     }),
//     'GET'
// );


// workbox.routing.registerRoute(
//     new RegExp('^http://localhost\\:5000/comment'),
//     new workbox.strategies.NetworkFirst({
//         cacheName: 'api-get-comment',
//         plugins: [
//             new workbox.cacheableResponse.Plugin({
//                 statuses: [200, 201, 404],
//             })
//         ]
//     }),
//     'GET'
// );


// workbox.routing.registerRoute(
//     new RegExp('^http://localhost\\:5000/user'),
//     new workbox.strategies.NetworkFirst({
//         cacheName: 'api-get-user',
//         plugins: [
//             new workbox.cacheableResponse.Plugin({
//                 statuses: [200, 201, 404],
//             })
//         ]
//     }),
//     'GET'
// );

