import smtplib
import os
import datetime


class MailHandler:

    conf = {
        'host': "smtp.gmail.com",
        'port': 465,
        'tls': True,
        'username': "powiadomieniapepper@gmail.com",
        'password': "!zxc23@4R",
        'sender': "tomekholda@gmail.com",
    }

    @staticmethod
    def send_mail(products, email):

        if not products:
            return

        headers = {
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-Disposition': 'inline',
            'Content-Transfer-Encoding': '8bit',
            'From': MailHandler.conf['sender'],
            'To': email,
            'Date': datetime.datetime.now().strftime('%a, %d %b %Y  %H:%M:%S %Z'),
            'X-Mailer': 'python',
            'Subject': 'Nowe aukcje z produktami których szukasz'
        }

        msg = '\n'.join(map(': '.join, headers.items())) + '\n'

        for product in products:
            msg += "%s - CENA: %s\r\n%s\r\n\r\n" % (product.get_name(), product.get_price(), product.get_url())

        s = smtplib.SMTP_SSL(MailHandler.conf['host'], MailHandler.conf['port'])
        s.ehlo()
        s.login(MailHandler.conf['username'], MailHandler.conf['password'])
        s.sendmail(headers['From'], email, msg.encode("utf8"))
        s.quit()
