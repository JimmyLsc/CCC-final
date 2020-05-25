import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Try from '@/components/Try'
import piechart from '@/components/piechart'
import statical from '@/components/statical'
import analysis from '@/view/analysis'
import homePage from '@/view/homePage'
import map from '@/components/map'
import emotion from '@/components/emotion'
import singlePerformance from '@/part/singlePerformance'
import performancePage from '@/view/performancePage'
import piechart2 from '@/components/piechart2'
import combine from '@/view/combine'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'homePage',
      component: homePage
    },

    {
      path: '/Home',
      name: 'Home',
      component: Home
    },
    {
      path: '/map',
      name: 'map',
      component: map
    },
    {
      path: '/piechart2',
      name: 'piechart2',
      component: piechart2

    },

    {
      path: '/Try',
      name: 'Try',
      component: Try
    },
    {
      path: '/pie',
      name: 'piechart',
      component: piechart
    },
    {
      path: '/statical',
      name: 'statical',
      component: statical
    },
    {
      path: '/emotion',
      name: 'emotion',
      component: emotion

    },
    {
      path: '/usage',
      name: 'singlePerformance',
      component: singlePerformance
    },
    {
      path: '/analysis',
      name: 'analysis',
      component: analysis
    },
    {
      path: '/performance',
      name: 'performancePage',
      component: performancePage
    },
    {
      path: '/combine',
      name: 'combine',
      component: combine
    }
  ]
})
