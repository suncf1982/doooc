import fetch from '@/utils/fetch'

export function getList(params) {
  return fetch({
    url: '/docs/',
    method: 'get',
    params
  })
}

export function get(id) {
  return fetch({
    url: '/docs/' + id + '/',
    method: 'get'
  })
}

export function create(data) {
  return fetch({
    url: '/docs/',
    method: 'post',
    data
  })
}

export function update(data) {
  return fetch({
    url: '/docs/' + data.id + '/',
    method: 'put',
    data
  })
}

export function del(id) {
  return fetch({
    url: '/docs/' + id + '/',
    method: 'delete'
  })
}

export function publish(id) {
  return fetch({
    url: '/docs/publish/' + id + '/',
    method: 'put'
  })
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
