# automation scripts

find_rtt.py -- 

Scenario ---- I have two servers server1 and server2. Both servers have two public IPs sip1 and sip2. server1 has sip1 as primary and server2 has sip2 as primary IP(this can be done using  bgp).Now there is a vendor server vendor1 which has one public IP vip1.

Server Name               Server IP
server1          -->      sip1 (primary) and sip2 (secondary)
server2          -->      sip2 (secondary) and sip1 (primary)
vendor1          -->      vip1 (primary)

I want to know which server is near(least rtt) to vip1. I can do that by logging in to server1 and server2 and manually pinging vip1.
This script automates all these steps and returns the public IP which has lowest rtt.
We can easily extend the script to check multiple vendor IPs.

Command format -- python3 find_rtt.py ssh-username ssh-pwd server1-name server1-primary-ip server2-name server2-primary-ip vendor1-ip
Example command -- python3 find_rtt.py my-username 12345678 server1 1.1.1.1 server2 2.2.2.2 8.8.8.8
