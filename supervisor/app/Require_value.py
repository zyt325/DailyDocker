# -*- encoding:utf-8 -*-

def Credentials(class_type='type', class_host='host', class_key='key'):
    credentials = {}
    # class_type: class_host: class_key: class_value:;
    credentials.setdefault('DB_z', {}).setdefault('test', {}).update(
        {'host': '127.0.0.1', 'user': 'zyt', 'passwd': '325', 'dbase': 'mysql', 'port': '3306'})
    credentials.setdefault('DB_z', {}).setdefault('db', {}).update(
        {'host': 'db.base-fx.com', 'user': 'root', 'passwd': 'basefx12', 'dbase': 'mysql', 'port': '3306'})
    credentials.setdefault('DB_z', {}).setdefault('db08', {}).update(
        {'host': 'db08.base-fx.com', 'user': 'root', 'passwd': 'basefx12', 'dbase': 'mysql', 'port': '3306'})
    credentials.setdefault('DB_z', {}).setdefault('all', {}).update(
        {'host': '', 'user': 'root', 'passwd': 'basefx12', 'dbase': 'mysql', 'port': '3306'})
    credentials.setdefault('DB_z', {}).setdefault('test', {}).update(
        {'host': '127.0.0.1', 'user': 'zyt', 'passwd': '325', 'dbase': 'mysql', 'port': '3306'})
    credentials.setdefault('DB_z', {}).setdefault('vps', {}).update(
        {'host': 'note.personer.tech', 'user': 'zyt', 'passwd': '325', 'dbase': 'mysql', 'port': '3306'})
    credentials.setdefault('DB_z', {}).setdefault('localhost', {}).update(
        {'host': 'localhost', 'user': 'root', 'passwd': '', 'dbase': 'mysql', 'port': '3306'})
    credentials.setdefault('DB_z', {}).setdefault('docker03', {}).update(
        {'host': 'docker03.base-fx.com', 'user': 'root', 'passwd': 'mysql325', 'dbase': 'mysql', 'port': '3306'})
    credentials.setdefault('PostgreSQL', {}).setdefault('sg-db01', {}).update(
        {'host': 'sg-db01.base-fx.com', 'user': 'com_base_fx_shotgun_prod', 'passwd': 'CHYlYIAWphYkjKl76Pj0',
         'dbase': 'com_base_fx_shotgun_prod', 'port': '5432'})
    credentials.setdefault('LDAP_z', {}).setdefault('test', {}).update(
        {'host': '10.14.6.170', 'user': 'cn=zyt_ad,ou=Basers,dc=ad,dc=bfx,dc=com', 'passwd': 'zyt_ad#325',
         'root_dn': 'ou=Basers,dc=ad,dc=bfx,dc=com'})
    credentials.setdefault('LDAP_z', {}).setdefault('dc09', {}).update(
        {'host': 'dc09.base-fx.com', 'user': 'cn=zhangyt,ou=NON,ou=BJ,ou=Basers,dc=ad,dc=base-fx,dc=com',
         'passwd': 'b!onpJ32',
         'root_dn': 'ou=Basers,dc=ad,dc=base-fx,dc=com'})
    credentials.setdefault('SSH_z', {}).setdefault('vps', {}).update(
        {'host': 'personer.tech', 'user': 'root', 'passwd': 'zyt#vps325'})
    credentials.setdefault('WIN_z', {}).setdefault('test', {}).update(
        {'host': '10.14.6.194', 'user': 'administrator', 'passwd': 'Base.f17d'})
    credentials.setdefault('WIN_z', {}).setdefault('all', {}).update(
        {'host': '', 'user': 'administrator', 'passwd': 'Base.f17d'})
    if credentials[class_type].get(class_host):
        return credentials[class_type][class_host][class_key]
    elif class_key == 'host':
        return class_host
    else:
        return credentials[class_type]['all'][class_key]
