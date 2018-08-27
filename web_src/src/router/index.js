import Vue from 'vue'
import Router from 'vue-router'
const _import = require('./_import_' + process.env.NODE_ENV)
// in development env not use Lazy Loading,because Lazy Loading too many pages will cause webpack hot update too slow.so only in production use Lazy Loading

/* layout */
import Layout from '../views/layout/Layout'

Vue.use(Router)

/**
 * icon : the icon show in the sidebar
 * hidden : if `hidden:true` will not show in the sidebar
 * redirect : if `redirect:noredirect` will not redirct in the levelbar
 * noDropdown : if `noDropdown:true` will not has submenu in the sidebar
 * meta : `{ group: ['ADMIN'] }`  will control the page role
 **/
export const constantRouterMap =
  [
    {
      path: '/login',
      component: _import('login/index'),
      hidden: true
    },
    {
      path: '/404',
      component: _import('404'),
      hidden: true
    },
    {
      path: '/',
      component: Layout,
      redirect: '/dashboard',
      name: 'dashboard',
      icon: 'zujian',
      noDropdown: true,
      meta: {
        label: '主页'
      },
      children:
        [
          {
            path: 'dashboard',
            component: _import('dashboard/index')
          }
        ]
    }
  ]

export default new Router({
  // mode: 'history', //后端支持可开
  scrollBehavior: () => ({
    y: 0
  }),
  routes: constantRouterMap
})

export const asyncRouterMap = [
  {
    path: '/doc',
    component: Layout,
    redirect: '/doc/index',
    name: 'doc',
    icon: 'tubiao',
    meta: {
      label: '文档管理',
      group: ['ADMIN']
    },
    children: [
      {
        path: 'index',
        name: 'doc-index',
        component: _import('doc/index'),
        meta: {
          label: '文档管理',
          group: ['ADMIN']
        }
      },
      {
        path: 'create',
        name: 'doc-create',
        component: _import('doc/create'),
        meta: {
          label: '添加文档',
          group: ['ADMIN']
        }
      },
      {
        path: 'view/:id',
        name: 'doc-view',
        component: _import('doc/view'),
        meta: {
          label: '查看文档',
          group: ['ADMIN']
        },
        hidden: true
      }
    ]
  },
  {
    path: '*',
    redirect: '/404',
    hidden: true
  }
]