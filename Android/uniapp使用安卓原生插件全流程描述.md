## 背景

- 具备安卓uniplugin-music插件项目

- plug uniapp调用项目文件

- 依赖版本项目系统自带

# 开始

新建uniapp项目

创建原生插件目录

![](E:\desktop\文件\Markdown\Android\images\Snipaste_2024-12-26_10-54-50.png)

在项目中配置插件

# 2，进入uniapp后台

进入uniapp后台，创建离线打包key(这个是测试版本使用，后面得换的)，android 云端证书

# 3，进入hbuilder

进入hbuilder进行项目的本地打包，

# 4，进入Android studio

进入Android studio，打开项目进行配置修改

主要是以下几个文件，app模块的build.gradle，AndroidManifest.xml，dcloud_control.xml，增加一个证书文件，

# 5，运行

运行不成功是配置问题，可以查看上述Androidstudio原生开发配置。

运行的是uniapp之前本地打包的代码，那边的插件和这边安卓项目的是对应的就可以

# 6，打包插件arr包

# 7，替换之前插件结构里面的arr插件包

# 8，uniapp打自定义基座包，使用uniapp后台的证书

# 9，运行


