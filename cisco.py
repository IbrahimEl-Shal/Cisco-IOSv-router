import os 
from netmiko import ConnectHandler 
from dotenv import load_dotenv
import json

load_dotenv()

switch = {
    'device_type':'cisco_ios_telnet',
    'ip': '192.168.17.129',
    'username':'memadd',
    'password':'12345gns3',
    'secret':'12345gns3',
    'port':5000
      
}

try:
    c = ConnectHandler(**switch)
    c.enable()

    #inventory info
    inventory = c.send_command('show inventory', use_textfsm=True)
    print(json.dumps(inventory,indent=2))

    #version info 
    version = c.send_command('show version', use_textfsm=True)
    print(json.dumps(version,indent=2))

    #interfaces
    interfaces = c.send_command('show interfaces', use_textfsm=True)
    #loop over each interface
    for interface in interfaces:
        #check interface status
        if interface['link_status'] == 'up':
            print(f"MAC address: {interface['address']}")
    
    #interfaces-brief
    ints = c.send_command('show ip int brief', use_textfsm=True)
    print(json.dumps(ints,indent=2))
    
except Exception as e:
    print(e)    



   


 