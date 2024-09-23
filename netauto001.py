import smtplib
from netmiko import ConnectHandler

def send_email_alert(interface):
    sender = 'vincent@nextech.com'
    receivers = ['admin@nextech.com']
    message = f"Subject: Interface {interface} Down\n\nInterface {interface} is currently down."

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
        print("Successfully sent email")
    except Exception as e:
        print(f"Error: unable to send email: {e}")

switch = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.2',
    'username': 'admin',
    'password': 'admin@nextech123'
}

net_connect = ConnectHandler(**switch)
output = net_connect.send_command('do sh ip int br')

if 'down' in output:
    send_email_alert("GigabitEthernet0/1")

