import { asyncRouterMap, constantRouterMap } from '@/router/index'

/**
 * 通过meta.role判断是否与当前用户权限匹配
 * @param roles
 * @param route
 */
function hasPermission(groups, route) {
  if (route.meta && route.meta.group) {
    return groups.some(group => route.meta.group.indexOf(group.value) >= 0)
  } else {
    return true
  }
}

/**
 * 递归过滤异步路由表，返回符合用户角色权限的路由表
 * @param asyncRouterMap
 * @param groups
 */
function filterAsyncRouter(asyncRouterMap, groups) {
  const accessedRouters = asyncRouterMap.filter(route => {
    if (hasPermission(groups, route)) {
      if (route.children && route.children.length) {
        route.children = filterAsyncRouter(route.children, groups)
      }
      return true
    }
    return false
  })
  return accessedRouters
}

const permission = {
  state: {
    routers: constantRouterMap,
    addRouters: [],
    isAdmin: false
  },
  mutations: {
    SET_ROUTERS: (state, routers) => {
      state.addRouters = routers
      state.routers = constantRouterMap.concat(routers)
    },
    SET_ADMIN: (state, isAdmin) => {
      state.isAdmin = isAdmin
    }
  },
  actions: {
    GenerateRoutes({ commit }, data) {
      return new Promise(resolve => {
        const { groups } = data
        let accessedRouters
        let isAdmin = groups.find((value, index, arr)=>{return value.value==='ADMIN'})
        commit('SET_ADMIN', isAdmin)
        
        if (isAdmin) {
          accessedRouters = asyncRouterMap
        } else {
          accessedRouters = filterAsyncRouter(asyncRouterMap, groups)
        }
        commit('SET_ROUTERS', accessedRouters)
        resolve()
      })
    }
  }
}

export default permission
