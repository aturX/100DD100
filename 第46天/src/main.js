import Vue from 'vue'
import { Button, Select } from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import './plugins/element.js'

Vue.config.productionTip = false


Vue.component(Button.name, Button);
Vue.component(Select.name, Select);

new Vue({
  el: '#app',
  render: h => h(App)
})