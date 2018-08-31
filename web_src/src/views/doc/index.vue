<template>
  <section>
    <div class="app-container page-doc-index">
      <!--工具条-->
      <el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
        <el-form :inline="true" :model="filters">
          <el-form-item>
            <el-input v-model="filters.search_word" size="small" placeholder="关键字" />
          </el-form-item>
          <el-form-item>
            <el-tooltip class="item" effect="dark" content="搜索" placement="top">
              <el-button size="mini" circle @click="fetchData"><i class="el-icon-search" /></el-button>
            </el-tooltip>
          </el-form-item>
          <el-form-item>
            <el-tooltip class="item" effect="dark" content="添加文档" placement="top">
              <router-link :to="{ name: 'Doc-Create'}"><el-button type="primary" size="mini" circle><i class="el-icon-plus" /></el-button></router-link>
            </el-tooltip>
          </el-form-item>
        </el-form>
      </el-col>

      <el-table v-loading.body="listLoading" :data="list" element-loading-text="拼命加载中" fit>
        <el-table-column label="标题" header-align="center">
          <template slot-scope="scope">
            <router-link :to="{ name: 'Doc-View', params: { id: scope.row.id } }" target="_blank" style="text-decoration: underline;">{{ scope.row.title }}</router-link>
          </template>
        </el-table-column>
        <el-table-column label="作者" header-align="center" align="center" width="100">
          <template slot-scope="scope">
            {{ scope.row.author_name }}
          </template>
        </el-table-column>
        <el-table-column label="发布状态" header-align="center" align="center" width="100">
          <template slot-scope="scope">
            <el-tag :type="scope.row.published | publishedFilter" size="small">{{ scope.row.published | publishedNameFilter }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="创建于" header-align="center" align="center" width="100">
          <template slot-scope="scope">
            {{ scope.row.create_at | formatDate }}
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
            <el-tooltip class="item" effect="dark" content="修改" placement="top">
              <router-link :to="{ name: 'Doc-Create', query: { id: scope.row.id }}"><el-button type="text"><i class="el-icon-edit" /></el-button></router-link>
            </el-tooltip>
            <el-tooltip class="item" effect="dark" content="发布" placement="top">
              <el-button type="text" style="color: #409EFF;" @click="handlePublish(scope.$index, scope.row)"><i class="el-icon-doooc-fabu" /></el-button>
            </el-tooltip>
            <el-tooltip class="item" effect="dark" content="删除" placement="top">
              <el-button type="text" style="color: #F56C6C;" @click="handleDel(scope.$index, scope.row)"><i class="el-icon-delete" /></el-button>
            </el-tooltip>
          </template>
        </el-table-column>
      </el-table>

      <!--工具条-->
      <el-col :span="24" class="toolbar">
        <el-pagination :page-size="pageSize" :total="total" layout="total, prev, pager, next, jumper" style="float:right;" @current-change="handleCurrentChange" />
      </el-col>

      <el-dialog
        :show-close="false"
        :visible.sync="viewDocDialogVisible"
        :fullscreen="true"
        title="">
        <div slot="title">
          <a :href="downloadMdUrl(viewedDoc.id)" download><el-button type="primary" icon="el-icon-download" size="small">MD</el-button></a>
          <a :href="downloadHtmlUrl(viewedDoc.id)" download><el-button type="primary" icon="el-icon-download" size="small">HTML</el-button></a>
          <a :href="downloadDocxUrl(viewedDoc.id)" download><el-button type="primary" icon="el-icon-download" size="small">DOCX</el-button></a>
          <a :href="downloadPdfUrl(viewedDoc.id)" download><el-button type="primary" icon="el-icon-download" size="small">PDF</el-button></a>
          <a :href="downloadPptxUrl(viewedDoc.id)" download><el-button type="primary" icon="el-icon-download" size="small">PPTX</el-button></a>
        </div>
        <mavon-editor
          v-model="viewedDoc.content"
          :toolbars-flag="false"
          :subfield="false"
          :navigation="true"
          default-open="preview"/>
      </el-dialog>
    </div>
  </section>
</template>

<script>
import { getList, del, publish, downloadMd, downloadHtml, downloadPdf, downloadDocx, downloadPptx } from '@/api/doc'
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
      filters: {
        search_word: ''
      },
      list: null,
      listLoading: true,
      total: 0,
      page: 1,
      pageSize: 10,
      viewDocDialogVisible: false,
      viewedDoc: {
        content: ''
      }
    }
  },
  computed: {
    ...mapGetters(['enums']),
    listQuery: function() {
      return {
        limit: this.pageSize,
        offset: (this.page - 1) * this.pageSize,
        search_word: this.filters.search_word
      }
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList(this.listQuery).then(response => {
        this.list = response.results
        this.total = response.count
        this.listLoading = false
      })
    },
    handleCurrentChange(val) {
      this.page = val
      this.fetchData()
    },
    handleAdd() {
      // todo:
    },
    handleEdit(index, row) {
      // todo:
    },
    handleView(index, row) {
      this.viewDocDialogVisible = true
      this.viewedDoc = { ...row }
    },
    handleDel(index, row) {
      this.$confirm('确认删除吗？', '提示', {}).then(() => {
        del(row.id).then(res => {
          this.$message({
            message: '删除成功',
            type: 'success'
          })
          this.fetchData()
        })
      })
    },
    handlePublish(index, row) {
      this.$confirm('确认发布吗？', '提示', {}).then(() => {
        publish(row.id).then(res => {
          this.$message({
            message: '发布成功',
            type: 'success'
          })
          this.fetchData()
        })
      })
    },
    downloadMdUrl(id) {
      return downloadMd(id)
    },
    downloadHtmlUrl(id) {
      return downloadHtml(id)
    },
    downloadPdfUrl(id) {
      return downloadPdf(id)
    },
    downloadDocxUrl(id) {
      return downloadDocx(id)
    },
    downloadPptxUrl(id) {
      return downloadPptx(id)
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss">
  .page-doc-index .el-dialog__body {
    padding-top: 5px;
  }

  .page-doc-index .op .el-button {
    margin-left: 10px;
  }

  .page-doc-index .el-table td, .page-doc-index .el-table th {
    padding: 3px 0;
  }
</style>
