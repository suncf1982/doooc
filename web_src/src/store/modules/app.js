import Cookies from 'js-cookie'
import { getDependences } from '@/api/common'

const app = {
  state: {
    sidebar: {
      opened: !+Cookies.get('sidebarStatus'),
      withoutAnimation: false
    },
    device: 'desktop',
    dependencesLoaded: false,
    enums: {}
  },
  mutations: {
    TOGGLE_SIDEBAR: state => {
      if (state.sidebar.opened) {
        Cookies.set('sidebarStatus', 1)
      } else {
        Cookies.set('sidebarStatus', 0)
      }
      state.sidebar.opened = !state.sidebar.opened
      state.sidebar.withoutAnimation = false
    },
    CLOSE_SIDEBAR: (state, withoutAnimation) => {
      Cookies.set('sidebarStatus', 1)
      state.sidebar.opened = false
      state.sidebar.withoutAnimation = withoutAnimation
    },
    TOGGLE_DEVICE: (state, device) => {
      state.device = device
    },
    DEPENDEDENCES_LOADED: (state, data) => {
      state.dependencesLoaded = true;
      state.enums = { ...data.enums };
    }
  },
  actions: {
    ToggleSideBar: ({ commit }) => {
      commit('TOGGLE_SIDEBAR')
    },
    CloseSideBar({ commit }, { withoutAnimation }) {
      commit('CLOSE_SIDEBAR', withoutAnimation)
    },
    ToggleDevice({ commit }, device) {
      commit('TOGGLE_DEVICE', device)
    },
    LoadDependences: ({ commit, state }) => {
      return new Promise((resolve, reject) => {
        getDependences(state.token).then(response => {
          commit('DEPENDEDENCES_LOADED', response)
          resolve(response)
        }).catch(error => {
          reject(error)
        })
      })
    }
  }
}

export default app
