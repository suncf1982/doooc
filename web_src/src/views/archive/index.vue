<template>
  <section>
    <div class="app-container page-archive-index">
      <el-container>
        <el-header>
          <el-tooltip class="item" effect="dark" content="添加归档" placement="top">
            <el-button type="primary" size="mini" circle @click="dialogAddArchiveVisible = true"><i class="el-icon-plus" /></el-button>
          </el-tooltip>
        </el-header>
        <el-container>
          <el-aside width="200px">
            <el-tree
              :data="archiveList"
              :props="defaultTreeProps"
              node-key="id"
              @node-click="onTreeNodeClick">
              <span slot-scope="{ node, data }" class="custom-tree-node">
                <span>{{ node.label }}</span>
                <span>
                  <el-button type="text" @click="() => onTreeNodeEdit(node, data)"><i class="el-icon-edit" /></el-button>
                  <el-button type="text" style="color: #F56C6C;" @click="() => onTreeNodeDel(node, data)"><i class="el-icon-remove" /></el-button>
                </span>
              </span>
            </el-tree>
          </el-aside>
          <el-main>
            <el-table v-loading.body="docListLoading" :data="docList" :show-header="false" element-loading-text="拼命加载中" fit>
              <el-table-column label="标题" header-align="center">
                <template slot-scope="scope">
                  <router-link :to="{ name: 'Doc-View', params: { id: scope.row.id } }" target="_blank" class="title" style="text-decoration: underline;">{{ scope.row.title }}</router-link>
                </template>
              </el-table-column>
              <el-table-column label="发布状态" header-align="center" align="center" width="100">
                <template slot-scope="scope">
                  <el-tag :type="scope.row.published | publishedFilter" size="small">{{ scope.row.published | publishedNameFilter }}</el-tag>
                </template>
              </el-table-column>
              <el-table-column label="更新于" header-align="center" align="center" width="100">
                <template slot-scope="scope">
                  {{ scope.row.update_at | formatDate }}
                </template>
              </el-table-column>
              <el-table-column label="操作" header-align="center" align="center" width="160" class-name="op">
                <template slot-scope="scope">
                  <el-tooltip class="item" effect="dark" content="预览" placement="top">
                    <router-link :to="{ name: 'Doc-View', params: { id: scope.row.id } }" target="_blank" style="color: #409EFF;"><i class="el-icon-view" /></router-link>
                  </el-tooltip>
                  <el-tooltip class="item" effect="dark" content="移除" placement="top">
                    <el-button type="text" style="color: #F56C6C;" @click="onRemoveFromArchive(scope.$index, scope.row)"><i class="el-icon-remove" /></el-button>
                  </el-tooltip>
                </template>
              </el-table-column>
            </el-table>
          </el-main>
        </el-container>
      </el-container>
      <el-dialog :visible.sync="dialogAddArchiveVisible" width="30%" title="添加归档">
        <el-form ref="addArchiveForm" :model="addArchiveForm">
          <el-form-item
            :rules="[{ required: true, message: '名称不能为空'}]"
            label="">
            <el-input v-model="addArchiveForm.name" auto-complete="off" placeholder="归档名称" />
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogAddArchiveVisible = false">取 消</el-button>
          <el-button type="primary" @click.native="onAddArchive('addArchiveForm')">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </section>
</template>

<script>
import { getList, create, update, del, removeDoc } from '@/api/archive'
import { getList as search } from '@/api/doc'
import { mapGetters } from 'vuex'
import moment from 'moment'

moment.locale('zh-cn')

export default {
  filters: {
    publishedFilter(published) {
      return published ? 'success' : 'info'
    },
    publishedNameFilter(published) {
      return published ? '已发布' : '未发布'
    },
    formatDate(dateStr) {
      return moment(dateStr).fromNow()
    }
  },
  data() {
    return {
      archiveList: [],
      archiveListLoading: true,
      defaultTreeProps: {
        label: 'name'
      },
      selectedArchive: '',
      docList: [],
      docListLoading: false,
      total: 0,
      page: 1,
      pageSize: 20,
      dialogAddArchiveVisible: false,
      addArchiveForm: {
        name: ''
      }
    }
  },
  computed: {
    ...mapGetters(['enums'])
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.getMyArchives()
    },
    getMyArchives() {
      this.archiveListLoading = true
      getList().then(response => {
        this.archiveList = response.results
        this.total = response.count
        this.archiveListLoading = false
      })
    },
    getDocsOfArchive(archiveId) {
      this.selectedArchive = archiveId
      search(this.getQuery({ archive: archiveId })).then(res => {
        this.docList = res.results
        this.total = res.count
      })
    },
    getQuery(kvpairs) {
      const params = {
        limit: this.pageSize,
        offset: (this.page - 1) * this.pageSize
      }
      Object.assign(params, kvpairs)
      return params
    },
    onAddArchive(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          const param = Object.assign({}, this.addArchiveForm)
          if (param.id === undefined) {
            create(param).then(res => {
              this.$message({
                message: '添加成功',
                type: 'success'
              })
              this.id = res.id
              this.fetchData()
            })
          } else {
            update(param).then(res => {
              this.$message({
                message: '修改成功',
                type: 'success'
              })

              this.fetchData()
            })
          }
          this.dialogAddArchiveVisible = false
          this.addArchiveForm.name = ''
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    onTreeNodeClick(data) {
      this.getDocsOfArchive(data.id)
    },
    onTreeNodeEdit(node, data) {
      this.addArchiveForm.id = data.id
      this.addArchiveForm.name = data.name
      this.dialogAddArchiveVisible = true
    },
    onTreeNodeDel(node, data) {
      this.$confirm('确认删除吗？', '提示', {}).then(() => {
        del(data.id).then(res => {
          this.$message({
            message: '删除成功',
            type: 'success'
          })
          this.getMyArchives()
        })
      })
    },
    onRemoveFromArchive(index, row) {
      removeDoc(this.selectedArchive, row.id).then(res => {
        this.$message({
          message: '移除成功',
          type: 'success'
        })
        this.getDocsOfArchive(this.selectedArchive)
      })
    },
    handleCurrentChange(val) {
      this.page = val
      this.fetchData()
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss">
  .page-archive-index {
    .el-aside {
      color: #333;
      text-align: center;
      padding: 10px 0;
    }
    .el-main {
      margin-left: 20px;
      padding: 0 20px;
    }

    .custom-tree-node {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 14px;
      padding-right: 8px;
    }
  }
</style>
