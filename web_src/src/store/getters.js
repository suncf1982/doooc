const getters = {
  sidebar: state => state.app.sidebar,
  token: state => state.user.token,
  avatar: state => state.user.avatar,
  name: state => state.user.name,
  groups: state => state.user.groups,
  permission_routers: state => state.permission.routers,
  addRouters: state => state.permission.addRouters,
  isAdmin: state => state.permission.isAdmin,
  enums: state=> state.app.enums
}
export default getters
