# Linux 命令
创建文件软链接   
`ln -s /source linkname`   
在用户目录下创建可执行文件的链接   
`ln -s /source ./linkname`   
执行命令 `./linkname`   

修改 文件/文件夹 权限   
`chomd *** filename`   

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
