<template>
  <ul class="timeline">
    <slot></slot>
  </ul>
</template>

<script>
  export default {
    name: 'time-line'
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>

  .timeline {
    position: relative;
    margin: 0 0 30px 0;
    padding: 0;
    list-style: none;

    &:before {
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      width: 4px;
      background: #ddd;
      left: 31px;
      margin: 0;
      border-radius: 2px;
    }
  }
</style>