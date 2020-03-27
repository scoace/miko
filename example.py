import paramiko
from scp import SCPClient, SCPException
import time
import logging
import credendials
import miko

timestr = time.strftime("%Y%m%d")
myfgt=miko.SSH(ipaddr=credendials.fgt,
            username=credendials.un,
            password=credendials.pw)
mylinux=miko.SSH(ipaddr="192.168.173.70",username="andy",password=credendials.pw)
mylist=myfgt.send_command("config system global\rset admin-scp enable\rend")
for lines in mylist:
    print (lines.strip())
#     scp admin@<FortiGate_IP>:sys_config <location>

mylist=myfgt.copy_file('sys_config','y:/fortinet/Bachup_fgt_'+timestr+'.conf')
mylist=mylinux.send_command("hostname")
for lines in mylist:
    print (lines.strip())
myfgt.disconnect()
mylinux.disconnect()