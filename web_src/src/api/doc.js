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

export function search(params) {
  return request({
    url: '/docs/search/',
    method: 'get',
    params
  })
}

export function publish(id) {
  return request({
    url: '/docs/publish/' + id + '/',
    method: 'put'
  })
}

export function share(id, share_to) {
  return request({
    url: '/docs/share/' + id + '/',
    method: 'put',
    data: {
      share_to: share_to
    }
  })
}

export function pupularTags() {
  return request({
    url: '/docs/pupulartags/',
    method: 'get'
  })
}

export function pupularKeywords() {
  return request({
    url: '/docs/pupularkeywords/',
    method: 'get'
  })
}

export function pupularDocs() {
  return request({
    url: '/docs/populardocs/',
    method: 'get'
  })
}

export function downloadMd(id) {
  return process.env.BASE_API + '/docs/download/md/' + id + '/'
}

export function downloadHtml(id) {
  return process.env.BASE_API + '/docs/download/html/' + id + '/'
}

export function downloadPdf(id) {
  return process.env.BASE_API + '/docs/download/pdf/' + id + '/'
}

export function downloadDocx(id) {
  return process.env.BASE_API + '/docs/download/docx/' + id + '/'
}

export function downloadPptx(id) {
  return process.env.BASE_API + '/docs/download/pptx/' + id + '/'
}

export function onlinePpt(id) {
  return process.env.BASE_API + '/docs/onlineppt/' + id + '/'
}

export function uploadFile() {
  return process.env.BASE_API + '/resources/upload/'
}

export function getTemplates(params) {
  return request({
    url: '/docs/templates/',
    method: 'get',
    params
  })
}

export function getTemplateContent(id) {
  return request({
    url: '/docs/templates/' + id + '/',
    method: 'get'
  })
}

export function getFavorites(params) {
  return request({
    url: '/docs/favorites/',
    method: 'get',
    params
  })
}

export function createFavorite(data) {
  return request({
    url: '/docs/favorites/',
    method: 'post',
    data
  })
}

export function delFavorite(id) {
  return request({
    url: '/docs/favorites/' + id + '/',
    method: 'delete'
  })
}
