# Linux 命令
root 密码   
`sudo passwd`   

### 解决在执行 sudo 命令时慢的问题：

查看本机name   
`hostname`   
打开 hosts 文件，检查本机 name 是否在   
`sudo vim /etc/hosts`   
`127.0.0.1       localhost your_hosts_name`   
这一行中，如果没有，添加进去，搞定。   

### ln
创建文件软链接   
`ln -s /source linkname`   
在用户目录下创建可执行文件的链接   
`ln -s /source ./linkname`   
执行命令 `./linkname`   

### 权限
修改 文件/文件夹 权限   
`chomd *** filename`   

### gcc

编译多个 c/c++ 源文件，链接成 test 可执行文件   
`g++/gcc test.cpp fun.cpp -o test`

### 解压缩
tar.xz		tar xvJf ***.tar.xz

### 查找

查找并列出当前目录下所有含有 "IBM" 的文件   
`find .|xargs grep -ri "IBM" -l`   

# mysql 命令
进入mysql   
`mysql -u root -p`   

创建数据库   
`create datebase dbname;`   

创建数据库 并 指定默认编码 utf-8   
`CREATE DATABASE dbname DEFAULT CHARSET utf8 COLLATE utf8_general_ci;`   

链接数据库   
`use dbname;`

列出所有数据库，列出当下数据库的表   
`show databases;`   
`show tables;`   

删除数据库   
`drop database dbname;`   

导出数据库   
`mysqldump -u root -p dbname > qiyuanhualang.sql;`    

# java 

### Linux 下 编译运行 带有 jar 包 的 java 程序   

`javac -cp commons-codec-1.9.jar BaiduTranslate.java`   
`java -cp commons-codec-1.9.jar:. BaiduTranslat`   

### 数据类型转换   

String to int :   
int i = Integer.parseInt(str);   
char to int :   
int i = Integer.parseInt(char + "");   
String to Float :   
Float f = Float.parseFloat(str);   
int to String :   
String str = Integer.toString(int);   

# git

`git remote -v`
`git remote rm *`

* `git remote add origin git@github.com:username/repo.git`
* `git remote add origin https://github.com/username/repo.git`
