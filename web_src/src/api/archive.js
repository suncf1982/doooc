import request from '@/utils/request'

export function getList(params) {
  return request({
    url: '/archives/',
    method: 'get',
    params
  })
}

export function get(id) {
  return request({
    url: '/archives/' + id + '/',
    method: 'get'
  })
}

export function create(data) {
  return request({
    url: '/archives/',
    method: 'post',
    data
  })
}

export function update(data) {
  return request({
    url: '/archives/' + data.id + '/',
    method: 'put',
    data
  })
}

export function del(id) {
  return request({
    url: '/archives/' + id + '/',
    method: 'delete'
  })
}

export function removeDoc(archiveId, docId) {
  return request({
    url: '/archives/' + archiveId + '/' + docId + '/',
    method: 'delete'
  })
}

export function addDoc(archiveId, docId) {
  return request({
    url: '/archives/' + archiveId + '/' + docId + '/',
    method: 'post'
  })
}

