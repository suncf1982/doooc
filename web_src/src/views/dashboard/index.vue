<template>
  <div class="dashboard-container">
    <div :class="{ 'search-position-normal': !isSearching, 'search-position-top': isSearching }">
      <h2 :class="{title: !isSearching, 'title-hide': isSearching}">全&nbsp;文&nbsp;检&nbsp;索&nbsp;<i class="el-icon-search" /></h2>
      <el-input placeholder="请输入关键字" class="input-with-select" v-model.trim="searchedText" @keyup.enter.native="onSearch">
        <el-button slot="append" type="primary" icon="el-icon-search" @click.native="onSearch" />
      </el-input>
    </div>
    <div class="search-results">
      <dl v-for="item in list" :key="item.key" class="result-item">
        <dt class="result-item-title">
          <router-link :to="{ name: 'Doc-View', params: { id: item.id } }" target="_blank">{{ item.title }}</router-link>
        </dt>
        <dd class="result-item-content" v-html="item.searched"></dd>
        <dd class="result-item-tags">
          <el-tag type="success">作者：<a @click="onSearchAuthor(item.author)">{{ item.author_name }}</a></el-tag>
          <el-tag type="warning">领域：<a @click="onSearchTechStack(item.tech_stack)">{{ item.tech_stack_name }}</a></el-tag>
          <el-tag  v-for="tag in item.tags" :key="tag" style="margin-right: 4px">
            <a v-on:click="onSearchTag(tag)"><em>{{ tag }}</em></a>
          </el-tag>
        </dd>
        <dd class="result-item-link">
          <router-link :to="{ name: 'Doc-View', params: { id: item.id } }" target="_blank">{{ displayViewUrl(item.id) }}</router-link>
        </dd>
      </dl>
      <div v-if="isSearching && total===0" class="sorry">很抱歉，没有找到与<span style="color: red; margin: 0 5px;">{{ searchedText }}</span>相关的文档。</div>
    </div>
    <div :class="{'pupular-shortcut-no-margin': isSearching}" class="pupular-shortcut">
      <dl>
        <dt>热门标签</dt>
        <dd>
          <el-tag v-for="pupularTag in pupularTags" :key="pupularTag.tag__name" size="mini" style="margin-right: 4px">
            <a @click="onSearchTag(pupularTag.tag__name)"><em>{{ pupularTag.tag__name }}</em></a>
          </el-tag>
        </dd>
      </dl>
      <dl>
        <dt>都在搜索</dt>
        <dd>
          <el-tag v-for="pupularKeyword in pupularKeywords" :key="pupularKeyword.keyword" size="mini" style="margin-right: 4px">
            <a @click="onSearch(pupularKeyword.keyword)"><em>{{ pupularKeyword.keyword }}</em></a>
          </el-tag>
        </dd>
      </dl>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getList as search, pupularTags, pupularKeywords } from '@/api/doc'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {
    pupularTags().then(res => {
      this.pupularTags = res
    });

    pupularKeywords().then(res => {
      this.pupularKeywords = res
    })
  },
  data() {
    return {
      searchedText: '',
      isSearching: false,
      pupularTags: [],
      pupularKeywords: [],
      list: [],
      total: 0,
      page: 1,
      pageSize: 10
    };
  },
  methods: {
    onSearch(keyword) {
      debugger
      if (Object.prototype.toString.call(keyword) === '[object String]') {
        this.searchedText = keyword
      }
      if (!this.searchedText) {
        return
      }
      this.isSearching = true
      search(this.getQuery({ search_word: this.searchedText })).then(
        response => {
          this.list = response.results
          this.total = response.count
        }
      );
    },
    onSearchAuthor(author) {
      this.isSearching = true
      this.searchedText = ''
      search(this.getQuery({ author: author })).then(response => {
        this.list = response.results
        this.total = response.count
      });
    },
    onSearchTechStack(techStack) {
      this.isSearching = true
      this.searchedText = ''
      search(this.getQuery({ tech_stack: techStack })).then(response => {
        this.list = response.results
        this.total = response.count
      });
    },
    onSearchTag(tag) {
      this.isSearching = true
      this.searchedText = ''
      search(this.getQuery({ tag: tag })).then(response => {
        this.list = response.results
        this.total = response.count
      })
    },
    displayViewUrl(id) {
      return 'http://' + location.host + '/#/view/' + id
    },
    getQuery(kvpairs) {
      const params = {
        limit: this.pageSize,
        offset: (this.page - 1) * this.pageSize
      }
      Object.assign(params, kvpairs)
      return params
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.dashboard {
  &-container {
    margin: 15px;

    .search-position {
      &-normal {
        margin: 160px auto;
        margin-bottom: 20px;
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

    .pupular-shortcut {
      margin: 0 auto;
      width: 80%;
      border-top: solid 1px #c0c4cc;
      &-no-margin {
        margin: 0;
      }
      dl {
        height: 30px;
      }
      dt {
        float: left;
        width: 60px;
        font-size: 14px;
        color: #303133;
        line-height: 30px;
      }
      dd {
        margin-left: 80px;
        line-height: 30px;
      }
    }
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
