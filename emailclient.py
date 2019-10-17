import email
import imaplib


class IMAP_Client:

    def __init__(self,host,port,email,password,mailbox='INBOX',readonly=0):
        self.mail =imaplib.IMAP4_SSL()
        self.mail.host = host
        self.mail.port = port
        self.mail.login(email,password)
        self.selectmailbox(mailbox,readonly)

    def selectmailbox(self,mailbox,readonly):
        self.mail.select(mailbox=mailbox,readonly=readonly)

    def readEmails(self,query='(UNSEEN)'):
        (retcode, messages) = self.mail.search(None,query)
        emails = []
        if(retcode == 'OK'):
            for num in messages[0].split():
                typ,data = self.mail.fetch(num, '(RFC822)')
                emails.append(email.message_from_bytes(data[0][1]))
        return emails