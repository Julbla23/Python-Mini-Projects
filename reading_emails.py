from imap_tools import MailBox

SERVER = "imap.wp.pl"
MAIL_PASSWORD = ""
MAIL_USERNAME = "@wp.pl"

with MailBox("imap.wp.pl").login(MAIL_USERNAME, MAIL_PASSWORD, "INBOX") as mb:
    #print(mb.folder.list())
    #print(mb.folder.get())
    for msg in mb.fetch(limit=5, reverse=True, mark_seen=False):
        print(msg.subject, msg.date, msg.flags, msg.text, msg.uid)

    mb.move("6652", "Trash")
