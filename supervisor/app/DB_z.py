import Require_value

class_type = 'DB_z'
default_value = Require_value.Credentials


class DB:
    def __init__(self):
        self.con = None
        self.cur = None
        import pymysql
        self.mysql = pymysql

    def connect(self, host='127.0.0.1', user='', passwd='', port=3306):
        import pymysql.cursors
        if not user and not passwd:
            user, passwd = default_value(class_type, host)
        con = self.mysql.connect(host, user, passwd, charset='utf8', cursorclass=pymysql.cursors.DictCursor,
                                 connect_timeout=30, use_unicode=True, port=port)
        cur = con.cursor()
        return con, cur


    def closed(self):
        '''close connect'''
        self.con.close()
