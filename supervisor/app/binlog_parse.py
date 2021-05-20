import sys
import datetime

from DB_z import DB
from COMMON_z import Common
from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent,
)
from pymysqlreplication.event import RotateEvent


def binlog_dump():
    mysql_settings = {'host': 'docker03.base-fx.com', 'port': 3306, 'user': 'root', 'passwd': 'mysql325'}
    stream = BinLogStreamReader(connection_settings=mysql_settings, server_id=100, blocking=True)
    for binlogevent in stream:
        binlogevent.dump()

    # stream.close()


def get_binlog_info():
    con, cur = DB().connect('dmz-lockedweb01.base-fx.com', user='root', passwd='basefx12', port=3307)
    cur.execute('show master status;')
    return cur.fetchone()


def binlog_parsing():
    binlog_status_info = get_binlog_info()
    mysql_settings = {'host': 'dmz-lockedweb01.base-fx.com', 'port': 3307, 'user': 'root', 'passwd': 'basefx12'}
    # mysql_settings = {'host': 'docker03.base-fx.com', 'port': 3306, 'user': 'root', 'passwd': 'mysql325'}
    stream = BinLogStreamReader(connection_settings=mysql_settings, server_id=1001, blocking=True,
                                # log_file=binlog_status_info['File'], log_pos=binlog_status_info['Position'],
                                resume_stream=True
                                # ,only_events=[DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent]
                                )

    for binlogevent in stream:
        ff = open("binlog-%s" % datetime.date.today(), 'a+')
        sys.stdout = ff
        binlogevent.dump()
        action = binlogevent.__class__.__name__
        if action in ['WriteRowsEvent', 'DeleteRowsEvent', 'UpdateRowsEvent']:
            f = open("binlog-rows-%s" % datetime.date.today(), 'a+')
            content = {}
            content['action'] = binlogevent.__class__.__name__
            content['database'] = binlogevent.schema
            content['table'] = binlogevent.table
            content['rows'] = binlogevent.rows
            content['rows_line'] = len(binlogevent.rows)
            content['log_pos'] = binlogevent.packet.log_pos
            f.writelines(str(content) + "\n")
            f.close()
            table_content = """<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>""" % tuple(content.values())
            mail_template = """Hi ALL:<br>
            <div style="margin-left:20px;text-align:left">以下是HRDB数据库更新<br>User account has been created for the following newcomer, please contact ITD if you have any question, thank you!</div>
            <table border="1px" style="margin-left:20px;border:1px solid #000000;border-spacing:0;border-collapse:collapse">
                <tr bgcolor="#6495ed" style="color: #FFFFFF">
                    <th>Action</th>
                    <th>Database</th>
                    <th>Table</th>
                    <th>Rows</th>
                    <th>Rows_line</th>
                    <th>log_pos</th>
                </tr>
                %s
            </table>"""
            mail_content = mail_template % table_content

            Common().email('itd_mail@base-fx.com', 'itdbj@base-fx.com', 'HRDB更新', mail_content,
                           server="smtp.base-fx.com",
                           passwd="Eo8yGcdjy", mimetext='html')

    # stream.close()


if __name__ == "__main__":
    binlog_parsing()
