import request from '@/utils/request'

export function getList(params) {
  return request({
    url: '/docs/',
    method: 'get',
    params
  })
}

export function get(id) {
  return request({
    url: '/docs/' + id + '/',
    method: 'get'
  })
}

export function create(data) {
  return request({
    url: '/docs/',
    method: 'post',
    data
  })
}

export function update(data) {
  return request({
    url: '/docs/' + data.id + '/',
    method: 'put',
    data
  })
}

export function del(id) {
  return request({
    url: '/docs/' + id + '/',
    method: 'delete'
  })
}

export function publish(id) {
  return request({
    url: '/docs/publish/' + id + '/',
    method: 'put'
  })
}

export function downloadMd(id) {
  return  process.env.BASE_API + '/docs/download/md/' + id + '/'
}

export function downloadHtml(id) {
  return  process.env.BASE_API + '/docs/download/html/' + id + '/'
}

export function downloadPdf(id) {
  return  process.env.BASE_API + '/docs/download/pdf/' + id + '/'
}

export function downloadDocx(id) {
  return  process.env.BASE_API + '/docs/download/docx/' + id + '/'
}
