(window.webpackJsonp=window.webpackJsonp||[]).push([["chunk-88d6"],{"0tVQ":function(t,e,n){n("FlQf"),n("VJsP"),t.exports=n("WEpk").Array.from},"41oq":function(t,e,n){},"5HWN":function(t,e,n){"use strict";n.d(e,"i",function(){return a}),n.d(e,"h",function(){return r}),n.d(e,"a",function(){return i}),n.d(e,"n",function(){return c}),n.d(e,"b",function(){return d}),n.d(e,"j",function(){return u}),n.d(e,"m",function(){return s}),n.d(e,"l",function(){return l}),n.d(e,"k",function(){return f}),n.d(e,"e",function(){return m}),n.d(e,"d",function(){return p}),n.d(e,"f",function(){return h}),n.d(e,"c",function(){return g}),n.d(e,"g",function(){return v}),n.d(e,"o",function(){return b});var o=n("t3Un");function a(t){return Object(o.a)({url:"/docs/",method:"get",params:t})}function r(t){return Object(o.a)({url:"/docs/"+t+"/",method:"get"})}function i(t){return Object(o.a)({url:"/docs/",method:"post",data:t})}function c(t){return Object(o.a)({url:"/docs/"+t.id+"/",method:"put",data:t})}function d(t){return Object(o.a)({url:"/docs/"+t+"/",method:"delete"})}function u(t){return Object(o.a)({url:"/docs/publish/"+t+"/",method:"put"})}function s(){return Object(o.a)({url:"/docs/pupulartags/",method:"get"})}function l(){return Object(o.a)({url:"/docs/pupularkeywords/",method:"get"})}function f(){return Object(o.a)({url:"/docs/populardocs/",method:"get"})}function m(t){return"http://121.42.144.73/docs/download/md/"+t+"/"}function p(t){return"http://121.42.144.73/docs/download/html/"+t+"/"}function h(t){return"http://121.42.144.73/docs/download/pdf/"+t+"/"}function g(t){return"http://121.42.144.73/docs/download/docx/"+t+"/"}function v(t){return"http://121.42.144.73/docs/download/pptx/"+t+"/"}function b(){return"http://121.42.144.73/resources/upload/"}},E8gZ:function(t,e,n){var o=n("w6GO"),a=n("NsO/"),r=n("NV0k").f;t.exports=function(t){return function(e){for(var n,i=a(e),c=o(i),d=c.length,u=0,s=[];d>u;)r.call(i,n=c[u++])&&s.push(t?[n,i[n]]:i[n]);return s}}},IP1Z:function(t,e,n){"use strict";var o=n("2faE"),a=n("rr1i");t.exports=function(t,e,n){e in t?o.f(t,e,a(0,n)):t[e]=n}},UZfA:function(t,e,n){"use strict";var o=n("41oq");n.n(o).a},VJsP:function(t,e,n){"use strict";var o=n("2GTP"),a=n("Y7ZC"),r=n("JB68"),i=n("sNwI"),c=n("NwJ3"),d=n("tEej"),u=n("IP1Z"),s=n("fNZA");a(a.S+a.F*!n("TuGD")(function(t){Array.from(t)}),"Array",{from:function(t){var e,n,a,l,f=r(t),m="function"==typeof this?this:Array,p=arguments.length,h=p>1?arguments[1]:void 0,g=void 0!==h,v=0,b=s(f);if(g&&(h=o(h,p>2?arguments[2]:void 0,2)),void 0==b||m==Array&&c(b))for(n=new m(e=d(f.length));e>v;v++)u(n,v,g?h(f[v],v):f[v]);else for(l=b.call(f),n=new m;!(a=l.next()).done;v++)u(n,v,g?i(l,h,[a.value,v],!0):a.value);return n.length=v,n}})},nGDx:function(t,e,n){var o=n("Y7ZC"),a=n("E8gZ")(!0);o(o.S,"Object",{entries:function(t){return a(t)}})},oF3Q:function(t,e,n){t.exports={default:n("tgZa"),__esModule:!0}},rfXi:function(t,e,n){t.exports={default:n("0tVQ"),__esModule:!0}},tMUA:function(t,e,n){"use strict";n.r(e);var o=n("P2sY"),a=n.n(o),r=n("oF3Q"),i=n.n(r),c=n("rfXi"),d=n.n(c),u=n("QbLZ"),s=n.n(u),l=n("vDqi"),f=n.n(l),m=n("L2JU"),p=n("5HWN"),h={title:"",author:"",content:"",tech_stack:"",tags:[]},g={name:"CreateDoc",data:function(){return{addForm:s()({},h),addLoading:!1,addingTag:!1,newTag:""}},computed:s()({},Object(m.b)(["enums"]),{techStackOptions:function(){return d()(i()(this.enums.TECH_STACK),function(t){return{value:t[0],label:t[1]}})}}),created:function(){var t=this.$route.query.id;void 0!==t&&(this.id=t,this.fetchData())},methods:{fetchData:function(){var t=this;Object(p.h)(this.id).then(function(e){t.addForm=s()({},e)})},onImgAdd:function(t,e){var n=this,o=new FormData;o.append("file",e),f()({url:Object(p.o)(),method:"post",data:o,headers:{"Content-Type":"multipart/form-data"}}).then(function(e){var o="http://121.42.144.73"+e.data.url;n.$refs.md.$img2Url(t,o)})},onAddTag:function(){this.addingTag=!0},onConfirmAddTag:function(){this.addForm.tags.push(this.newTag),this.newTag="",this.addingTag=!1},onCancelAddTag:function(){this.newTag="",this.addingTag=!1},onRemoveTag:function(t){this.addForm.tags.splice(this.addForm.tags.indexOf(t),1)},onSubmit:function(t){var e=this;this.$refs[t].validate(function(t){if(!t)return console.log("error submit!!"),!1;e.addLoading=!0;var n=a()({},e.addForm);void 0===n.id?Object(p.a)(n).then(function(t){e.addLoading=!1,e.$message({message:"保存成功",type:"success"}),e.id=t.id,e.fetchData(),e.$router.push({path:"/doc/create",query:{id:t.id}})}):Object(p.n)(n).then(function(t){e.addLoading=!1,e.$message({message:"保存成功",type:"success"}),e.fetchData()})})}}},v=(n("UZfA"),n("KHd+")),b=Object(v.a)(g,function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("section",[n("div",{staticClass:"app-container create-doc"},[n("el-form",{ref:"form",attrs:{model:t.addForm,"label-position":"top","label-width":"80px"},nativeOn:{keyup:function(e){return("button"in e||83===e.keyCode)&&e.ctrlKey?(e.stopPropagation(),e.preventDefault(),void t.onSubmit("form")):null}}},[n("el-form-item",{attrs:{rules:[{required:!0,message:"标题不能为空"}],label:"文档标题",prop:"title"}},[n("el-input",{model:{value:t.addForm.title,callback:function(e){t.$set(t.addForm,"title",e)},expression:"addForm.title"}})],1),t._v(" "),n("el-form-item",{attrs:{rules:[{required:!0,message:"内容不能为空"}],label:"",prop:"content"}},[n("mavon-editor",{ref:"md",attrs:{"font-size":"14px"},on:{imgAdd:t.onImgAdd},model:{value:t.addForm.content,callback:function(e){t.$set(t.addForm,"content",e)},expression:"addForm.content"}})],1),t._v(" "),n("el-form-item",{attrs:{label:""}},[n("el-select",{attrs:{clearable:"",size:"small",placeholder:"请选择技术栈"},model:{value:t.addForm.tech_stack,callback:function(e){t.$set(t.addForm,"tech_stack",e)},expression:"addForm.tech_stack"}},t._l(t.techStackOptions,function(t){return n("el-option",{key:t.value,attrs:{label:t.label,value:t.value}})})),t._v(" "),t._l(t.addForm.tags,function(e){return n("el-tag",{key:e,staticStyle:{"margin-right":"5px"},attrs:{"disable-transitions":!0,closable:""},on:{close:function(n){t.onRemoveTag(e)}}},[t._v(t._s(e))])}),t._v(" "),n("el-input",{directives:[{name:"show",rawName:"v-show",value:t.addingTag,expression:"addingTag"}],staticStyle:{width:"120px"},attrs:{placeholder:"添加标签",clearable:"",size:"small"},model:{value:t.newTag,callback:function(e){t.newTag=e},expression:"newTag"}}),t._v(" "),n("el-button",{directives:[{name:"show",rawName:"v-show",value:!t.addingTag,expression:"!addingTag"}],attrs:{type:"primary",icon:"el-icon-plus",size:"mini",title:"添加标签",circle:""},nativeOn:{click:function(e){t.onAddTag()}}}),t._v(" "),n("el-button",{directives:[{name:"show",rawName:"v-show",value:t.addingTag,expression:"addingTag"}],attrs:{type:"success",icon:"el-icon-check",size:"mini",title:"确定",circle:""},nativeOn:{click:function(e){t.onConfirmAddTag()}}}),t._v(" "),n("el-button",{directives:[{name:"show",rawName:"v-show",value:t.addingTag,expression:"addingTag"}],attrs:{type:"danger",icon:"el-icon-close",size:"mini",title:"取消",circle:""},nativeOn:{click:function(e){t.onCancelAddTag()}}})],2),t._v(" "),n("el-form-item",[n("el-button",{attrs:{type:"primary"},nativeOn:{click:function(e){t.onSubmit("form")}}},[t._v("保存")])],1)],1)],1)])},[],!1,null,"5bbc5aa3",null);b.options.__file="create.vue";e.default=b.exports},tgZa:function(t,e,n){n("nGDx"),t.exports=n("WEpk").Object.entries}}]);