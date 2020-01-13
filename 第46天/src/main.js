import Vue from 'vue'
// import axios from 'axios'
import { Button, Select } from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
import './plugins/element.js'
// import HelloWorld from './components/HelloWorld.vue'

Vue.config.productionTip = false
Vue.config.silent = false

Vue.component(Button.name, Button);
Vue.component(Select.name, Select);
// Todo
new Vue({
  el: '#app',
  render: h => h(App)
})

// Test

// new Vue({
//   el: '#app',
//   data(){
//     return {info: null}
//   },
//   mounted(){
//     // GET 请求
//     axios
//       .get('https://api.coindesk.com/v1/bpi/currentprice.json')
//       .then(response => {
//         console.log(response.data)
//         this.info = response.data
//       })
//       .catch(function (error) { // 请求失败处理
//         console.log(error);
//       });


//       axios.post('/user', {
//         firstName: 'Fred',        // 参数 firstName
//         lastName: 'Flintstone'    // 参数 lastName
//       })
//       .then(function (response) {
//         console.log(response);
//       })
//       .catch(function (error) {
//         console.log(error);
//       });
//   },
//   render: h => h(HelloWorld)
// })


 