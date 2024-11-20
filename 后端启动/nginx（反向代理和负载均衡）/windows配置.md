1. 在官方下载windows的压缩包，在方便的地方解压
2. 双击应用程序运行，或者进入该文件下输入start nginx.exe运行

   ## 注意，在启动之后没有停止继续使用启动命令或者双击进行这回导致一些莫名问题

   ## 常用命令

   1、启动：

> start nginx.exe
> 或
> nginx.exe

注：建议使用第一种，第二种会使你的cmd窗口一直处于执行中，不能进行其他命令操作。

如果需要特殊设置nginx的配置文件路径，可以这样执行start nginx -c conf/nginx.conf

2、停止：

> nginx.exe -s stop

> 或

> nginx.exe -s quit

注：stop是快速停止nginx，可能并不保存相关信息；quit是完整有序的停止nginx，并保存相关信息。

执行 nginx.exe -s stop或者quit命令是不是不能删除进程？查看进程开了一堆nignx.exe
还有80端口在Listening，并且浏览器F5刷新还能访问页面，可能nginx.exe版本或系统的原因，用
taskkill /f /im nginx.exe > null 杀死nginx进程

3、重新载入Nginx：

> nginx.exe -s reload

当配置信息修改，需要重新载入这些配置时使用此命令。

4、重新打开日志文件：

> nginx.exe -s reopen

5, 检查是否有运行：

> tasklist | findstr nginx

## API

[Windows下Nginx的启动、停止等命令 - 乡秀树i - 博客园 (cnblogs.com)](https://www.cnblogs.com/xiangxiushu/p/15523063.html#:~:text=Windows%E4%B8%8BNg)
