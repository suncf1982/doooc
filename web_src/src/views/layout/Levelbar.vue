<template>
  <el-breadcrumb class="app-levelbar" separator="/">
    <el-breadcrumb-item v-for="(item,index)  in levelList" :key="item.path">
      <router-link v-if='item.redirect==="noredirect"||index==levelList.length-1' to="" class="no-redirect">{{item.meta.label}}</router-link>
      <router-link v-else :to="item.redirect||{name: item.name}">{{item.meta.label}}</router-link>
    </el-breadcrumb-item>
  </el-breadcrumb>
</template>

<script>

export default {
  created() {
    this.getBreadcrumb()
  },
  data() {
    return {
      levelList: null
    }
  },
  methods: {
    getBreadcrumb() {
      let matched = this.$route.matched.filter(item => item.name)
      let list = []
      matched.forEach((item, idx)=>{
        if(item.meta.parent) {
          //{ name: 'Home', path: '/', meta: {label: 'Home'} }
        } else {
          list.push(item)
        }
      })
      const first = matched[0]
      if (first && (first.name !== 'Home' || first.path !== '')) {
        matched = [{ name: 'Home', path: '/', meta: {label: 'Home'} }].concat(matched)
      }
      this.levelList = matched
    }
  },
  watch: {
    $route() {
      this.getBreadcrumb()
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.app-levelbar.el-breadcrumb {
  display: inline-block;
  font-size: 14px;
  line-height: 50px;
  margin-left: 10px;
  .no-redirect {
    color: #97a8be;
    cursor: text;
  }
}
</style>
