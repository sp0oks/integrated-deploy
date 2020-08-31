import Vue from "vue";
import App from "./App.vue";
import router from "./router";

import { BootstrapVue, CardPlugin, BCard, BCardGroup } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
Vue.use(BootstrapVue);
Vue.use(CardPlugin);
Vue.component("b-card", BCard);
Vue.component("b-card-group", BCardGroup);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
