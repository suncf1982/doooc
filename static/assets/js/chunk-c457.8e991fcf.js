(window.webpackJsonp=window.webpackJsonp||[]).push([["chunk-c457"],{"+h0c":function(t,e,n){},"5HWN":function(t,e,n){"use strict";n.d(e,"l",function(){return o}),n.d(e,"j",function(){return a}),n.d(e,"a",function(){return c}),n.d(e,"u",function(){return i}),n.d(e,"c",function(){return s}),n.d(e,"s",function(){return u}),n.d(e,"o",function(){return l}),n.d(e,"t",function(){return d}),n.d(e,"r",function(){return h}),n.d(e,"q",function(){return p}),n.d(e,"p",function(){return f}),n.d(e,"g",function(){return m}),n.d(e,"f",function(){return _}),n.d(e,"h",function(){return g}),n.d(e,"e",function(){return v}),n.d(e,"i",function(){return b}),n.d(e,"v",function(){return k}),n.d(e,"n",function(){return w}),n.d(e,"m",function(){return y}),n.d(e,"k",function(){return O}),n.d(e,"b",function(){return j}),n.d(e,"d",function(){return S});var r=n("t3Un");function o(t){return Object(r.a)({url:"/docs/",method:"get",params:t})}function a(t){return Object(r.a)({url:"/docs/"+t+"/",method:"get"})}function c(t){return Object(r.a)({url:"/docs/",method:"post",data:t})}function i(t){return Object(r.a)({url:"/docs/"+t.id+"/",method:"put",data:t})}function s(t){return Object(r.a)({url:"/docs/"+t+"/",method:"delete"})}function u(t){return Object(r.a)({url:"/docs/search/",method:"get",params:t})}function l(t){return Object(r.a)({url:"/docs/publish/"+t+"/",method:"put"})}function d(t,e){return Object(r.a)({url:"/docs/share/"+t+"/",method:"put",data:{share_to:e}})}function h(){return Object(r.a)({url:"/docs/pupulartags/",method:"get"})}function p(){return Object(r.a)({url:"/docs/pupularkeywords/",method:"get"})}function f(){return Object(r.a)({url:"/docs/populardocs/",method:"get"})}function m(t){return"http://121.42.144.73/docs/download/md/"+t+"/"}function _(t){return"http://121.42.144.73/docs/download/html/"+t+"/"}function g(t){return"http://121.42.144.73/docs/download/pdf/"+t+"/"}function v(t){return"http://121.42.144.73/docs/download/docx/"+t+"/"}function b(t){return"http://121.42.144.73/docs/download/pptx/"+t+"/"}function k(){return"http://121.42.144.73/resources/upload/"}function w(t){return Object(r.a)({url:"/docs/templates/",method:"get",params:t})}function y(t){return Object(r.a)({url:"/docs/templates/"+t+"/",method:"get"})}function O(t){return Object(r.a)({url:"/docs/favorites/",method:"get",params:t})}function j(t){return Object(r.a)({url:"/docs/favorites/",method:"post",data:t})}function S(t){return Object(r.a)({url:"/docs/favorites/"+t+"/",method:"delete"})}},ObBx:function(t,e,n){"use strict";var r=n("+h0c");n.n(r).a},lAbF:function(t,e,n){"use strict";n.r(e);var r=n("P2sY"),o=n.n(r),a=n("QbLZ"),c=n.n(a),i=n("L2JU"),s=n("5HWN"),u={name:"Dashboard",data:function(){return{searchedText:"",isSearching:!1,pupularTags:[],pupularKeywords:[],pupularDocs:[],list:[],total:0,page:1,pageSize:10}},computed:c()({},Object(i.b)(["name","roles"])),created:function(){var t=this;Object(s.r)().then(function(e){t.pupularTags=e}),Object(s.q)().then(function(e){t.pupularKeywords=e}),Object(s.p)().then(function(e){t.pupularDocs=e})},methods:{onSearch:function(t){var e=this;"[object String]"===Object.prototype.toString.call(t)&&(this.searchedText=t),this.searchedText&&(this.isSearching=!0,Object(s.s)(this.getQuery({search_word:this.searchedText})).then(function(t){e.list=t.results,e.total=t.count}))},onSearchAuthor:function(t){var e=this;this.isSearching=!0,this.searchedText="",Object(s.s)(this.getQuery({author:t})).then(function(t){e.list=t.results,e.total=t.count})},onSearchTechStack:function(t){var e=this;this.isSearching=!0,this.searchedText="",Object(s.s)(this.getQuery({tech_stack:t})).then(function(t){e.list=t.results,e.total=t.count})},onSearchTag:function(t){var e=this;this.isSearching=!0,this.searchedText="",Object(s.s)(this.getQuery({tag:t})).then(function(t){e.list=t.results,e.total=t.count})},displayViewUrl:function(t){return"http://"+location.host+"/#/view/"+t},getQuery:function(t){var e={limit:this.pageSize,offset:(this.page-1)*this.pageSize};return o()(e,t),e},favorite:function(t){var e=this;Object(s.b)({doc:t}).then(function(t){e.$message({message:"已收藏",type:"success"})})},downloadMdUrl:function(t){return Object(s.g)(t)},downloadHtmlUrl:function(t){return Object(s.f)(t)},downloadPdfUrl:function(t){return Object(s.h)(t)},downloadDocxUrl:function(t){return Object(s.e)(t)},downloadPptxUrl:function(t){return Object(s.i)(t)}}},l=(n("ObBx"),n("KHd+")),d=Object(l.a)(u,function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"dashboard-container"},[n("div",{class:{"search-position-normal":!t.isSearching,"search-position-top":t.isSearching}},[n("h2",{class:{title:!t.isSearching,"title-hide":t.isSearching}},[t._v("全 文 检 索 "),n("i",{staticClass:"el-icon-search"})]),t._v(" "),n("el-input",{staticClass:"input-with-select",attrs:{placeholder:"请输入关键字"},nativeOn:{keyup:function(e){return"button"in e||!t._k(e.keyCode,"enter",13,e.key,"Enter")?t.onSearch(e):null}},model:{value:t.searchedText,callback:function(e){t.searchedText="string"==typeof e?e.trim():e},expression:"searchedText"}},[n("el-button",{attrs:{slot:"append",type:"primary",icon:"el-icon-search"},nativeOn:{click:function(e){return t.onSearch(e)}},slot:"append"})],1)],1),t._v(" "),n("div",{staticClass:"search-results"},[t._l(t.list,function(e){return n("dl",{key:e.key,staticClass:"result-item"},[n("dt",{staticClass:"result-item-title"},[n("router-link",{attrs:{to:{name:"Doc-View",params:{id:e.id}},target:"_blank"}},[t._v(t._s(e.title))])],1),t._v(" "),n("dd",{staticClass:"result-item-content",domProps:{innerHTML:t._s(e.searched)}}),t._v(" "),n("dd",{staticClass:"result-item-tags"},[n("el-tag",{attrs:{type:"success"}},[t._v("作者："),n("a",{on:{click:function(n){t.onSearchAuthor(e.author)}}},[t._v(t._s(e.author_name))])]),t._v(" "),n("el-tag",{attrs:{type:"warning"}},[t._v("领域："),n("a",{on:{click:function(n){t.onSearchTechStack(e.tech_stack)}}},[t._v(t._s(e.tech_stack_name))])]),t._v(" "),t._l(e.tags,function(e){return n("el-tag",{key:e,staticStyle:{"margin-right":"4px"}},[n("a",{on:{click:function(n){t.onSearchTag(e)}}},[n("em",[t._v(t._s(e))])])])})],2),t._v(" "),n("dd",{staticClass:"result-item-link"},[n("router-link",{staticStyle:{"margin-right":"10px"},attrs:{to:{name:"Doc-View",params:{id:e.id}},target:"_blank"}},[t._v(t._s(t.displayViewUrl(e.id)))]),t._v(" "),n("el-tooltip",{staticClass:"item",attrs:{effect:"dark",content:"收藏",placement:"top"}},[n("el-button",{staticClass:"result-item-link-favorite",attrs:{type:"text"},on:{click:function(n){t.favorite(e.id)}}},[n("i",{staticClass:"el-icon-doooc-shoucang"})])],1),t._v(" "),n("el-tooltip",{staticClass:"item",attrs:{effect:"dark",content:"下载MARKDOWN文件",placement:"top"}},[n("a",{attrs:{href:t.downloadMdUrl(e.id),download:""}},[n("el-button",{attrs:{type:"text",icon:"el-icon-doooc-markdown",size:"medium"}})],1)]),t._v(" "),n("el-tooltip",{staticClass:"item",attrs:{effect:"dark",content:"下载HTML文件",placement:"top"}},[n("a",{attrs:{href:t.downloadHtmlUrl(e.id),download:""}},[n("el-button",{attrs:{type:"text",icon:"el-icon-doooc-html",size:"medium"}})],1)]),t._v(" "),n("el-tooltip",{staticClass:"item",attrs:{effect:"dark",content:"下载WORD文件",placement:"top"}},[n("a",{attrs:{href:t.downloadDocxUrl(e.id),download:""}},[n("el-button",{attrs:{type:"text",icon:"el-icon-doooc-word",size:"medium"}})],1)]),t._v(" "),n("el-tooltip",{staticClass:"item",attrs:{effect:"dark",content:"下载PDF文件",placement:"top"}},[n("a",{attrs:{href:t.downloadPdfUrl(e.id),download:""}},[n("el-button",{attrs:{type:"text",icon:"el-icon-doooc-pdf",size:"medium"}})],1)]),t._v(" "),n("el-tooltip",{staticClass:"item",attrs:{effect:"dark",content:"下载PPT文件",placement:"top"}},[n("a",{attrs:{href:t.downloadPptxUrl(e.id),download:""}},[n("el-button",{attrs:{type:"text",icon:"el-icon-doooc-ppt",size:"medium"}})],1)])],1)])}),t._v(" "),t.isSearching&&0===t.total?n("div",{staticClass:"sorry"},[t._v("很抱歉，没有找到与"),n("span",{staticStyle:{color:"red",margin:"0 5px"}},[t._v(t._s(t.searchedText))]),t._v("相关的文档。")]):t._e()],2),t._v(" "),n("div",{staticClass:"pupular-shortcut",class:{"pupular-shortcut-no-margin":t.isSearching}},[n("dl",[n("dt",[t._v("热门标签")]),t._v(" "),n("dd",t._l(t.pupularTags,function(e){return n("el-tag",{key:e.tag__name,staticStyle:{"margin-right":"4px"},attrs:{size:"mini"}},[n("a",{on:{click:function(n){t.onSearchTag(e.tag__name)}}},[n("em",[t._v(t._s(e.tag__name))])])])}))]),t._v(" "),n("dl",[n("dt",[t._v("都在搜索")]),t._v(" "),n("dd",t._l(t.pupularKeywords,function(e){return n("el-tag",{key:e.keyword,staticStyle:{"margin-right":"4px"},attrs:{size:"mini"}},[n("a",{on:{click:function(n){t.onSearch(e.keyword)}}},[n("em",[t._v(t._s(e.keyword))])])])}))]),t._v(" "),n("dl",[n("dt",[t._v("最受欢迎")]),t._v(" "),n("dd",t._l(t.pupularDocs,function(e){return n("router-link",{key:e.id,staticClass:"doc-title",attrs:{to:{name:"Doc-View",params:{id:e.id}},target:"_blank"}},[t._v(t._s("<<"+e.title+">>"))])}))])])])},[],!1,null,"38c90bc4",null);d.options.__file="index.vue";e.default=d.exports}}]);