# 并没有你想象的难。转换一下概念一下就立即了服务器和本地的关系（和你部署在网上的虚拟机一样的）

> 注释：服务器就是一个直接暴露在公网内的电脑，所以你的程序在该电脑上面运行可以被大家都进行检索。就这么简单

## 第一步，

拿到服务器的公网ip,电脑的账号密码（你可以立即为win的开机账号和密码）——直接重置会比较快

## 第二步，

下载远程链接工具进行服务器的连接。这里使用的是Xshell 6 软件，步骤是点击新建会话，然后填入主机地址和端口号（默认22），完成后在连接的时候会让你输入账户和密码。（就和电脑开机一样）

## 第三步，

在你新开的公网电脑（云服务器）上面安装你需要的东西，比如项目运行环境，项目运行的库，数据库。——操作流程就和你在自己的本地电脑上面安装这些东西是一样的

注释：对于传输文件可以使用FileZilla进行文件传输

## 第四步，

创建mysql数据库,这个网上很多教程以下是邓工给的参考

> ## ubuntu安装mysql
> 
> cd /data
> sudo apt install mysql-server
> sudo mysql
> use mysql
> 
> ### 1.修改密码：
> 
> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password by 'pickup1688';
> 
> ### 2: 将root用户改为可在任何host访问
> 
> update user set host = '%' where user ='root';
> flush privileges;
> 
> ### 3：查看当前的root连接host
> 
> select User,Host from user;
> exit
> 
> ### 修改配置文件：
> 
> vi  /etc/mysql/mysql.conf.d/mysqld.cnf
> 
> Port=16806
> Bind-address=0.0.0.0
> Mysqlx- bind-address=0.0.0.0
> 
> ## 缓冲区大小
> 
> key_buffer_size = 256m
> 
> ## 设置binlog清理时间,只保留30天的日志
> 
> expire_logs_days = 30
> 
> ## binlog每个日志文件大小
> 
> max_binlog_size = 100m
> 
> ## binlog缓存大小
> 
> binlog_cache_size = 4m
> 
> ## 最大binlog缓存大小
> 
> max_binlog_cache_size = 512m
> 
> ### #启动mysql服务
> 
> sudo service mysql start
> safe_mysql&
> 
> ### #停止mysql服务
> 
> sudo service mysql stop

## 第五步

连接到数据库，idea,vscode,Navicat Premium 15都可以，各有优劣。过程很简单
