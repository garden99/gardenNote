1. **查看本地镜像列表**：
   
   > docker images

2. **删除镜像**：
   
   > docker rmi <image-id> | \<image-name>[:tag]

3. **构建镜像**：
   
   > docker build -t \<image-name>[:tag] [-f \<Dockerfile-path>] .

4. **导出镜像为tar文件**：
   
   > docker save -o \<filename.tar> <image-name>[:tag]

5. **导入tar文件为镜像**：
   
   > docker load -i <filename.tar>

6. **查看容器列表**：
   
   > docker ps [-a]

7. **启动容器**：

```
> docker run
  > --name container_name \          # 容器的名字
  > -d \                             # 在后台运行容器
  > -p host_port:container_port \    # 端口映射，将主机端口映射到容器端口
  > --env VAR_NAME=value \           # 设置环境变量
  > --mount type=bind,src=host_dir,dst=container_dir \ # 数据卷挂载
  > --volume host_dir:/container_dir \ # 另一种形式的数据卷挂载
  > --network network_name \          # 指定容器连接到哪个网络
  > -it \                            # 如果需要交互式终端，则使用此选项
  > --rm \                           # 运行完成后自动清理容器
  > image_name \                     # 需要运行的镜像名称
  > command                          # 在容器内运行的命令
```

10. **进入容器终端**：
    
    > docker exec -it bash

11. **停止容器**：
    
    docker stop \<container-id>

12. **删除容器**：
    
    > docker rm /<container-id>

13. **查看容器日志**：
    
    > docker logs /<container-id>

14. **创建自定义网络**：
    
    > docker network create --driver \<network-driver> [--subnet \<subnet>] [--gateway \<gateway>] \<network-name>

15. **连接容器到网络**：
    
    > docker network connect \<network-name> \<container-id>

16. **断开容器与网络的连接**：
    
    > docker network disconnect \<network-name> \<container-id>

17. **删除网络**：
    
    > docker network rm \<network-name>

18. **查看网络列表**：

> docker network ls

19. **查看网络详情**：
    
    > docker network inspect \<network-name>

### 配置选项：

#### 1. Dockerfile 配置选项：

* `FROM <base-image>`：指定基础镜像。
* `LABEL <key>=<value>`：为镜像添加元数据标签。
* `MAINTAINER <name>`：指定镜像维护者信息。
* `RUN <command>`：运行命令。
* `CMD <command>`：容器启动时默认执行的命令。
* `ENTRYPOINT <command>`：定义容器启动时的入口点。
* `ENV <key>=<value>`：设置环境变量。
* `EXPOSE <port>`：声明容器中服务监听的端口。
* `ADD <src>... <dest>`：从本地添加文件、目录或远程URL到镜像中。
* `COPY <src>... <dest>`：从本地复制文件或目录到镜像中。
* `VOLUME <path>`：创建数据卷挂载点。

#### 2. Docker 命令行配置选项：

* `-d`：在后台运行容器。
* `-i`：保持STDIN打开。
* `-t`：分配一个TTY。
* `-p <host-port>:<container-port>`：端口映射。
* `--name <container-name>`：指定容器的名称。
* `--network <network-name>`：指定容器连接的网络。
* `--ip <ip-address>`：指定容器在网络中的IP地址。
* `-v <host-dir>:<container-dir>`：挂载宿主机目录到容器。
* `--mount type=volume,src=<volume-name>,dst=<container-dir>`：挂载匿名数据卷。
* `--restart <policy>`：设置容器的重启策略。
* `--env <key>=<value>`：设置环境变量。
* `--label <key>=<value>`：设置标签。
