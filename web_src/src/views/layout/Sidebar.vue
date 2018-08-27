<template>

  <el-menu
    :default-active="activeIndex"
    class="el-menu-vertical-demo"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b">

    <template v-for="item in permission_routers">
      <router-link v-if="!item.hidden&&( (item.noDropdown&&item.children.length>0) || item.children.length == 0)" :to="{name: item.name}">
        <el-menu-item :index="item.name">
          <i class="el-icon-star-on"></i>
          <span slot="title">{{item.meta.label}}</span>
        </el-menu-item>
      </router-link>
      <el-submenu :index="item.name" v-if="!item.hidden&&!item.noDropdown&&item.children.length>0">
        <template slot="title">
          <i class="el-icon-star-on"></i>
          <span>{{item.meta.label}}</span>
        </template>
        <template v-for="child in item.children" >
          <router-link v-if="!child.hidden" :to="{name: child.name}">
            <el-menu-item :index="child.name">
              <i class="el-icon-setting"></i>
              <span slot="title">{{child.meta.label}}</span>
            </el-menu-item>
          </router-link>
        </template>
      </el-submenu>
    </template>
  </el-menu>
</template>

<script>
import { mapGetters } from 'vuex'
import SidebarItem from './SidebarItem'
export default {
  components: { SidebarItem },
  computed: { 
    ...mapGetters([
      'permission_routers'
    ]),
    activeIndex () {
      return this.$router.currentRoute.name;
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.el-menu {
  min-height: 100%;
}
</style>
