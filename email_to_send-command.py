import time
import win32com.client
from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty
pretty.install()


def send_hostname():
    client = SSHClient()
    # Known_host policy
    client.set_missing_host_key_policy(AutoAddPolicy())
    # client.connect('10.1.1.92', username='root', password='password1')
    client.connect('ubuntu-vm', port=22, username='ubaid', password='test.123')
    # client.exec_command('hostname')
    # execute the commands
    stdin, stdout, stderr = client.exec_command('hostname')
    print(stdout.read().decode())
    err = stderr.read().decode()

def send_ls():
    client = SSHClient()
    # Known_host policy
    client.set_missing_host_key_policy(AutoAddPolicy())
    # client.connect('10.1.1.92', username='root', password='password1')
    client.connect('ubuntu-vm', port=22, username='ubaid', password='test.123')
    # client.exec_command('hostname')
    # execute the commands
    stdin, stdout, stderr = client.exec_command('ls')
    print(stdout.read().decode())
    err = stderr.read().decode()

# For reading email subject code
# outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
# # For Subfolders
# inbox = outlook.GetDefaultFolder(6).Folders["JAZZ Cloud"]

# For Inbox
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items
# message = messages.GetLast()
# print(message.subject)


PC1 = "muhammad.ubaid@falconitracking.com"
PC2 = "ls"
# Loop to pick messages that are unread
for x in messages:
        message = messages.GetLast()

        #Loop to check if the any new email arrives
        if (message.Unread == True): # and (message.Sender.GetExchangeUser().PrimarySmtpAddress == PC1):
            print("New Mail Found")
            print("Message from", message.Sender.GetExchangeUser().PrimarySmtpAddress)
            print("Subject", message.subject)
            send_hostname()
            message.Unread = False
            time.sleep(1)

        elif (message.Unread == True) and (message.subject == PC2):
            print("New Mail Found")
            print("Message from", message.Sender.GetExchangeUser().PrimarySmtpAddress)
            print("Subject", message.subject)
            print(message.subject)
            send_ls()
            message.Unread = False
            time.sleep(1)

        else:
            time.sleep(1)
            print ("Checking...")