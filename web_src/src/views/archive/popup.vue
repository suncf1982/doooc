<template>
  <el-tree :data="list" :props="defaultProps" @node-click="handleNodeClick" />
</template>

<script>
import { getList } from '@/api/archive'

export default {
  data() {
    return {
      list: [],
      defaultProps: {
        children: 'children',
        label: 'name'
      }
    }
  },
  created() {
    getList().then(response => {
      this.list = response.results
    })
  },
  methods: {
    handleNodeClick(data) {
      console.log(data)
      this.$emit('selectedArchiveId', data.id)
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
</style>
