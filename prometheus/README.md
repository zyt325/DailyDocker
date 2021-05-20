1、拷贝文件夹zabbix到目标主机的/docker下
2、sh init.sh  创建需要的文件夹
3、启动mariadb容器   docker-compose -f mariadb.yml up -d
4、修改mariadb数据库，创建用户,数据库(会自行创建)
5、启动zabbix容器   docker-compose -f zabbix.yml up -d


解决中文界面，图形中文乱码问题
```
docker cp ./simkai.ttf zabbix-web:/usr/share/zabbix/assets/fonts/
docker cp zabbix-web:/usr/share/zabbix/include/defines.inc.php ./
sed -n '/DejaVuSans/p' defines.inc.php
sed -i 's/DejaVuSans/simkai/g' defines.inc.php
sed -n '/simkai/p' defines.inc.php
docker cp defines.inc.php zabbix-web:/usr/share/zabbix/include/defines.inc.php
```