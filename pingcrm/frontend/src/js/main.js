import "../css/app.css";
import Vue from "vue";
import VueMeta from "vue-meta";
import PortalVue from "portal-vue";
import { InertiaApp } from "@inertiajs/inertia-vue";

Vue.config.productionTip = false;
Vue.mixin({ methods: { route: window.reverse } });
Vue.use(InertiaApp);
Vue.use(PortalVue);
Vue.use(VueMeta);

let app = document.getElementById("app");
window.console.log(app.dataset.page);

new Vue({
  metaInfo: {
    titleTemplate: title => (title ? `${title} - Ping CRM` : "Ping CRM")
  },
  render: h =>
    h(InertiaApp, {
      props: {
        initialPage: JSON.parse(app.dataset.page),
        resolveComponent: name =>
          import(`@/Pages/${name}`).then(module => module.default)
      }
    })
}).$mount(app);
