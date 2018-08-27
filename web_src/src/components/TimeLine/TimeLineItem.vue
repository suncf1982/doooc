<template>
  <div>
  <li class="time-label" :class="theme">
    <el-tag>{{label}}</el-tag>
  </li>
  <li>
    <div class="timeline-item">
      <span class="time">
        <slot></slot>
      </span>
      <h5 class="timeline-header">{{header}}</h5>
      <div class="timeline-body" v-html="body">
      </div>
      <div class="timeline-footer">
        <a class="btn btn-primary btn-xs"></a>
      </div>
    </div>
  </li>
  </div>
</template>

<script>
  export default {
    name: 'time-line-item',
    props: ['label', 'header', 'body', 'theme']
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>

  .timeline {
    li {
      position: relative;
      margin-right: 10px;
      margin-bottom: 15px;
      &:before, &:after  {
        content: " ";
        display: table;
      }
      &:after {
        clear: both;
      }

      .timeline-item {
        -webkit-box-shadow: 0 1px 1px rgba(0,0,0,0.1);
        box-shadow: 0 1px 1px rgba(0,0,0,0.1);
        border-radius: 3px;
        margin-top: 0;
        background: #fff;
        color: #444;
        margin-left: 60px;
        margin-right: 15px;
        padding: 0;
        position: relative;

        .time {
          color: #999;
          float: right;
          padding: 10px;
          font-size: 12px;
        }

        .timeline-header {
          margin: 0;
          color: #555;
          border-bottom: 1px solid #f4f4f4;
          padding: 10px;
          font-size: 13px;
          line-height: 1.1;
        }

        .timeline-body, .timeline-footer {
          padding: 10px;
        }
      }
    }

    .time-label {
      span {
        font-weight: 600;
      }
    }

    .el-tag {
      color: #fff;
    }

    .red {
      .el-tag {
        background: #dd4b39;
      }
    }

    .green {
      .el-tag {
        background: #00a65a;
      }
    }

    .orange {
      .el-tag {
        background: #f39c12;
      }
    }

    .blue {
      .el-tag {
        background: #00c0ef;
      }
    }
  }
</style>