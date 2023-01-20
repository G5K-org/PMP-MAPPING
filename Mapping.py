import os
import subprocess
import time
interner_port = "55555"

def start_openvpn():
    cmd = "openvpn"
    temp = subprocess.Popen([cmd, 'vpn.ovpn'],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    #output = str(temp.communicate())
    #print(output)
    #print("\n\n\n")
    return 0

def get_IP():
    print("External IP:")
    cmd = "curl"
    temp = subprocess.Popen([cmd,'-4','icanhazip.com'],)
    #output = str(temp.communicate())
    #index = output.rfind("b'")
    #print(temp)
    return 0

def map_Port():
    cmd = "natpmpc"
    temp = subprocess.Popen([cmd,'-a','44444', interner_port, 'tcp','60'])
    return 0

start_openvpn()
print("waiting for OpenVPN")
time.sleep(10)
get_IP()
time.sleep(1)

while(True):
    print("\n------=======Handshake PMP=========------\n")
    map_Port()
    time.sleep(55)
