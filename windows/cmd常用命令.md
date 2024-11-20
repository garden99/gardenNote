## 查看当前登录的用户

> whoami

## 查看当前用户属于的组

> whoami /groups

在Windows中，可以使用`netstat`命令来查看端口占用情况。以下是具体的命令：

> netstat -ano -b | findstr :8080

这里的`<port>`是你想要查询的端口号。例如，要查看8080端口是否被占用，可以执行：

> netstat -ano | findstr

这条命令会列出所有监听8080端口的进程。

#### 获取进程ID

如果你需要知道占用端口的进程ID（PID），可以在命令中加上`-b`选项来显示程序的路径：

> netstat -ano -b | findstr :8080

#### 关闭端口占用的进程

知道了PID后，可以使用`taskkill`命令来结束占用端口的进程：

> taskkill /F /PID 

这里的`<PID>`是你从`netstat`命令中得到的进程ID。例如：

> taskkill /F /PID 12345

