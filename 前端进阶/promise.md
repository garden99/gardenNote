# 路漫漫其修远兮，吾将上下而求索

## promise

### 遇到的坑

不要讲promise成功的resolve与return返回方法归为一谈，resolve后面的语句还会被执行，多个resolve时，遇到第一个resolve即为成功，且接受第一个的值为返回
