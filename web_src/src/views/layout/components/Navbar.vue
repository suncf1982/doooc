<template>
  <el-menu class="navbar" mode="horizontal">
    <hamburger :toggle-click="toggleSideBar" :is-active="sidebar.opened" class="hamburger-container"/>
    <breadcrumb />
    <el-dropdown class="avatar-container" trigger="hover" placement="top">
      <div class="avatar-wrapper">
        {{ name }}<i class="el-icon-caret-bottom"/>
      </div>
      <el-dropdown-menu slot="dropdown" class="user-dropdown">
        <div class="user-panel">
          <div class="user-panel-header">
            <img src="@/assets/images/avatar5.png" class="user-avatar">
            <div class="user-info">{{ name }}</div>
          </div>
          <div class="user-panel-footer">
            <el-button size="medium">个人信息</el-button>
            <el-button size="medium" style="float: right;" @click="logout">退出系统</el-button>
          </div>
        </div>
      </el-dropdown-menu>
    </el-dropdown>
  </el-menu>
</template>

<script>
import { mapGetters } from 'vuex'
import Breadcrumb from '@/components/Breadcrumb'
import Hamburger from '@/components/Hamburger'

export default {
  components: {
    Breadcrumb,
    Hamburger
  },
  computed: {
    ...mapGetters([
      'sidebar',
      'avatar',
      'name'
    ])
  },
  methods: {
    toggleSideBar() {
      this.$store.dispatch('ToggleSideBar')
    },
    logout() {
      this.$store.dispatch('LogOut').then(() => {
        location.reload() // 为了重新实例化vue-router对象 避免bug
      })
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.navbar {
  height: 50px;
  line-height: 50px;
  border-radius: 0px !important;
  .hamburger-container {
    line-height: 58px;
    height: 50px;
    float: left;
    padding: 0 10px;
  }
  .screenfull {
    position: absolute;
    right: 90px;
    top: 16px;
    color: red;
  }
  .avatar-container {
    height: 50px;
    display: inline-block;
    position: absolute;
    right: 35px;
    .avatar-wrapper {
      cursor: pointer;
      margin-top: 5px;
      position: relative;
      .user-avatar {
        width: 40px;
        height: 40px;
        border-radius: 10px;
      }
      .el-icon-caret-bottom {
        position: absolute;
        right: -20px;
        top: 18px;
        font-size: 12px;
      }
    }
  }
}

.user-panel {
  width: 280px;
  &-header {
    height: 160px;
    background: #3c8dbc;
    padding: 10px;
    text-align: center;
    .user-avatar {
      z-index: 5;
      height: 90px;
      width: 90px;
      border: 3px solid;
      border-radius: 50%;
      border-color: white;
    }
    .user-info {
      color: white;
      padding: 10px;
    }
  }
  &-footer {
    padding: 10px;
  }
}
</style>

