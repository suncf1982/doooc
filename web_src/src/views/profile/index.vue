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
            <el-tab-pane label="修改密码" name="setting">
              <el-form ref="ruleChgPassForm" :model="ruleChgPassForm" :rules="rulesChgPass" status-icon label-width="100px" class="demo-ruleForm">
                <el-form-item label="原密码" prop="originalPass">
                  <el-input v-model="ruleChgPassForm.originalPass" type="password" auto-complete="off" />
                </el-form-item>
                <el-form-item label="密码" prop="pass">
                  <el-input v-model="ruleChgPassForm.pass" type="password" auto-complete="off" />
                </el-form-item>
                <el-form-item label="确认密码" prop="checkPass">
                  <el-input v-model="ruleChgPassForm.checkPass" type="password" auto-complete="off" />
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="onSubmitChgPassForm('ruleChgPassForm')">保存</el-button>
                </el-form-item>
              </el-form>
            </el-tab-pane>
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
    const validateOriginalPass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入原密码'))
      } else {
        callback()
      }
    }
    const validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.ruleChgPassForm.checkPass !== '') {
          this.$refs.ruleChgPassForm.validateField('checkPass')
        }
        callback()
      }
    }
    const validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.ruleChgPassForm.pass) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      user: {},
      activeName: 'mydocs',
      myDocsLoading: false,
      mydocs: [],
      ruleChgPassForm: {
        originalPass: '',
        pass: '',
        checkPass: ''
      },
      rulesChgPass: {
        originalPass: [
          { validator: validateOriginalPass, trigger: 'blur' }
        ],
        pass: [
          { validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur' }
        ]
      }
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
    },
    onSubmitChgPassForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
        } else {
          return false
        }
      })
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
