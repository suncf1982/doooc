(window.webpackJsonp=window.webpackJsonp||[]).push([["chunk-7d27"],{"4WHG":function(t,n,o){},"5HWN":function(t,n,o){"use strict";o.d(n,"i",function(){return r}),o.d(n,"h",function(){return d}),o.d(n,"a",function(){return u}),o.d(n,"n",function(){return c}),o.d(n,"b",function(){return a}),o.d(n,"j",function(){return i}),o.d(n,"m",function(){return l}),o.d(n,"l",function(){return s}),o.d(n,"k",function(){return f}),o.d(n,"e",function(){return p}),o.d(n,"d",function(){return m}),o.d(n,"f",function(){return h}),o.d(n,"c",function(){return w}),o.d(n,"g",function(){return b}),o.d(n,"o",function(){return v});var e=o("t3Un");function r(t){return Object(e.a)({url:"/docs/",method:"get",params:t})}function d(t){return Object(e.a)({url:"/docs/"+t+"/",method:"get"})}function u(t){return Object(e.a)({url:"/docs/",method:"post",data:t})}function c(t){return Object(e.a)({url:"/docs/"+t.id+"/",method:"put",data:t})}function a(t){return Object(e.a)({url:"/docs/"+t+"/",method:"delete"})}function i(t){return Object(e.a)({url:"/docs/publish/"+t+"/",method:"put"})}function l(){return Object(e.a)({url:"/docs/pupulartags/",method:"get"})}function s(){return Object(e.a)({url:"/docs/pupularkeywords/",method:"get"})}function f(){return Object(e.a)({url:"/docs/populardocs/",method:"get"})}function p(t){return"http://121.42.144.73/docs/download/md/"+t+"/"}function m(t){return"http://121.42.144.73/docs/download/html/"+t+"/"}function h(t){return"http://121.42.144.73/docs/download/pdf/"+t+"/"}function w(t){return"http://121.42.144.73/docs/download/docx/"+t+"/"}function b(t){return"http://121.42.144.73/docs/download/pptx/"+t+"/"}function v(){return"http://121.42.144.73/resources/upload/"}},"5nfn":function(t,n,o){"use strict";var e=o("4WHG");o.n(e).a},"9ZrR":function(t,n,o){"use strict";o.r(n);var e=o("QbLZ"),r=o.n(e),d=o("L2JU"),u=o("5HWN"),c={name:"ViewDoc",data:function(){return{document:{content:""}}},computed:r()({},Object(d.b)(["enums"])),created:function(){this.id=this.$route.params.id,this.fetchData()},methods:{fetchData:function(){var t=this;Object(u.h)(this.id).then(function(n){t.document=r()({},n)})},downloadMdUrl:function(t){return Object(u.e)(t)},downloadHtmlUrl:function(t){return Object(u.d)(t)},downloadPdfUrl:function(t){return Object(u.f)(t)},downloadDocxUrl:function(t){return Object(u.c)(t)},downloadPptxUrl:function(t){return Object(u.g)(t)}}},a=(o("5nfn"),o("KHd+")),i=Object(a.a)(c,function(){var t=this,n=t.$createElement,o=t._self._c||n;return o("section",[o("div",{staticClass:"app-container view-doc"},[o("div",{staticStyle:{"margin-bottom":"20px"}},[o("a",{attrs:{href:t.downloadMdUrl(t.document.id),download:""}},[o("el-button",{attrs:{type:"primary",icon:"el-icon-download",size:"small"}},[t._v("MD")])],1),t._v(" "),o("a",{attrs:{href:t.downloadHtmlUrl(t.document.id),download:""}},[o("el-button",{attrs:{type:"primary",icon:"el-icon-download",size:"small"}},[t._v("HTML")])],1),t._v(" "),o("a",{attrs:{href:t.downloadDocxUrl(t.document.id),download:""}},[o("el-button",{attrs:{type:"primary",icon:"el-icon-download",size:"small"}},[t._v("DOCX")])],1),t._v(" "),o("a",{attrs:{href:t.downloadPdfUrl(t.document.id),download:""}},[o("el-button",{attrs:{type:"primary",icon:"el-icon-download",size:"small"}},[t._v("PDF")])],1),t._v(" "),o("a",{attrs:{href:t.downloadPptxUrl(t.document.id),download:""}},[o("el-button",{attrs:{type:"primary",icon:"el-icon-download",size:"small"}},[t._v("PPTX")])],1)]),t._v(" "),o("mavon-editor",{attrs:{"toolbars-flag":!1,subfield:!1,navigation:!0,"default-open":"preview","font-size":"14px"},model:{value:t.document.content,callback:function(n){t.$set(t.document,"content",n)},expression:"document.content"}})],1)])},[],!1,null,null,null);i.options.__file="view.vue";n.default=i.exports}}]);