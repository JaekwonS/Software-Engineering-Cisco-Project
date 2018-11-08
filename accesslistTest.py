import re
import yaml
import time
import paramiko
from click._compat import raw_input


def accesslist_config_test(params):
    '''
    This test is to determine if tcp and ip configuration changes are correct

    '''

    csr1000v = paramiko.SSHClient()
    csr1000v.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    csr1000v.connect(params["csr1000v"]["IP"], port=22, username=params["csr1000v"]["Username"], password=params["csr1000v"]["Password"],
                allow_agent=False, look_for_keys=False, auth_timeout=30, passphrase=None)

    cmd = raw_input("Command to run: ")

    re1 = '((?:access-list))'  # access-list
    # re2 = '(\\s+)'  # White Space 1
    # re3 = '(\\d)'  # Any Single Digit 1
    # re4 = '(\\d)'  # Any Single Digit 2
    # re5 = '(\\d)'  # Any Single Digit 3
    # re6 = '(\\s+)'  # White Space 2
    # re7 = '((?permit))'  # permit
    # re8 = '(\\s+)'  # White Space 3
    re9 = '((?:tcp))'  # tcp
    re9b = '((?:ip))' # ip
    # re10 = '(\\s+)'  # White Space 4
    # re11 = '((?:host))'  # host
    # re12 = '(\\s+)'  # White Space 5
    # re13 = '((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\\d])'  # IPv4 IP Address 1
    # re14 = '(\\s+)'  # White Space 6
    # re15 = '((?:host))'  # host
    # re16 = '(\\s+)'  # White Space 7
    # re17 = '((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\\d])'  # IPv4 IP Address 2
    # re18 = '(\\s+)'  # White Space 8
    re19 = '((?:eq))'  # eq - designate port
    re20 = '(\\s+)'  # White Space 9
    re21 = '(\\d)'  # Any Single Digit 4
    re22 = '(\\d)'  # Any Single Digit 5

    # rg = re.compile(
    #     re1 + re2 + re3 + re4 + re5 + re6 + re7 + re8 + re9 + re10 + re11 + re12 + re13 + re14 + re15 + re16 + re17 + re18 + re19 + re20 + re21 + re22,
    #     re.DOTALL)
    # verify = bool(rg.match(cmd))

    reg = re.compile(re1)
    type1 = re.compile(re9)
    type2 = re.compile(re9b)
    ending = re.compile(re19 + re20 + re21 + re22)

    while reg.match(cmd):
        if type1.match(cmd):
            if not ending.match(cmd):
                print('error')
        elif type2.match(cmd):
            if ending.match(cmd):
                print('error')
        else:
            print('wrong command')

    return


# Load the yaml file to read parameters needed for test
with open('params.yaml', 'r') as f:
    params = yaml.load(f)

# Connect to the csr1000v anf traffic generator and see if traffic is running between them.
accesslist_config_test(params)
