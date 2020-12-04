import win32com.client

subject = 'email subject'
body = '<html><body>' + 'test email.<br />' + '</body></html>'
recipient = 'tayml.at.rp@gmail.com'
#attachments = ["D:\\Dropbox\\Modules\\PythonCET\\Past Runs\\Dec2019\\day2\\05. Email\\abc.txt"]
#attachments = ["C:\\Users\\hazet\\Dropbox\\lan_work\\adjunct_rp\\CET_Python\\TML\\abc.txt"]

#Create and send email
olMailItem = 0x0
obj = win32com.client.Dispatch("Outlook.Application")
newMail = obj.CreateItem(olMailItem)
newMail.Subject = subject
newMail.HTMLBody = body
#newMail.Body = body
newMail.To = recipient

#for location in attachments:
#    newMail.Attachments.Add(Source=location)

#newMail.display()
newMail.Send()
print("Sent")