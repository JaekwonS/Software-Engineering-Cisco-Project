import re
import yaml
import time
import paramiko
from click._compat import raw_input


def accesslist_config_test(params):
    '''
    This test is to determine if tcp and ip configuration changes are correct

    '''

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(params["ssh"]["IP"], port=22, username=params["ssh"]["Username"],
                password=params["ssh"]["Password"], allow_agent=False, look_for_keys=False,
                auth_timeout=30, passphrase=None)
    #input command ourselves or checking the

    while True:
        cmd = raw_input("Command to run: ")
        cmd_list = cmd.split()
        cmd_list = [str(a) for a in cmd_list]
        if cmd == "":
            print("Enter a valid command")
        if cmd_list[0] == "access-list" and cmd_list[3] == "tcp":
                if cmd_list[1].isdigit():
                    
        if cmd_list[0] == "access-list" and cmd_list[3] == "ip":
