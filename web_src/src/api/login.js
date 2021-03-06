import request from '@/utils/request'

export function login(username, password) {
  return request({
    url: '/api-token-auth/',
    method: 'post',
    data: {
      username,
      password
    }
  })
}

export function getInfo(token) {
  return request({
    url: '/user/info/',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/api-auth/logout/',
    method: 'get'
  })
}
