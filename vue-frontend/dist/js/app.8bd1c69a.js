(function(e){function t(t){for(var o,a,s=t[0],c=t[1],u=t[2],l=0,d=[];l<s.length;l++)a=s[l],r[a]&&d.push(r[a][0]),r[a]=0;for(o in c)Object.prototype.hasOwnProperty.call(c,o)&&(e[o]=c[o]);p&&p(t);while(d.length)d.shift()();return i.push.apply(i,u||[]),n()}function n(){for(var e,t=0;t<i.length;t++){for(var n=i[t],o=!0,a=1;a<n.length;a++){var s=n[a];0!==r[s]&&(o=!1)}o&&(i.splice(t--,1),e=c(c.s=n[0]))}return e}var o={},a={app:0},r={app:0},i=[];function s(e){return c.p+"js/"+({about:"about"}[e]||e)+"."+{about:"5d4aced2"}[e]+".js"}function c(t){if(o[t])return o[t].exports;var n=o[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,c),n.l=!0,n.exports}c.e=function(e){var t=[],n={about:1};a[e]?t.push(a[e]):0!==a[e]&&n[e]&&t.push(a[e]=new Promise(function(t,n){for(var o="css/"+({about:"about"}[e]||e)+"."+{about:"c92745e2"}[e]+".css",r=c.p+o,i=document.getElementsByTagName("link"),s=0;s<i.length;s++){var u=i[s],l=u.getAttribute("data-href")||u.getAttribute("href");if("stylesheet"===u.rel&&(l===o||l===r))return t()}var d=document.getElementsByTagName("style");for(s=0;s<d.length;s++){u=d[s],l=u.getAttribute("data-href");if(l===o||l===r)return t()}var p=document.createElement("link");p.rel="stylesheet",p.type="text/css",p.onload=t,p.onerror=function(t){var o=t&&t.target&&t.target.src||r,i=new Error("Loading CSS chunk "+e+" failed.\n("+o+")");i.code="CSS_CHUNK_LOAD_FAILED",i.request=o,delete a[e],p.parentNode.removeChild(p),n(i)},p.href=r;var f=document.getElementsByTagName("head")[0];f.appendChild(p)}).then(function(){a[e]=0}));var o=r[e];if(0!==o)if(o)t.push(o[2]);else{var i=new Promise(function(t,n){o=r[e]=[t,n]});t.push(o[2]=i);var u,l=document.createElement("script");l.charset="utf-8",l.timeout=120,c.nc&&l.setAttribute("nonce",c.nc),l.src=s(e),u=function(t){l.onerror=l.onload=null,clearTimeout(d);var n=r[e];if(0!==n){if(n){var o=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src,i=new Error("Loading chunk "+e+" failed.\n("+o+": "+a+")");i.type=o,i.request=a,n[1](i)}r[e]=void 0}};var d=setTimeout(function(){u({type:"timeout",target:l})},12e4);l.onerror=l.onload=u,document.head.appendChild(l)}return Promise.all(t)},c.m=e,c.c=o,c.d=function(e,t,n){c.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},c.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.t=function(e,t){if(1&t&&(e=c(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(c.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)c.d(n,o,function(t){return e[t]}.bind(null,o));return n},c.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return c.d(t,"a",t),t},c.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},c.p="/",c.oe=function(e){throw console.error(e),e};var u=window["webpackJsonp"]=window["webpackJsonp"]||[],l=u.push.bind(u);u.push=t,u=u.slice();for(var d=0;d<u.length;d++)t(u[d]);var p=l;i.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"034f":function(e,t,n){"use strict";var o=n("64a9"),a=n.n(o);a.a},"09e5":function(e,t,n){"use strict";var o=n("e86e"),a=n.n(o);a.a},"31e3":function(e,t,n){"use strict";var o=n("7f35"),a=n.n(o);a.a},4826:function(e,t,n){e.exports=n.p+"img/Logo_Full_White.8facd64e.svg"},"56d7":function(e,t,n){"use strict";n.r(t);n("cadf"),n("551c"),n("f751"),n("097d");var o=n("2b0e"),a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[e.modalActive?n("Modal",{attrs:{modaltype:e.modalType,modaldata:e.modalData},on:{closeModal:e.onModalClose}}):e._e(),n("Sidebar",{attrs:{extended:e.sidebarExtended},on:{"set-extended":e.onExtentionChange}}),n("Header",{on:{requestModal:e.openModal}}),n("div",{staticClass:"all-content"},[n("router-view",{on:{requestModal:e.openModal}})],1),n("Footer")],1)},r=[],i=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("header",[o("div",{staticClass:"header-content"},[o("div",{staticClass:"logo-wrapper"},[o("router-link",{attrs:{to:"/"}},[o("img",{attrs:{src:n("4826"),alt:"logo"}})])],1),o("div",{staticClass:"search-wrapper"},[o("i",{staticClass:"fa fa-search"}),o("form",{attrs:{action:"#"},on:{submit:function(t){return t.preventDefault(),e.searchAction(t)}}},[o("input",{directives:[{name:"model",rawName:"v-model",value:e.searchQuery,expression:"searchQuery"}],attrs:{type:"search",name:"headerSearch",placeholder:"Doorzoek de website"},domProps:{value:e.searchQuery},on:{input:function(t){t.target.composing||(e.searchQuery=t.target.value)}}})])]),o("div",{staticClass:"search-filler"}),o("div",{staticClass:"account-wrapper"},[o("span",{staticClass:"account-label search-label",on:{click:e.toggleSearch}},[o("i",{staticClass:"fa fa-search"}),o("span",[e._v("Zoeken")])]),e.authenticated?e._e():o("span",{staticClass:"account-label",attrs:{title:"Inloggen"},on:{click:function(t){return e.$emit("requestModal","login",{})}}},[o("i",{staticClass:"fa fa-sign-in"}),o("span",[e._v("Inloggen")])]),e.authenticated?o("router-link",{staticClass:"account-label",attrs:{to:"/profile",title:"Profiel"}},[o("i",{staticClass:"fa fa-user"}),o("span",[e._v("Profiel")])]):e._e(),e.authenticated?o("span",{staticClass:"account-label",attrs:{title:"Uitloggen"},on:{click:e.logout}},[o("i",{staticClass:"fa fa-sign-out"}),o("span",[e._v("Uitloggen")])]):e._e(),e.authenticated?e._e():o("router-link",{staticClass:"account-label",attrs:{to:"/register",title:"Registreren"}},[o("i",{staticClass:"fa fa-paper-plane"}),o("span",[e._v("Registreren")])])],1)]),o("div",{staticClass:"mobile-search-wrapper",class:{"mobile-search-expanded":e.searchExpanded}},[o("div",{staticClass:"mobile-search"},[o("i",{staticClass:"fa fa-search"}),o("form",{attrs:{action:"#"},on:{submit:function(t){return t.preventDefault(),e.searchAction(t)}}},[o("input",{directives:[{name:"model",rawName:"v-model",value:e.searchQuery,expression:"searchQuery"}],attrs:{type:"search",name:"headerSearch",placeholder:"Doorzoek de website"},domProps:{value:e.searchQuery},on:{input:function(t){t.target.composing||(e.searchQuery=t.target.value)}}})])])])])},s=[],c={name:"Header",methods:{toggleMenu:function(){this.menuCollapse=!this.menuCollapse},logout:function(){this.$store.dispatch("logoutUser"),this.$router.push({path:"/"})},toggleSearch:function(){this.searchExpanded=!this.searchExpanded},searchAction:function(){this.searchQuery.length>0&&this.$router.push({path:"/search?q=".concat(this.searchQuery)})}},data:function(){return{menuCollapse:!0,searchQuery:"",searchExpanded:!1}},computed:{authenticated:function(){return this.$store.getters.authenticated}}},u=c,l=(n("31e3"),n("2877")),d=Object(l["a"])(u,i,s,!1,null,"306e7d2a",null),p=d.exports,f=function(){var e=this,t=e.$createElement;e._self._c;return e._m(0)},m=[function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("footer",[o("div",{staticClass:"footer-filler"},[o("div",{staticClass:"footer-content"},[o("div",{staticClass:"logo-wrapper"},[o("img",{attrs:{src:n("4826"),alt:"logo"}})]),o("span",{staticClass:"footer-message"},[e._v("Project Planner Ⓒ2019")])])])])}],h={name:"Footer"},v=h,g=(n("09e5"),Object(l["a"])(v,f,m,!1,null,"1f396a02",null)),b=g.exports,_=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("aside",{class:{"hide-aside":!e.extended}},[n("div",{staticClass:"side-extender",class:{"left-float":!e.extended}},[e.extended?n("div",{on:{click:function(t){return e.$emit("set-extended",!1)}}},[n("span",[e._v("«")])]):n("div",{on:{click:function(t){return e.$emit("set-extended",!0)}}},[n("span",[e._v("»")])])]),n("div",{staticClass:"side-pane"},[n("router-link",{staticClass:"side-pane-title",attrs:{to:"/explore"}},[n("a",[e._v("Explore")])])],1),n("div",{staticClass:"side-pane"},[n("router-link",{staticClass:"side-pane-title",attrs:{to:"/new"}},[n("a",[e._v("Nieuw Project")])])],1)])},k=[],y={name:"Sidebar",data:function(){return{authenticated:!0,extendedInfo:!1,extendedProjects:!0,extendedRecent:!0,myProjects:[],userprojects:[],recentProjects:[{id:1,title:"Invisiline"},{id:2,title:"Barbarapapa"},{id:3,title:"De beste titel voor een lange beschrijving"}]}},methods:{toggleInfoVisibility:function(){this.extendedInfo=!this.extendedInfo},toggleMyProjectsVisibility:function(){this.extendedProjects=!this.extendedProjects},toggleRecentProjectsVisibility:function(){this.extendedRecent=!this.extendedRecent}},props:["extended"]},j=y,w=(n("fa3e"),Object(l["a"])(j,_,k,!1,null,"51df9f38",null)),C=w.exports,x=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"modal"},[n("div",{staticClass:"modal-wrapper"},[n("div",{staticClass:"modal-centerer"},[n("div",{staticClass:"modal-body"},[n("div",{staticClass:"modal-close fa fa-times",on:{click:function(t){return e.$emit("closeModal")}}}),"login"==e.modaltype?n("Login",{on:{closeModal:function(t){return e.$emit("closeModal")}}}):e._e(),"delete"==e.modaltype?n("Delete",{attrs:{body:e.modaldata},on:{closeModal:function(t){return e.$emit("closeModal")}}}):e._e(),"create"==e.modaltype?n("Create",{attrs:{body:e.modaldata},on:{closeModal:function(t){return e.$emit("closeModal")}}}):e._e(),"edit"==e.modaltype?n("Edit",{attrs:{body:e.modaldata},on:{closeModal:function(t){return e.$emit("closeModal")}}}):e._e()],1)])])])},T=[],P=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"modal-content"},[n("form",{attrs:{action:"#"},on:{submit:function(t){return t.preventDefault(),e.loginAction(t)}}},[n("div",{staticClass:"modal-header"},[e._v("Inloggen")]),n("div",{staticClass:"modal-text"},[n("label",[e._v("Gebruikersnaam")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.username,expression:"username"}],attrs:{type:"text",placeholder:"Gebruikersnaam"},domProps:{value:e.username},on:{input:function(t){t.target.composing||(e.username=t.target.value)}}}),n("label",[e._v("Wachtwoord")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.password,expression:"password"}],attrs:{type:"password",placeholder:"Wachtwoord"},domProps:{value:e.password},on:{input:function(t){t.target.composing||(e.password=t.target.value)}}}),n("label",[e._v("\n                Nog geen account? \n                "),n("span",{staticClass:"register-link",attrs:{to:"/register"},on:{click:e.goToRegister}},[e._v("Registreer hier")])])]),n("div",{staticClass:"modal-actions"},[n("button",{staticClass:"modal-button",attrs:{type:"submit"}},[e._v("Inloggen")]),n("transition",{attrs:{name:"fade"}},[n("span",{directives:[{name:"show",rawName:"v-show",value:e.error,expression:"error"}],staticClass:"error"},[e._v(e._s(e.errorMsg))])])],1)])])},I=[],D={name:"Login",data:function(){return{username:"",password:"",error:!1,errorMsg:""}},methods:{goToRegister:function(){this.$emit("closeModal"),this.$router.push({path:"/register"})},loginAction:function(){var e=this;this.$store.dispatch("loginUser",{user:this.username,pass:this.password}).then(function(t){e.$emit("closeModal"),e.$router.push({path:"/explore"})}).catch(function(t){e.errorMsg=t,e.showError()})},showError:function(){var e=this;this.error=!0,setTimeout(function(){e.error=!1},5e3)}}},$=D,E=(n("d98d"),Object(l["a"])($,P,I,!1,null,"67ffc733",null)),A=E.exports,M=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"modal-content"},[n("div",{staticClass:"modal-header"},[e._v("Verwijderen")]),n("div",{staticClass:"modal-text"},[e._v("\n        Weet je zeker dat je \n        "),"post"==e.body.type?n("span",[e._v("dit bericht")]):e._e(),"project"==e.body.type?n("span",[e._v("dit project")]):e._e(),"projectuser"==e.body.type?n("span",[e._v("deze gebruiker")]):n("span",[e._v("deze reactie")]),e._v(" \n        wilt verwijderen?\n\n    ")]),n("div",{staticClass:"modal-actions"},[n("div",{staticClass:"modal-button modal-button-cancel",on:{click:function(t){return e.$emit("closeModal")}}},[e._v("Annuleren")]),n("div",{staticClass:"modal-button modal-button-red",on:{click:e.deleteAction}},[e._v("Verwijder")])])])},W=[],B={name:"Delete",methods:{deleteAction:function(){var e=this;"project"==this.body.type?this.$store.dispatch("deleteProject",this.body.id).then(function(t){e.$emit("closeModal"),e.body.cb(t)}).catch(function(t){t.request&&e.$emit("closeModal")}):"post"==this.body.type?this.$store.dispatch("deletePost",this.body.id).then(function(t){e.$emit("closeModal"),e.body.cb(e.body.id)}).catch(function(t){t.request&&e.$emit("closeModal")}):"projectuser"==this.body.type?this.$store.dispatch("deleteProjectUser",{projectID:this.body.id,userID:this.body.userID}).then(function(t){e.$emit("closeModal"),e.body.cb(e.body.id,e.body.userID)}).catch(function(t){t.request&&e.$emit("closeModal")}):this.$store.dispatch("deleteComment",this.body.id).then(function(t){e.$emit("closeModal"),e.body.cb(e.body.id)}).catch(function(t){t.request&&e.$emit("closeModal")})}},props:["body"]},S=B,J=Object(l["a"])(S,M,W,!1,null,"e8986f40",null),z=J.exports,N=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"modal-content"},[n("div",{staticClass:"modal-header"},[e._v("Plaats een "+e._s("post"==e.body.type?"bericht":"reactie"))]),n("div",{staticClass:"modal-text"},[e._v("\n        "+e._s(e.body.message)+"\n        "),"post"==e.body.type?n("label",[e._v("Titel")]):e._e(),"post"==e.body.type?n("input",{directives:[{name:"model",rawName:"v-model",value:e.title,expression:"title"}],attrs:{type:"text",placeholder:"Titel"},domProps:{value:e.title},on:{input:function(t){t.target.composing||(e.title=t.target.value)}}}):e._e(),n("label",[e._v("Omschrijving")]),n("textarea",{directives:[{name:"model",rawName:"v-model",value:e.description,expression:"description"}],attrs:{placeholder:"Omschrijving"},domProps:{value:e.description},on:{input:function(t){t.target.composing||(e.description=t.target.value)}}})]),n("div",{staticClass:"modal-actions"},[n("div",{staticClass:"modal-button modal-button-cancel",on:{click:function(t){return e.$emit("closeModal")}}},[e._v("Annuleren")]),n("div",{staticClass:"modal-button",on:{click:e.createAction}},[e._v("Aanmaken")])])])},O=[],U={name:"Create",data:function(){return{title:"",description:""}},methods:{createAction:function(){var e=this;"post"==this.body.type?this.$store.dispatch("createPost",{projectID:this.body.id,title:this.title,content:this.description}).then(function(t){e.$router.push("/project/".concat(e.body.id,"/post/").concat(t.data.postID)),e.$emit("closeModal")}).catch(function(t){t.request&&e.$emit("closeModal")}):this.$store.dispatch("createComment",{postID:this.body.id,parent:this.body.parent||null,content:this.description}).then(function(t){e.$emit("closeModal"),e.body.cb(t)}).catch(function(t){t.request&&e.$emit("closeModal")})}},props:["body"]},q=U,Q=Object(l["a"])(q,N,O,!1,null,"3a3af7fc",null),R=Q.exports,V=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"modal-content"},[n("div",{staticClass:"modal-header"},[e._v("Bewerken")]),n("div",{staticClass:"modal-text"},[e._v("\n        Geef een nieuwe omschrijving voor \n        "),"post"==e.body.type?n("span",[e._v("dit bericht")]):n("span",[e._v("deze reactie")]),"post"==e.body.type?n("span",{staticClass:"additional-info"},[e._v("Titel kan niet worden aangepast")]):e._e(),n("textarea",{directives:[{name:"model",rawName:"v-model",value:e.body.text,expression:"body.text"}],domProps:{value:e.body.text},on:{input:function(t){t.target.composing||e.$set(e.body,"text",t.target.value)}}})]),n("div",{staticClass:"modal-actions"},[n("div",{staticClass:"modal-button modal-button-cancel",on:{click:function(t){return e.$emit("closeModal")}}},[e._v("Annuleren")]),n("div",{staticClass:"modal-button",on:{click:e.updateAction}},[e._v("Bevestig")])])])},L=[],F={name:"Edit",methods:{updateAction:function(){var e=this;"post"==this.body.type?this.$store.dispatch("updatePost",{id:this.body.id,text:this.body.text}).then(function(t){e.$emit("closeModal"),e.body.cb(t)}).catch(function(t){t.request&&e.$emit("closeModal")}):this.$store.dispatch("updateComment",{id:this.body.id,text:this.body.text}).then(function(t){e.$emit("closeModal"),e.body.cb(t)}).catch(function(t){t.request&&e.$emit("closeModal")})}},props:["body"]},H=F,G=(n("b172"),Object(l["a"])(H,V,L,!1,null,"06250d26",null)),K=G.exports,Z={name:"Modal",components:{Login:A,Delete:z,Create:R,Edit:K},props:["modaltype","modaldata"]},X=Z,Y=(n("6683"),Object(l["a"])(X,x,T,!1,null,null,null)),ee=Y.exports,te={name:"App",components:{Header:p,Footer:b,Sidebar:C,Modal:ee},data:function(){return{sidebarExtended:!1,modalType:null,modalData:{},modalActive:!1}},methods:{onExtentionChange:function(e){this.sidebarExtended=e},onModalClose:function(){this.modalActive=!1},openModal:function(e,t){this.modalType=e,this.modalData=t,this.modalActive=!0},askPermission:function(){var e=this;if(this.notificationsSupported){if("granted"===Notification.permission)return;Notification.requestPermission(function(t){"granted"!==t||e.showNotification()})}},showNotification:function(){navigator.serviceWorker.ready.then(function(e){return e.showNotification("Notificaties Ingeschakeld",{body:"Vanaf nu ontvang je updates van Project Planner",icon:"/img/icons/android-chrome-192x192.png",image:"/img/autumn-forest.png",vibrate:[300,200,300],badge:"/img/icons/plint-badge-96x96.png"})})}},created:function(){"Notification"in window&&"serviceWorker"in navigator&&(this.notificationsSupported=!0)},mounted:function(){var e=this;setTimeout(function(){return e.sidebarExtended=!1},1e3),this.askPermission()}},ne=te,oe=(n("034f"),Object(l["a"])(ne,a,r,!1,null,null,null)),ae=oe.exports,re=n("8c4f"),ie=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"home"},[e.loggedIn?n("Newsfeed"):n("Welcome")],1)},se=[],ce=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"welcome"},[n("div",{staticClass:"wide-banner"},[n("div",{staticClass:"banner-content"},[n("div",{staticClass:"banner-text"},[e._m(0),n("span",{staticClass:"banner-subtitle"},[e._v("De samenwerkingstool om de communicatie binnen je project naar het volgende level te tillen")]),n("div",{staticClass:"banner-actions"},[n("router-link",{staticClass:"banner-button",attrs:{to:"/explore"}},[e._v("Ontdek Projecten")]),n("router-link",{staticClass:"banner-button",attrs:{to:"/register"}},[e._v("Direct Aanmelden")]),e.notificationsSupported?n("button",{staticClass:"banner-button",on:{click:e.askPermission}},[e._v("Enable notifications >")]):e._e()],1)])])]),e._m(1)])},ue=[function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("span",{staticClass:"banner-title"},[e._v("Welkom bij "),n("span",{staticClass:"logo-text"},[e._v("Project "),n("span",{staticClass:"cursive-green"},[e._v("Planner")])])])},function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"site-info"},[n("div",{staticClass:"site-info-title"},[e._v("Voordelen")]),n("div",{staticClass:"info-grid"},[n("div",{staticClass:"info-column"},[n("div",{staticClass:"info-column-title"},[e._v("Deel Ideeën")]),n("div",{staticClass:"info-column-content"},[e._v("Vindt de projecten die bij jou passen, en deel jouw beste ideeën met anderen. Project planner is het ideale platform om anderen op de hoogte te stellen van jouw beste werk.")])]),n("div",{staticClass:"info-column"},[n("div",{staticClass:"info-column-title"},[e._v("Start conversaties")]),n("div",{staticClass:"info-column-content"},[e._v("Bereik nieuwe leden, start nieuwe gesprekken en bereik nieuwe hoogtes in jouw project. Het regelen van projecten is nog nooit zo makkelijk geweest.")])]),n("div",{staticClass:"info-column"},[n("div",{staticClass:"info-column-title"},[e._v("Beheer leden")]),n("div",{staticClass:"info-column-content"},[e._v("Kies met wie jij je volgende grote klus gaat klaren, en stel het beste team samen voor jouw project. Project planner biedt de mogelijkheid om jouw projecten te beheren op de manier die jij wilt.")])])])])}],le={name:"Welcome",data:function(){return{notificationsSupported:!1}}},de=le,pe=(n("fd1a"),Object(l["a"])(de,ce,ue,!1,null,"72b00ab0",null)),fe=pe.exports,me=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"newsfeed"})},he=[],ve={name:"Newsfeed"},ge=ve,be=Object(l["a"])(ge,me,he,!1,null,"0d098d82",null),_e=be.exports,ke={name:"Home",components:{Welcome:fe,Newsfeed:_e},data:function(){return{loggedIn:!1}}},ye=ke,je=Object(l["a"])(ye,ie,se,!1,null,"63fcb8ab",null),we=je.exports;o["a"].use(re["a"]);var Ce=new re["a"]({routes:[{path:"/",name:"home",component:we},{path:"/register",name:"register",meta:{title:"Register Page",requiresVisitor:!0},component:function(){return n.e("about").then(n.bind(null,"73cf"))}},{path:"/about",name:"about",component:function(){return n.e("about").then(n.bind(null,"f820"))}},{path:"/project/:id",name:"project",meta:{title:"Project",requiresAuthenticated:!0},component:function(){return n.e("about").then(n.bind(null,"07bd"))}},{path:"/project/:projectid/post/:id",name:"post",meta:{title:"Bericht",requiresAuthenticated:!0},component:function(){return n.e("about").then(n.bind(null,"37d3"))}},{path:"/explore",name:"explore",component:function(){return n.e("about").then(n.bind(null,"7797"))}},{path:"/search",name:"search",component:function(){return n.e("about").then(n.bind(null,"2d3b"))}},{path:"/project/:id/settings",name:"projectsettings",meta:{title:"Project instellingen",requiresAuthenticated:!0},component:function(){return n.e("about").then(n.bind(null,"7b05"))}},{path:"/new",name:"newproject",meta:{title:"Project aanmaken",requiresAuthenticated:!0},component:function(){return n.e("about").then(n.bind(null,"0a37"))}},{path:"/profile",name:"usersettings",meta:{title:"Profiel instellingen",requiresAuthenticated:!0},component:function(){return n.e("about").then(n.bind(null,"3a73"))}}]}),xe=(n("7f7f"),n("6b54"),n("2f62")),Te=n("bc3a"),Pe=n.n(Te);Pe.a.defaults.baseURL="http://localhost:5000/",o["a"].use(xe["a"]);var Ie=new xe["a"].Store({state:{JWT_Token:localStorage.getItem("JWT_Token")||null,userID:localStorage.getItem("userID")||null,userProjects:{}},getters:{token:function(e){return e.JWT_Token},userID:function(e){return e.userID},authenticated:function(e){return null!==e.JWT_Token},userProjects:function(e){return e.userProjects}},mutations:{setToken:function(e,t){e.JWT_Token=t},unsetToken:function(e){e.JWT_Token=null},setUserID:function(e,t){e.userID=t},unsetUserID:function(e){e.userID=null},setUserProjects:function(e,t){e.userProjects=t}},actions:{getProjects:function(e,t){var n=t.limit.toString(),o=t.offset.toString(),a="?offset="+o+"&limit="+n;return t.name&&(a+="&name=".concat(t.name)),new Promise(function(e,t){return Pe.a.get("/project"+a).then(function(t){return e(t.data)}).catch(function(e){return t(e)})})},getProjectByID:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(e,n){return Pe.a.get("/project/".concat(t)).then(function(t){return e(t.data)}).catch(function(e){return n(e)})})},getProjectPosts:function(e,t){Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token;var n=t.projectID,o=t.limit.toString(),a=t.offset.toString(),r="?offset="+a+"&limit="+o;return new Promise(function(e,t){return Pe.a.get("/project/".concat(n,"/posts")+r).then(function(t){return e(t.data)}).catch(function(e){return t(e)})})},getPostByID:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(e,n){return Pe.a.get("/post/".concat(t)).then(function(t){return e(t.data)}).catch(function(e){return n(e)})})},getPostComments:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(e,n){return Pe.a.get("/post/".concat(t,"/comments")).then(function(t){return e(t.data)}).catch(function(e){return n(e)})})},getProjectUsers:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(e,n){return Pe.a.get("/project/".concat(t,"/users")).then(function(t){return e(t.data)}).catch(function(e){return n(e)})})},getUser:function(e){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(t,n){return Pe.a.get("/user/".concat(e.state.userID)).then(function(e){return t(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),n(t)})})},getUserByName:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.get("/user?name=".concat(t)).then(function(e){return n(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),o(t)})})},getUserProjects:function(e){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(t,n){return Pe.a.get("/user/".concat(e.state.userID,"/projects")).then(function(n){t(n.data),e.commit("setUserProjects",n.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),n(t)})})},getUserPosts:function(e){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(t,n){return Pe.a.get("/user/".concat(e.state.userID,"/posts")).then(function(e){return t(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),n(t)})})},getUserComments:function(e){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(t,n){return Pe.a.get("/user/".concat(e.state.userID,"/comments")).then(function(e){return t(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),n(t)})})},createProject:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.post("/project",{name:t.name,description:t.description,visibility:t.visibility,ownerID:e.state.userID}).then(function(e){return n(e)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),o(t)})})},createPost:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.post("/project/".concat(t.projectID,"/posts"),{userID:e.state.userID,title:t.title,content:t.content}).then(function(e){return n(e)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),o(t)})})},createComment:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.post("/post/".concat(t.postID,"/comments"),{content:t.content,parent:t.parent,userID:e.state.userID}).then(function(e){return n(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),o(t)})})},createProjectUser:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.post("/project/".concat(t.projectID,"/users"),{user:t.userID?t.userID:e.state.userID,role:t.role}).then(function(e){return n(e)}).catch(function(t){e.dispatch("checkTokenExpiration",t),o(t)})})},updateProject:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.put("/project/".concat(t.projectID),{title:t.name,content:t.description,visibility:t.visibility}).then(function(e){return n(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),o(t)})})},updatePost:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.put("/post/".concat(t.id),{content:t.text}).then(function(e){return n(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),o(t)})})},updateComment:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.put("/comment/".concat(t.id),{content:t.text}).then(function(e){return n(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),o(t)})})},updateProjectUser:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.put("/project/".concat(t.projectID,"/users"),{user:t.userID?t.userID:e.state.userID,role:t.role}).then(function(e){return n(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),o(t)})})},deleteProject:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.delete("/project/".concat(t)).then(function(e){return n(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),o(t)})})},deletePost:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.delete("/post/".concat(t)).then(function(e){return n(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),o(t)})})},deleteComment:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.delete("/comment/".concat(t)).then(function(e){return n(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),o(t)})})},deleteProjectUser:function(e,t){return Pe.a.defaults.headers.common["Authorization"]="Bearer "+e.state.JWT_Token,new Promise(function(n,o){return Pe.a.delete("/project/".concat(t.projectID,"/users"),{data:{user:t.userID?t.userID:e.state.userID}}).then(function(e){return n(e.data)}).catch(function(t){e.dispatch("checkTokenExpiration",t.response),o(t)})})},registerUser:function(e,t){return new Promise(function(e,n){Pe.a.post("http://localhost:5000/user",{name:t.user,password:t.pass}).then(function(t){e(t.data)}).catch(function(e){n(e.response)})})},loginUser:function(e,t){return new Promise(function(n,o){Pe.a.post("http://localhost:5000/login",{name:t.user,password:t.pass}).then(function(t){var o=t.data.jwt_token,a=t.data.id;localStorage.setItem("JWT_Token",o),localStorage.setItem("userID",a),e.commit("setToken",o),e.commit("setUserID",a),n(t.data)}).catch(function(e){o(e.response.data.error)})})},logoutUser:function(e){e.commit("unsetToken"),e.commit("unsetUserID"),localStorage.removeItem("JWT_Token"),localStorage.removeItem("userID")},checkTokenExpiration:function(e,t){}}}),De=n("9483");Object(De["a"])("".concat("/","service-worker.js"),{ready:function(){console.log("App is being served from cache by a service worker.\nFor more details, visit https://goo.gl/AFskqB")},registered:function(){console.log("Service worker has been registered.")},cached:function(){console.log("Content has been cached for offline use.")},updatefound:function(){console.log("New content is downloading.")},updated:function(){console.log("New content is available; please refresh.")},offline:function(){console.log("No internet connection found. App is running in offline mode.")},error:function(e){console.error("Error during service worker registration:",e)}}),o["a"].config.productionTip=!1,Ce.beforeEach(function(e,t,n){e.matched.some(function(e){return e.meta.requiresVisitor})?Ie.getters.authenticated?n({path:"/"}):n():e.matched.some(function(e){return e.meta.requiresAuthenticated})?Ie.getters.authenticated?n():n({path:"/"}):n()}),new o["a"]({store:Ie,router:Ce,render:function(e){return e(ae)}}).$mount("#app")},"5ad7":function(e,t,n){},"5ffb":function(e,t,n){},6468:function(e,t,n){},"64a9":function(e,t,n){},6683:function(e,t,n){"use strict";var o=n("5ffb"),a=n.n(o);a.a},"6e26":function(e,t,n){},"7f35":function(e,t,n){},b172:function(e,t,n){"use strict";var o=n("5ad7"),a=n.n(o);a.a},d98d:function(e,t,n){"use strict";var o=n("6e26"),a=n.n(o);a.a},e86e:function(e,t,n){},eaeb:function(e,t,n){},fa3e:function(e,t,n){"use strict";var o=n("eaeb"),a=n.n(o);a.a},fd1a:function(e,t,n){"use strict";var o=n("6468"),a=n.n(o);a.a}});
//# sourceMappingURL=app.8bd1c69a.js.map