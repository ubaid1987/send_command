from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty
pretty.install()

# Command Definition
hostname = "ansible --version"
ping = "ping ubuntu-vm"

# Send Command function
def send_command(command):
    client: SSHClient = SSHClient()
    # Known_host policy
    client.set_missing_host_key_policy(AutoAddPolicy())
    # client.connect('10.1.1.92', username='root', password='password1')
    client.connect('ubuntu-vm', port=22, username='ubaid', password='test.123')

    # execute the commands
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    err = stderr.read().decode()

send_command(ping)
send_command(hostname)
send_command(hostname)