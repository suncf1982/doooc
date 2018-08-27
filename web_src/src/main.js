import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import ECharts from 'vue-echarts/components/ECharts.vue'
import locale from 'element-ui/lib/locale/lang/zh-CN'
import App from './App'
import router from './router'
import store from './store'
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'// Progress 进度条样式
import '@/icons' // icon
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

import { getToken, removeToken } from '@/utils/auth' //鉴权

Vue.use(ElementUI, { locale })
Vue.use(mavonEditor)
Vue.component('chart', ECharts)
Vue.config.productionTip = false

const whiteList = ['/login']

router.beforeEach((to, from, next) => {
  NProgress.start()
  if (getToken()) {
    if (to.path === '/login') {
      next({ path: '/' })
    } else {
      if (store.getters.groups.length === 0) {
        store.dispatch('GetInfo').then(res => {

          if (res.groups.length === 0) {
            next('/login')
          }
          store.dispatch('LoadDependences').then(() => {
            const groups = res.groups || ['ADMIN']
            store.dispatch('GenerateRoutes', { groups }).then(() => {
              router.addRoutes(store.getters.addRouters)
              next({ ...to })
            })
          })
        },
          error => {
            removeToken()
            next('/login')
          })
      } else {
        next()
      }
    }
  } else {
    if (whiteList.indexOf(to.path) !== -1) {
      next()
    } else {
      next('/login')
      NProgress.done()
    }
  }
})

router.afterEach(() => {
  NProgress.done() // 结束Progress
})

new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
