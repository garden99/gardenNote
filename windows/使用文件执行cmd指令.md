### 下面命令的作用是运行 cmd ipconfig然后不关闭窗口

```cmd
@echo off
ipconfig
pause
```

### @echo off

关闭命令回显（就是命令回车的输出信息关闭）

### @echo off

打开回显

### @echo <输出的打印信息>

输出信息（就和打印一样）

### pause

这个很重要，这个可以让窗口处于等待用户执行操作的状态，也就是不会关闭窗口
