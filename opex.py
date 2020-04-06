from datetime import datetime, timedelta
import pytz
from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, ServiceAccount, \
    EWSDateTime, EWSTimeZone, Configuration, NTLM, CalendarItem, Message, \
    Mailbox, Attendee, Q, ExtendedProperty, FileAttachment, ItemAttachment, \
    HTMLBody, Build, Version#, FolderCollection

credentials = Credentials('jake.jian.wang@accenture.com', 'Wkhacn0203$')
config = Configuration(server='mail.accenture.com', credentials=credentials)
#account = Account('jake.jian.wang@accenture.com', credentials=credentials, autodiscover=True)
account = Account(primary_smtp_address='jake.jian.wang@accenture.com', config=config, autodiscover=False, access_type=IMPERSONATION)

for item in account.inbox.all().order_by('-datetime_received')[:3]:
    print(item.subject, item.sender, item.datetime_received)
