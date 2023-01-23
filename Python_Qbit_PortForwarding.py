#NAT Portforwarding for Qbittorrent with OPENVPN eg. ProtonVPN custom Openvpn config
#depence on natpmp-util, qbittorrent-cli

import os
import subprocess
import time

def map_Port():
       
    cmd = "natpmpc"
    temp = subprocess.Popen([cmd,'-a','0','0' , 'tcp','60'], stdout=subprocess.PIPE)
    output = str(temp.communicate())
    index_of_port = output.index('public port')
    port_nr_extern = (output[index_of_port+12:index_of_port+17])
    
    
    index_of_ip = output.index('Public IP address :')
    ip_nr_extern = (output[index_of_ip+20:index_of_ip+34])
    
    #print(output)

    index_of_local_port = output.index('local port')
    port_nr_local = (output[index_of_local_port+11:index_of_local_port+16])
    
   
   
    print("IP Adresse extern: ")
    print(ip_nr_extern)
    print("Port local: ")
    print(port_nr_local)
    print("Port extern: ")
    print(port_nr_extern)
    
    if port_nr_local == port_nr_extern:
        return port_nr_local
    else:
        return 0 


def check_qbit_Port(port_forwarded):
    cmd ="qbt"
    temp = subprocess.Popen([cmd,'server','settings','connection'], stdout=subprocess.PIPE)
    output = str(temp.communicate())
    #print(output)
    index_of_qbit_port = output.index('Incoming connections port:')
    #print(index_of_qbit_port)
    qbit_port = (output[index_of_qbit_port+44:index_of_qbit_port+49])
    print("Port von Qbit:")
    print(qbit_port)
    if port_forwarded == qbit_port:
        return 0
    else:
        return 1

def set_qbit_Port(port_to_set):
    cmd ="qbt"
    temp = subprocess.Popen([cmd,'server','settings','connection','--listen-port', port_to_set])


while True:
    
   #mapped_port = map_Port()
   #print("\nMapped Port: ")
   #print(mapped_port)
   #set_qbit_Port("1234")   
   matched = check_qbit_Port(map_Port())
   #print(matched)
   if matched == 0:
       print("Port stimmt mit qbit ueberein!")
   else:
        print("Port stimmt nicht ueberein!")
        print("Setze neuen Port in Qbit")
        set_qbit_Port(map_Port())

   time.sleep(55)
