"""
Author Akash
Scenario ---- I have two servers server1 and server2. Both servers have two public IPs sip1 and sip2. server1 has sip1 as primary and server2 has sip2 as primary IP(this can be done using  bgp).Now there is a vendor server vendor11 which has one public IP vip1.

Server Name          Server IP
server1          -->      sip1 (primary) and sip2 (secondary)
server2          -->      sip2 (secondary) and sip1 (primary)
vendor1          -->      vip1 (primary)

I want to know if the vendor server vendor1 is near(least rtt) to sever1 or server2. I can do that by logging in to server1 and server2 and manually pinging vendor1 IP (vip1).Then the ping which has the least rtt can be determined. 
This script automates all these steps and returns the lowest rtt.
We can easily extend the script to check multiple vendor IPs.

Command format -- python3 find_rtt.py ssh-username ssh-pwd server1-name server1-primary-ip server2-name server2-primary-ip vendor1-ip
Example command -- python3 find_rtt.py my-username 12345678 server1 1.1.1.1 server2 2.2.2.2 8.8.8.8
"""

# Import modules

import paramiko
import sys

# Save command line arguments as variables

username = sys.argv[1]
password = sys.argv[2]
server1 = sys.argv[3]
sip1 = sys.argv[4]
server2 = sys.argv[5]
sip2 = sys.argv[6]
vip1 = sys.argv[7]

print(f"Getting average ping rtt from {server1} and {server2} ")

# Define a fuction to run ping command remotely and then return rtt
 
def get_avg_rtt(server_name, server_primary_ip, vendor_ip):
    ping_command = 'ping -I ' + sip1 + ' ' + vip1 + ' -c 1'
    avg_rtt = 0
    if vendor_ip == '0':
        return avg_rtt
    else:    
        try:
            print(f'Checking rtt for vendor IP {vip1} from {server1}')
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(server1, port=22, username=username, password=password)
            stdin, stdout, stderr = ssh.exec_command(ping_command)
            output = stdout.readlines()
            ssh.close()
            avg_rtt = output[-1].split("/")[-3]
            return avg_rtt
        except Exception as e:
            print(e)
            print("Vendor IP might not be pingable")

server1_avg_rtt = get_avg_rtt(server1, sip1, vip1)
server2_avg_rtt = get_avg_rtt(server2, sip2, vip1) 

print(f'Average rtt from {server1} is {server1_avg_rtt} ms')
print(f'Average rtt from {server2} is {server2_avg_rtt} ms')

if server2_avg_rtt > server1_avg_rtt:
    public_ip = sip1
else:
    public_ip = sip2

print(f"Please use {public_ip} as Public IP to connect with this vendor")
