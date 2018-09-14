<template>
  <section>
    <div class="app-container view-doc">
      <div class="op">
        <el-button type="text" icon="el-icon-printer" class="op-print" @click="print">打印</el-button>
        <el-button type="text" icon="el-icon-doooc-fenxiang" class="op-share" @click="shareDialogVisible = true">分享</el-button>
        <div style="display: inline-block; float: right;">
          <a :href="downloadMdUrl(document.id)" download class="op-download-md"><el-button type="primary" icon="el-icon-download" size="mini" plain>MD</el-button></a>
          <a :href="downloadHtmlUrl(document.id)" download class="op-download-html"><el-button type="primary" icon="el-icon-download" size="mini" plain>HTML</el-button></a>
          <a :href="downloadDocxUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="mini" plain>Word</el-button></a>
          <!-- <a :href="downloadPdfUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="mini" plain>PDF</el-button></a> -->
          <a :href="downloadPptxUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="mini" plain>PPT</el-button></a>
        </div>
      </div>
      <mavon-editor
        v-model="document.content"
        :toolbars-flag="false"
        :subfield="false"
        :navigation="true"
        default-open="preview"
        font-size="14px" />
      <div class="attachment">
        <a v-for="(attachment, index) in document.attachments" :key="index" :href="downloadAttachment(attachment.url)" download><el-button type="text" icon="el-icon-tickets"> {{ attachment.name }} </el-button></a>
      </div>
      <el-dialog :visible.sync="shareDialogVisible" title="分享文档">
        <el-form>
          <el-form-item label="">
            <el-input v-model="share_to" auto-complete="off" placeholder="邮箱" />
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
  share,
  downloadFile
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
    downloadAttachment(url) {
      return downloadFile(url)
    },
    share() {
      share(this.document.id, this.share_to).then(res => {
        this.shareDialogVisible = false
      })
    },
    print() {
      const newhtml = document.getElementsByClassName('v-note-show')[0].innerHTML
      const oldhtml = document.body.innerHTML
      document.body.innerHTML = newhtml
      window.print()
      window.location.reload()
      document.body.innerHTML = oldhtml
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
  .v-note-navigation-title{
    display: none;
  }
  .v-note-wrapper .v-note-panel .v-note-navigation-wrapper .v-note-navigation-title {
    font-size: 16px;
  }
  .v-note-show, .attachment {
    padding-left: 250px !important;
    @media screen and (max-width:768px) {
      padding-left: 0 !important;
    }
  }
  .attachment {
    margin-top: 20px;
    a {
      display: block;
    }
  }
  .v-note-navigation-wrapper {
    left: 0;
    border-right: solid 1px #eaecef !important;
    box-shadow: none !important;

    @media screen and (max-width:768px) {
      display: none !important;
    }
  }
  .v-note-navigation-close {
    display: none;
  }
  .v-note-wrapper .v-note-panel.shadow {
    border: none;
    box-shadow: none;
  }
  .v-note-wrapper .v-note-panel .v-note-show .v-show-content, .v-note-wrapper .v-note-panel .v-note-show .v-show-content-html {
    background: #fff;
  }
  .op {
    padding-bottom: 10px;
    border-bottom: solid 1px #eaecef;
    &-print, &-download-md, &-download-html {
      @media screen and (max-width:768px) {
        display: none !important;
      }
    }
  }
}
</style>
