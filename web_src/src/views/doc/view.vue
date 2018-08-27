<template>
  <section>
  <div class="app-container view-doc">
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
import { get as getDocDetail } from "@/api/doc";

export default {
  name: "viewDoc",
  created() {
    this.id = this.$route.params.id;
    this.fetchData();
  },
  data() {
    return {
      document: {
        content: ''
      }
    };
  },
  methods: {
    fetchData() {
      getDocDetail(this.id).then(res => {
        this.document = {...res};
      })
    },
  },
  computed: {
    ...mapGetters(["enums"]),
  }
};
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.view-doc {
  margin: 0;
}
</style>
