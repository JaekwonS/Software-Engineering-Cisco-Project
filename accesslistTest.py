import re
import yaml
import time
import paramiko
from click._compat import raw_input


def accesslist_config_test(params):
    '''
    This test is to determine if tcp and ip configuration commands are correct for access lists

    '''

    csr1000v = paramiko.SSHClient()
    csr1000v.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    csr1000v.connect(params["csr1000v"]["IP"], port=22, username=params["csr1000v"]["Username"],
                     password=params["csr1000v"]["Password"],
                     allow_agent=False, look_for_keys=False, auth_timeout=30, passphrase=None)

    cmd = raw_input("Command to run: ")

    re1='((?:[a-z][a-z]+))'	# Word 1
    re2='(.)'	# Any Single Character 1
    re3='((?:[a-z][a-z]+))'	# Word 2
    re4='(\\s+)'	# White Space 1
    re5='(\\d)'	# Any Single Digit 1
    re6='(\\d)'	# Any Single Digit 2
    re7='(\\d)'	# Any Single Digit 3
    re8='(\\s+)'	# White Space 2
    re9='((?:[a-z][a-z]+))'	# Word 3
    re10='(\\s+)'	# White Space 3
    re11='((?:[a-z][a-z]+))'	# Word 4
    re12='(\\s+)'	# White Space 4
    re13='((?:[a-z][a-z]+))'	# Word 5
    re14='(\\s+)'	# White Space 5
    re15='((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\\d])'	# IPv4 IP Address 1
    re16='(\\s+)'	# White Space 6
    re17='((?:[a-z][a-z]+))'	# Word 6
    re18='(\\s+)'	# White Space 7
    re19='((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\\d])'	# IPv4 IP Address 2
    re20='(\\s+)'	# White Space 8
    re21='((?:[a-z][a-z]+))'	# Word 7
    re22='(\\s+)'	# White Space 9
    re23='(\\d)'	# Any Single Digit 4
    re24='(\\d)'	# Any Single Digit 5

    rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16+re17+re18+re19+re20+re21+re22+re23+re24)

    if not rg.search(cmd): 
        print("Not valid input")

    reg_access = '((?:access-list))'  # access-list
    reg_tcp = '((?:tcp))'  # tcp
    reg_ip = '((?:ip))'  # ip
    reg_eq = '((?:eq))'  # eq - designate port
    reg_white = '(\\s+)'  # White Space 9
    reg_dig = '(\\d)'  # Any Single Digit 4
    reg_dig2 = '(\\d)'  # Any Single Digit 5

    reg = re.compile(reg_access)
    type1 = re.compile(reg_tcp)
    type2 = re.compile(reg_ip)
    ending = re.compile(reg_eq + reg_white + reg_dig + reg_dig2)

    if bool(reg.search(cmd)):
        if bool(type1.search(cmd)):
            if not bool(ending.search(cmd)):
                print('eq port required')
            else:
                stdin, stdout, stderr = csr1000v.exec_command(cmd)
        elif bool(type2.search(cmd)):
            if bool(ending.search(cmd)):
                print('eq port not needed')
            else:
                stdin, stdout, stderr = csr1000v.exec_command(cmd)
        else:
            print('wrong command')

    return


# Load the yaml file to read parameters needed for test
with open('params.yaml', 'r') as f:
    params = yaml.load(f)

# Connect to the csr1000v anf traffic generator and see if traffic is running between them.
accesslist_config_test(params)

# access-list 110 permit tcp host 192.168.1.2 host 172.32.11.5 eq 80
