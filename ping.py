import socket
from datetime import datetime
import http.server
import socketserver

adresse_ip = input("Enter the IP address: ")
debut = datetime.now()
tempsExec= 0.025
port = 6332
socket.setdefaulttimeout(tempsExec)

def scan(adresse):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   resultat = sock.connect_ex((adresse,port))
   if resultat == 0:
      return 1
   else :
      return 0

def ping(adresse):
      if (scan(adresse)):
         fin = datetime.now()
         total = fin - debut
         print('Succes !!')
         print ("from {}: ttl={} time={} ".format(adresse, tempsExec, total))
      else:
          print('Port unreachable')

# Lancement       
ping(adresse_ip )