FROM harbor.base-fx.com/itd/centos:7.2.1511

RUN yum -y install samba samba-common iproute
RUN groupadd -g 3000 cgi
RUN useradd -u 4011 -g 3000 base
RUN echo 'base' | passwd --stdin base
RUN (echo base;echo base) | pdbedit -a -u base -t
EXPOSE 139 445 137/udp 138/udp
ENTRYPOINT [ "bash","-c","/usr/sbin/smbd --no-process-group && /usr/sbin/nmbd  --no-process-group && /bin/bash" ]
