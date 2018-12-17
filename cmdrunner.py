import netmiko
import json
import mytools
import sys


with open(sys.argv[1]) as cmd_file:
    commands = cmd_file.readlines()

with open(sys.argv[2]) as dev_file:
    devices = json.load(dev_file)

username, password = mytools.get_credentials()

net_exceptions = ('netmiko.ssh_execption.NetMikoAuthenticationException',
                  'netmiko.ssh_execption.NetMikoTimeoutException')

for device in devices:
    device['username'] = username
    device['password'] = password
    try:
        print(('~'*79) + '\n Connecting to device ', + device['ip'] + '\n')
        connection = netmiko.ConnectHandler(**device)
        filename = connection.base_prompt + '.txt'
        with open(filename, 'w') as out_file:
            for command in commands:
                out_file.write('## Output of ' + command + '\n\n')
                out_file.write(connection.send_command(command) + '\n\n')
        connection.disconnect()
    except net_exceptions as exception:
        print('####Authentication Failed to ', + device['ip'] + '#### \n' + exception + '\n')
