<template>
  <section>
  <div class="app-container view-doc">
    <div style="margin-bottom: 20px;">
      <a :href="downloadMdUrl(document.id)" download><el-button type="primary" icon="el-icon-download">MD</el-button></a>
      <a :href="downloadHtmlUrl(document.id)" download><el-button type="primary" icon="el-icon-download">HTML</el-button></a>
      <a :href="downloadPdfUrl(document.id)" download><el-button type="primary" icon="el-icon-download">PDF</el-button></a>
      <a :href="downloadDocxUrl(document.id)" download><el-button type="primary" icon="el-icon-download">DOCX</el-button></a>
      <el-button type="primary" :disabled="true" icon="el-icon-download">PPT</el-button>
    </div>
    <mavon-editor 
      v-model="document.content"
      :toolbarsFlag="false"
      :subfield="false"
      defaultOpen="preview"
      :navigation="true"/>
  </div>
  </section>
</template>

<script>
import { mapGetters } from "vuex";
import {
  get as getDocDetail,
  downloadMd,
  downloadHtml,
  downloadPdf,
  downloadDocx
} from "@/api/doc";

export default {
  name: "viewDoc",
  created() {
    this.id = this.$route.params.id;
    this.fetchData();
  },
  data() {
    return {
      document: {
        content: ""
      }
    };
  },
  methods: {
    fetchData() {
      getDocDetail(this.id).then(res => {
        this.document = { ...res };
      });
    },
    downloadMdUrl(id) {
      return downloadMd(id);
    },
    downloadHtmlUrl(id) {
      return downloadHtml(id);
    },
    downloadPdfUrl(id) {
      return downloadPdf(id);
    },
    downloadDocxUrl(id) {
      return downloadDocx(id);
    }
  },
  computed: {
    ...mapGetters(["enums"])
  }
};
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
