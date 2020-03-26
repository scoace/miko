import paramiko
from scp import SCPClient, SCPException
import time
import logging
import credendials


logging.basicConfig(level=logging.ERROR )
logger = logging.getLogger('global')

class SSH:
    def __init__(self, ipaddr, username, password, port="22"):
        self.ipaddr = ipaddr
        self.username = username
        self.password = password
        self.port = port
        if not paramiko:
                raise ImportError (name='Error importing paramiko.')
        
        
    #def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.ipaddr,port=self.port,username=self.username,password=self.password) 
        
        
    def disconnect(self):
            
            return(self.ssh.close())
        
    def send_command(self,command):

            stdin, stdout, stderr=self.ssh.exec_command(command)
            return(stdout.readlines())

    def copy_file(self,remote,local):
        self.scp = SCPClient(self.ssh.get_transport())
        self.scp.get(remote, local)
timestr = time.strftime("%Y%m%d")
myfgt=SSH(ipaddr=credendials.fgt,
            username=credendials.un,
            password=credendials.pw)
mylinux=SSH(ipaddr="192.168.173.70",username="andy",password=credendials.pw)
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