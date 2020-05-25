// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
import 'element-ui/lib/theme-chalk/index.css'
import echarts from 'echarts'
import axios from 'axios'
import Qs from 'qs'
import dataV from '@jiaminghi/data-view'
import VueParticles from 'vue-particles'

Vue.use(VueParticles)
Vue.use(dataV)
Vue.use(ElementUI)

Vue.config.productionTip = false
Vue.use(VueResource)

Vue.prototype.$echarts = echarts
Vue.prototype.axios = axios
Vue.prototype.qs = Qs

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
