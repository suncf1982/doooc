<template>
  <section>
  <div class="app-container create-doc">
    <el-form ref="form" :model="addForm"  @keyup.ctrl.83.native.stop.prevent="onSubmit('form')" label-position="top" label-width="80px">
        <el-form-item label="文档标题" 
          prop="title"
          :rules="[{ required: true, message: '标题不能为空'}]">
            <el-input v-model="addForm.title"></el-input>
        </el-form-item>
        <el-form-item label=""
          prop="content"
          :rules="[{ required: true, message: '内容不能为空'}]">
            <mavon-editor v-model="addForm.content"/>
        </el-form-item>
        <el-form-item label="">
            <el-select v-model="addForm.tech_stack" clearable size="small" placeholder="请选择技术栈">
                <el-option
                    v-for="item in techStackOptions"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
            <el-tag v-for="tag in addForm.tags" :key="tag" closable @close="onRemoveTag(tag)" :disable-transitions="true" style="margin-right: 5px">{{tag}}</el-tag>
            <el-input v-show="addingTag" placeholder="添加标签" v-model="newTag" clearable size="small" style="width: 120px;"></el-input>
            <el-button v-show="!addingTag" @click.native="onAddTag()" type="primary" icon="el-icon-plus" size="mini" title="添加标签" circle></el-button>
            <el-button v-show="addingTag" @click.native="onConfirmAddTag()" type="success" icon="el-icon-check" size="mini" title="确定" circle></el-button>
            <el-button v-show="addingTag" @click.native="onCancelAddTag()" type="danger" icon="el-icon-close" size="mini" title="取消" circle></el-button>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click.native="onSubmit('form')">保存</el-button>
        </el-form-item>
    </el-form>
  </div>
  </section>
</template>

<script>
import { mapGetters } from "vuex";
import { get as getDocDetail, create, update } from "@/api/doc";
let form = {
  title: "",
  author: "",
  content: "",
  tech_stack: "",
  tags: []
};
export default {
  name: "createDoc",
  created() {
    let id = this.$route.query.id;
    if (id !== undefined) {
      this.id = id;
      this.fetchData();
    }
  },
  data() {
    return {
      addForm: { ...form },
      addLoading: false,
      addingTag: false,
      newTag: ""
    };
  },
  methods: {
    fetchData() {
      getDocDetail(this.id).then(res => {
        this.addForm = { ...res };
      });
    },
    onAddTag() {
      this.addingTag = true;
    },
    onConfirmAddTag() {
      this.addForm.tags.push(this.newTag);
      this.newTag = "";
      this.addingTag = false;
    },
    onCancelAddTag() {
      this.newTag = "";
      this.addingTag = false;
    },
    onRemoveTag(tag) {
      this.addForm.tags.splice(this.addForm.tags.indexOf(tag), 1);
    },
    onSubmit: function(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.addLoading = true;
          let param = Object.assign({}, this.addForm);
          if (param.id === undefined) {
            create(param).then(res => {
              this.addLoading = false;
              //NProgress.done();
              this.$message({
                message: "保存成功",
                type: "success"
              });

              this.fetchData();
            });
          } else {
            update(param).then(res => {
              this.addLoading = false;
              //NProgress.done();
              this.$message({
                message: "保存成功",
                type: "success"
              });

              this.fetchData();
            });
          }
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    }
  },
  computed: {
    ...mapGetters(["enums"]),
    techStackOptions: function() {
      return Array.from(Object.entries(this.enums.TECH_STACK), function(item) {
        return { value: item[0], label: item[1] };
      });
    }
  }
};
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
</style>
