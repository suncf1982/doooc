<template>
  <section>
    <div class="app-container create-doc">
      <el-form ref="form" :model="addForm" label-position="top" label-width="80px" @keyup.ctrl.83.native.stop.prevent="onSubmit('form')">
        <el-form-item
          :rules="[{ required: true, message: '标题不能为空'}]"
          label=""
          prop="title">
          <el-input v-model="addForm.title" placeholder="标题" />
        </el-form-item>
        <el-form-item
          :rules="[{ required: true, message: '内容不能为空'}]"
          label=""
          prop="content">
          <el-button type="warning" icon="el-icon-search" size="mini" style="margin-bottom: 10px;" @click="onSelectDocTemplates">选择模板快速开始</el-button>
          <mavon-editor
            ref="md"
            v-model="addForm.content"
            font-size="14px"
            @imgAdd="onImgAdd" />
        </el-form-item>
        <el-form-item label="">
          <el-select v-model="addForm.tech_stack" clearable size="small" placeholder="请选择技术栈">
            <el-option
              v-for="item in techStackOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value" />
          </el-select>
          <el-tag v-for="tag in addForm.tags" :key="tag" :disable-transitions="true" closable style="margin-right: 5px" @close="onRemoveTag(tag)">{{ tag }}</el-tag>
          <el-input v-show="addingTag" v-model="newTag" placeholder="添加标签" clearable size="small" style="width: 120px;" />
          <el-button v-show="!addingTag" type="primary" icon="el-icon-plus" size="mini" title="添加标签" circle @click.native="onAddTag()" />
          <el-button v-show="addingTag" type="success" icon="el-icon-check" size="mini" title="确定" circle @click.native="onConfirmAddTag()" />
          <el-button v-show="addingTag" type="danger" icon="el-icon-close" size="mini" title="取消" circle @click.native="onCancelAddTag()" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" icon="el-icon-doooc-baocun" size="small" @click.native="onSubmit('form')">保存</el-button>
        </el-form-item>
      </el-form>
      <el-dialog
        :visible.sync="selTplDialogVisible"
        top="5vh"
        title="选择文档模块"
        width="80%">
        <el-row>
          <el-col v-for="(template, index) in templates" :key="template.id" :span="6" :offset="index > 0 ? 2 : 0">
            <el-card :body-style="{ padding: '0px' }" shadow="hover">
              <img :src="template.preview_image" class="image">
              <div style="padding: 14px;">
                <span>{{ template.name }}</span>
                <div class="bottom clearfix">
                  <time class="time">{{ template.update_at | formatDate }}</time>
                  <el-button type="text" class="button" icon="el-icon-check" @click="onTemplateSelected(template.id)">选择</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-dialog>
    </div>
  </section>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
import { get as getDocDetail, create, update, uploadFile, getTemplates, getTemplateContent } from '@/api/doc'
import moment from 'moment'

moment.locale('zh-cn')
const form = {
  title: '',
  author: '',
  content: '',
  tech_stack: '',
  tags: []
}
export default {
  name: 'CreateDoc',
  filters: {
    formatDate(dateStr) {
      return moment(dateStr).fromNow()
    }
  },
  data() {
    return {
      addForm: { ...form },
      addLoading: false,
      addingTag: false,
      newTag: '',
      selTplDialogVisible: false,
      templates: []
    }
  },
  computed: {
    ...mapGetters(['enums']),
    techStackOptions: function() {
      return Array.from(Object.entries(this.enums.TECH_STACK), function(item) {
        return { value: item[0], label: item[1] }
      })
    }
  },
  created() {
    const id = this.$route.query.id
    if (id !== undefined) {
      this.id = id
      this.fetchData()
    }
  },
  methods: {
    fetchData() {
      getDocDetail(this.id).then(res => {
        this.addForm = { ...res }
      })
    },
    onImgAdd(pos, file) {
      const formdata = new FormData()
      formdata.append('file', file)
      axios({
        url: uploadFile(),
        method: 'post',
        data: formdata,
        headers: { 'Content-Type': 'multipart/form-data' }
      }).then((res) => {
        const file_url = process.env.BASE_API + res.data.url
        this.$refs.md.$img2Url(pos, file_url)
      })
    },
    onAddTag() {
      this.addingTag = true
    },
    onConfirmAddTag() {
      this.addForm.tags.push(this.newTag)
      this.newTag = ''
      this.addingTag = false
    },
    onCancelAddTag() {
      this.newTag = ''
      this.addingTag = false
    },
    onRemoveTag(tag) {
      this.addForm.tags.splice(this.addForm.tags.indexOf(tag), 1)
    },
    onSubmit: function(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.addLoading = true
          const param = Object.assign({}, this.addForm)
          if (param.id === undefined) {
            create(param).then(res => {
              this.addLoading = false
              // NProgress.done();
              this.$message({
                message: '保存成功',
                type: 'success'
              })
              this.id = res.id
              this.fetchData()
              this.$router.push({ path: '/doc/create', query: { id: res.id }})
            })
          } else {
            update(param).then(res => {
              this.addLoading = false
              // NProgress.done();
              this.$message({
                message: '保存成功',
                type: 'success'
              })

              this.fetchData()
            })
          }
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    onSelectDocTemplates() {
      getTemplates().then(res => {
        this.templates = res.results
        this.selTplDialogVisible = true
      })
    },
    onTemplateSelected(id) {
      getTemplateContent(id).then(res => {
        this.addForm.content = res.content
        this.addForm.title = res.template.name
        this.selTplDialogVisible = false
      })
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .image {
    width: 100%;
    height: 240px;
    display: block;
  }
  .button {
    padding: 0;
    float: right;
  }
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }
  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  .clearfix:after {
      clear: both
  }
  .time {
    font-size: 13px;
    color: #999;
  }
</style>
