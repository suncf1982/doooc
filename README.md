## 项目安装

### 项目介绍
&emsp;&emsp;该项目旨在帮助用户高效的管理自己的各种文档和随想。归档、标签、搜索等功能使文档管理更加方便。使用markdown语法进行写作，可转换成html格式、pdf格式、word格式和ppt格式。
&emsp;&emsp;可作为个人、团队或公司的项目文档管理使用
&emsp;&emsp;项目时基于django、vue2等开源框架开发，涉及比较多的技术，可以作为个人学习之参考。

### 软件架构
&emsp;&emsp;项目使用Django作为基础开发框架；前端采用Vue2+Element UI
；数据库支持mysql、sqlite等常用的关系型数据库；使用pandoc进行pdf，word，ppt等格式的转换。


### 安装教程-准备环境
1. pyhton3.5+, pip
2. pandoc [参考](http://pandoc.org/installing.html)
3. LaTeX（生成pdf使用） [windows参考MiKTeX](https://miktex.org/download#unx)、 [linux参考TeX Live](http://www.tug.org/texlive/)

### 安装教程-部署安装
1. 下载工程代码：git clone https://gitee.com/suncf1982/doooc.git
2. 进入工程并安装依赖项目依赖.
cd doooc && pip install -r requirements.txt
3. 数据库初始化：python manager migrate
4. 运行： python manager runserver
5. nginx部署，请参考项目中site-nginx.conf

### 使用说明

1. 用户一块直接使用django admin进行管理
2. 权限一块暂时使用group进行简单控制，公开文档可供所有用户搜索查阅
3. 支持归档、标签、收藏、分享等精细化管理功能
4. 文档支持markdown语法。另外支持模板功能，如使用手册模板、读数笔记模板等，方便快速笔记。

### 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


### 附录参考

1. [pandoc markdown 生成pdf文档](http://yijiebuyi.com/blog/17e31502e8a6229a18971a2499f0e72b.html)
2. [A little trick with tlmgr: Unknown directive …containerchecksum error](https://darrengoossens.wordpress.com/2016/06/20/a-little-trick-with-tlmgr-unknown-directive-containerchecksum-error/)
3. [pandoc安装](http://pandoc.org/MANUAL.html)