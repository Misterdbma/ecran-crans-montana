/* Cache hors ligne : l'écran reste affiché si le wifi coupe */
const CACHE="cm-v2";
const SHELL=["./","index.html","qrcode.js","manifest.webmanifest","icon-192.png","icon-512.png","apple-touch-icon.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(SHELL)).then(()=>self.skipWaiting()));});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener("fetch",e=>{
  const u=new URL(e.request.url);
  if(e.request.method!=="GET"||u.origin!==location.origin) return;
  /* réseau d'abord (contenu frais), cache en secours */
  e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(CACHE).then(c=>c.put(e.request.url.split("?")[0],cp));return r;})
    .catch(()=>caches.match(e.request.url.split("?")[0]).then(m=>m||caches.match("index.html"))));
});
