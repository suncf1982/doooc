import request from '@/utils/request'

export function getDependences(params) {
  return request({
    url: '/dependences/',
    method: 'get',
    params
  })
}
