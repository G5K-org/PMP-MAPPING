#!/usr/bin/env python
import qbittorrentapi
import getopt
import sys 
from datetime import datetime

try:
    import natpmp as NATPMP
except ImportError:
    import NATPMP

qbt_client = qbittorrentapi.Client(
    host='localhost',
    port=8080,
    username='admin',
    password='xxxxx',
)

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)



protocol = NATPMP.NATPMP_PROTOCOL_TCP
lifetime = 60
public_port = 0
private_port = 0
gateway = NATPMP.get_gateway_addr()
port_mapping_temp = NATPMP.map_tcp_port(public_port, private_port, lifetime, gateway_ip=gateway)
string_ports = str(port_mapping_temp)
index_of_private_port = string_ports.index('private_port')
private_port_int= int(string_ports[index_of_private_port+13:index_of_private_port+18])
index_of_public_port = string_ports.index('public')
public_port_int = int(string_ports[index_of_public_port+12:index_of_public_port+17])
webui_port_int = int(qbt_client.app_preferences().get("listen_port"))

print("\n")
print(datetime.now())
print("Oeffentliche IP Adresse        : "+str(NATPMP.get_public_address())) 
print("Lokaler Port                  : "+str(private_port_int))
print("Oeffentlicher Port vom VPN     : "+str(public_port_int))
print("Port von QBittorrent WEBUI    : "+str(webui_port_int))

if private_port_int != public_port_int:
    print("Ports unterschiedlich! QBittorrent nicht erreichbar!")
    
if public_port_int != webui_port_int:
    print("Port im WEBUI stimmt nicht ueberein mit NATMAP Ports...aktualisiere!")
    qbt_client.app_setPreferences({"listen_port":public_port_int})
    print("Neuer WEBUI PORT          :"+ str(qbt_client.app_preferences().get("listen_port")))
else:   
    print("PORTS sind aktuell!")


