import fetch from '@/utils/fetch'

export function getDependences(params) {
  return fetch({
    url: '/dependences/',
    method: 'get',
    params
  })
}