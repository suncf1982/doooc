<template>
  <section>
  <div class="app-container dashboard">
    <div class="dashboard-container">
      
    </div>
  </div>
  </section>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "dashboard",
  created() {},
  data() {
    return {
    };
  },
  computed: {
    ...mapGetters(["dependences"])
  }
};
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
}
</style>
