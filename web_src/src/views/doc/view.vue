<template>
  <section>
    <div class="app-container view-doc">
      <div style="margin-bottom: 20px;">
        <a :href="downloadMdUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="small">MD</el-button></a>
        <a :href="downloadHtmlUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="small">HTML</el-button></a>
        <a :href="downloadDocxUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="small">DOCX</el-button></a>
        <a :href="downloadPdfUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="small">PDF</el-button></a>
        <a :href="downloadPptxUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="small">PPTX</el-button></a>
        <el-tooltip class="item" effect="dark" content="分享" placement="top">
          <el-button type="text" style="color: #F56C6C; float: right;" @click="shareDialogVisible = true"><i class="el-icon-doooc-fenxiang" /></el-button>
        </el-tooltip>
      </div>
      <mavon-editor
        v-model="document.content"
        :toolbars-flag="false"
        :subfield="false"
        :navigation="true"
        default-open="preview"
        font-size="14px" />

      <el-dialog :visible.sync="shareDialogVisible" title="分享文档">
        <el-form>
          <el-form-item label="邮箱地址" label-width="100px">
            <el-input v-model="share_to" auto-complete="off" />
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="shareDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="share()">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex'
import {
  get as getDocDetail,
  downloadMd,
  downloadHtml,
  downloadPdf,
  downloadDocx,
  downloadPptx,
  share
} from '@/api/doc'

export default {
  name: 'ViewDoc',
  data() {
    return {
      document: {
        content: ''
      },
      shareDialogVisible: false,
      share_to: ''
    }
  },
  computed: {
    ...mapGetters(['enums'])
  },
  created() {
    this.id = this.$route.params.id
    this.fetchData()
  },
  methods: {
    fetchData() {
      getDocDetail(this.id).then(res => {
        this.document = { ...res }
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
    },
    share() {
      share(this.document.id, this.share_to).then(res => {
        this.shareDialogVisible = false
      })
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss">
.view-doc {
  margin: 0;
  .markdown-body {
    font-size: 14px;
  }
  .v-note-wrapper .v-note-panel .v-note-navigation-wrapper .v-note-navigation-title {
    font-size: 16px;
  }
  .v-note-show {
    padding-left: 250px !important;
  }
  .v-note-navigation-wrapper {
    left: 0;
  }
  .v-note-navigation-close {
    display: none;
  }
}
</style>
