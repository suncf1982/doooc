<template>
  <section>
    <div class="app-container page-profile">
      <el-container>
        <el-aside>
          <div class="profile-user">
            <img src="@/assets/images/avatar5.png" class="profile-user-avatar">
            <div class="profile-user-info">{{ user.first_name }}</div>
            <ul class="list-group">
              <li class="list-group-item">
                <em>邮箱</em>
                <span>{{ user.email }}</span>
              </li>
              <li class="list-group-item">
                <em>加入日期</em>
                <span>{{ user.date_joined }}</span>
              </li>
            </ul>
          </div>
        </el-aside>
        <el-main>
          <el-tabs v-model="activeName" @tab-click="onTabClick">
            <el-tab-pane label="我的文档" name="mydocs">
              <el-table v-loading.body="myDocsLoading" :data="mydocs" :show-header="false" element-loading-text="拼命加载中" fit>
                <el-table-column label="标题" header-align="center">
                  <template slot-scope="scope">
                    <router-link :to="{ name: 'Doc-View', params: { id: scope.row.id } }" target="_blank" class="title" style="text-decoration: underline;">{{ scope.row.title }}</router-link>
                  </template>
                </el-table-column>
                <el-table-column label="更新于" header-align="center" align="center" width="100">
                  <template slot-scope="scope">
                    {{ scope.row.update_at | formatDate }}
                  </template>
                </el-table-column>
              </el-table>
            </el-tab-pane>
            <el-tab-pane label="我的收藏" name="myfavorites">我的收藏</el-tab-pane>
            <el-tab-pane label="设置" name="setting">基础信息设置</el-tab-pane>
          </el-tabs>
        </el-main>
      </el-container>
    </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex'
import moment from 'moment'
import { getInfo } from '@/api/login'
import { getList as getDocList } from '@/api/doc'

moment.locale('zh-cn')

export default {
  filters: {
    formatDate(dateStr) {
      return moment(dateStr).fromNow()
    }
  },
  data() {
    return {
      user: {},
      activeName: 'mydocs',
      myDocsLoading: false,
      mydocs: []
    }
  },
  computed: {
    ...mapGetters([
      'enums',
      'avatar',
      'name',
      'token'
    ])
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.getUserInfo()
      this.getMyDocs()
    },
    getUserInfo() {
      getInfo(this.token).then(response => {
        this.user = { ...response }
      })
    },
    getMyDocs() {
      getDocList({ limit: 10 }).then(response => {
        this.mydocs = response.results
      })
    },
    onTabClick(tab, event) {
      if (tab.name === 'mydocs') {
        this.getMyDocs()
      }
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss">
  .el-aside {
    color: #333;
    text-align: center;
  }
  .el-main {
    margin-left: 20px;
    padding: 0 20px;
  }
  .profile-user {
    padding: 0;
    text-align: center;
    &-avatar {
      z-index: 5;
      height: 120px;
      width: 120px;
      border: 3px solid;
      border-radius: 50%;
      border-color: white;
      margin-top: 10px;
    }
    &-info {
      padding: 10px;
    }
    .list-group {
      padding-left: 0;
      margin-bottom: 20px;
      &-item {
        position: relative;
        display: block;
        padding: 10px;
        border-top: 1px solid #D3DCE6;
        &:last-child {
          border-bottom: 1px solid #D3DCE6;
        }
        span {
          float: right;
        }
      }
    }
  }
</style>
