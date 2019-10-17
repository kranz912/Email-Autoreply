import json
from emailclient import IMAP_Client
with open('config.json') as jsonconfig:
    config = json.load(jsonconfig)

__EMAIL = config['email']
__PASSWORD = config['password']
__HOST = config['host']
__PORT = config['port']
__REPLY = config['reply']

imap_client = IMAP_Client(
                host= __HOST,
                port= __PORT,
                email= __EMAIL,
                password= __PASSWORD
                )
imap_client.selectmailbox('INBOX',False)
imap_client.readEmails()