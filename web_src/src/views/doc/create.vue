<template>
  <section>
  <div class="app-container create-doc">
    <el-form ref="form" :model="addForm" label-position="top" label-width="80px">
        <el-form-item label="文档标题">
            <el-input v-model="addForm.title"></el-input>
        </el-form-item>
        <el-form-item label="">
            <mavon-editor v-model="addForm.content"/>
        </el-form-item>
        <el-form-item label="">
            <el-select v-model="addForm.tech_stack" clearable placeholder="请选择技术栈">
                <el-option
                    v-for="item in techStackOptions"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
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
import { create, update } from "@/api/doc";
let form = {
  title: "",
  author: "",
  content: "",
  tech_stack: ""
};
export default {
  name: "createDoc",
  created() {},
  data() {
    return {
      addForm: { ...form },
      addLoading: false
    };
  },
  methods: {
    onSubmit: function(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.$confirm("确认保存吗？", "提示", {}).then(() => {
            this.addLoading = true;
            let param = Object.assign({}, this.addForm);
            if (param.id === "" || param.id === undefined) {
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
          });
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
.create-doc {
  margin: 30px;
}
</style>
