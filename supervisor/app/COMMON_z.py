import os


class Common():
    '''class tools'''

    def __init__(self, debug=False):
        self._debug = debug

    def email(self, from_address, to_addresses, subject, body, server='localhost', mimetext='plain',
              passwd=None, cc_addresses=None, attachments=None):
        if type(to_addresses) != list:
            to_addresses = [to_addresses]
        import smtplib
        import mimetypes
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email import encoders

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = from_address
        msg['To'] = ','.join(to_addresses)
        msg['Accept-Language'] = "zh-CN"
        msg['Accept-Charset'] = "ISO-8859-1,utf-8"
        msg.attach(MIMEText(body, mimetext, 'utf-8'))
        if cc_addresses:
            if type(cc_addresses) != list:
                cc_addresses = [cc_addresses]
            msg['Cc'] = ','.join(cc_addresses)
            to_addresses += cc_addresses
        if attachments:
            if type(attachments) != list:
                attachments = [attachments]
            for f in attachments:
                try:
                    ctype = mimetypes.guess_type(f)[0].split('/')[1]
                except:
                    ctype = 'octet-stream'
                with open(f, 'rb') as fp:
                    record = MIMEBase('application', ctype)
                    record.set_payload(fp.read())
                    encoders.encode_base64(record)
                    record.add_header('Content-Disposition',
                                      'attachment', filename=os.path.basename(f))
                msg.attach(record)
        s = smtplib.SMTP(server)
        if passwd:
            s.login(from_address, passwd)
        s.sendmail(from_address, to_addresses, msg.as_string())
        s.quit()
