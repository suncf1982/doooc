<template>
  <div class="dashboard-container">
    <div :class="{ 'search-position-normal': !isSearching, 'search-position-top': isSearching }">
      <h2 :class="{title: !isSearching, 'title-hide': isSearching}">全&nbsp;文&nbsp;检&nbsp;索&nbsp;<i class="el-icon-search"></i></h2>
      <el-input placeholder="请输入关键字" v-model.trim="searchedText" @keyup.enter.native="onSearch" class="input-with-select">
        <el-button @click.native="onSearch" slot="append" icon="el-icon-search"></el-button>
      </el-input>
    </div>
    <div class="search-results">
      <dl class="result-item" v-for="item in list" :key="item.key">
        <dt class="result-item-title">
          <router-link target="_blank" :to="{ name: 'Doc-View', params: { id: item.id }}">{{item.title}}</router-link>
        </dt>
        <dd class="result-item-content" v-html="item.searched"></dd>
        <dd class="result-item-tags">
          <el-tag type="success">作者：<a v-on:click="onSearchAuthor(item.author)">{{item.author_name}}</a></el-tag>
          <el-tag type="warning">领域：<a v-on:click="onSearchTechStack(item.tech_stack)">{{item.tech_stack_name}}</a></el-tag>
        </dd>
        <dd class="result-item-link">
          <router-link target="_blank" :to="{ name: 'Doc-View', params: { id: item.id }}">{{displayViewUrl(item.id)}}</router-link>
        </dd>
      </dl>
      <div class="sorry" v-if="isSearching && total===0">很抱歉，没有找到与<span style="color: red; margin: 0 5px;">{{searchedText}}</span>相关的文档。</div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { getList as search } from "@/api/doc";

export default {
  name: "Dashboard",
  data() {
    return {
      searchedText: "",
      isSearching: false,
      list: [],
      total: 0,
      page: 1,
      pageSize: 10
    };
  },
  methods: {
    onSearch() {
      if (!this.searchedText) {
        return;
      }
      this.isSearching = true;
      search(this.getQuery({search_word: this.searchedText})).then(response => {
        this.list = response.results;
        this.total = response.count;
      });
    },
    onSearchAuthor(author) {
      this.isSearching = true;
      this.searchedText = '';
      search(this.getQuery({author: author})).then(response => {
        this.list = response.results;
        this.total = response.count;
      });
    },
    onSearchTechStack(techStack) {
      this.isSearching = true;
      this.searchedText = '';
      search(this.getQuery({tech_stack: techStack})).then(response => {
        this.list = response.results;
        this.total = response.count;
      });
    },
    displayViewUrl(id) {
      return "http://" + location.host + "/#/view/" + id;
    },
    getQuery(kvpairs) {
      let params = {
        limit: this.pageSize,
        offset: (this.page - 1) * this.pageSize
      };
      Object.assign(params, kvpairs);
      return params;
    }
  },
  computed: {
    ...mapGetters(["name", "roles"])
  }
};
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.dashboard {
  &-container {
    margin: 15px;

    .search-position {
      &-normal {
        margin: 160px auto;
        width: 80%;
      }
      &-top {
        margin-top: 10px;
        width: 60%;
      }
    }

    .title {
      text-align: center;
      color: #409eff;
      &-hide {
        display: none;
      }
    }

    .search-results {
      width: 80%;
      .result-item {
        dd {
          margin-left: 0;
        }
        &-title {
          color: #409eff;
          line-height: 24px;
          a {
            text-decoration: underline;
          }
        }
        &-content {
          color: #333;
          font-size: 13px;
          line-height: 20px;
          margin-bottom: 5px;
        }
        &-tags {
          color: #333;
          font-size: 14px;
          margin-bottom: 5px;
          span {
            height: 22px;
            line-height: 22px;
          }
        }
        &-link {
          color: green;
          font-size: 13px;
        }
      }

      .sorry {
        font-size: 18px;
        margin: 20px 0;
      }
    }
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
