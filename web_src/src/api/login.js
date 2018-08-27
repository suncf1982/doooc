import fetch from '@/utils/fetch'

export function login(username, password) {
  return fetch({
    url: '/api-token-auth/',
    method: 'post',
    data: {
      username,
      password
    }
  })
}

export function getInfo(token) {
  return fetch({
    url: '/user/info/',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return fetch({
    url: '/api-auth/logout/',
    method: 'get'
  })
}
