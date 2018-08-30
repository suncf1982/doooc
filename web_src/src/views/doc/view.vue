<template>
  <section>
    <div class="app-container view-doc">
      <div style="margin-bottom: 20px;">
        <a :href="downloadMdUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="small">MD</el-button></a>
        <a :href="downloadHtmlUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="small">HTML</el-button></a>
        <a :href="downloadDocxUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="small">DOCX</el-button></a>
        <a :href="downloadPdfUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="small">PDF</el-button></a>
        <a :href="downloadPptxUrl(document.id)" download><el-button type="primary" icon="el-icon-download" size="small">PPTX</el-button></a>
      </div>
      <mavon-editor
        v-model="document.content"
        :toolbars-flag="false"
        :subfield="false"
        :navigation="true"
        default-open="preview"
        font-size="14px" />
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
  downloadPptx
} from '@/api/doc'

export default {
  name: 'ViewDoc',
  data() {
    return {
      document: {
        content: ''
      }
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
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss">
.view-doc {
  margin: 0;
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
