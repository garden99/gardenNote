# 使用官方的 Node.js 镜像作为基础镜像
FROM node:20.12.0-alpine

# 设置工作目录
WORKDIR /usr/src/app

# 暴露应用程序端口
EXPOSE 3090

# 复制 package.json 和 package-lock.json 到工作目录
COPY package*.json ./

# 安装依赖
RUN npm install


# 复制应用程序源代码到工作目录
COPY . .

# 设置启动命令
CMD ["node", "./bin/www"]