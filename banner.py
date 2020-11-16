import socket 
import os  
import csv

csv_output = {}
new_attribute =[]
start_port = 1
end_port = 1024
def portscan(server_address):
 try:
    for port in range(start_port, end_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((server_address,port))
        if result == 0:
            new_attribute  =[]
            banner = banner_get(server_address,port)
            domain = socket.gethostbyaddr(server_address)[0]
            service =str(socket.getservbyport(port))
            print ("Open socket detected: {}:{} \t-- Service: {} \t-- Hostname: {} \t--Banner: {}" .format(server_address,port,service,domain, banner)) 
            new_attribute .append(str(server_address)) 
            new_attribute .append(str(service))
            new_attribute .append(str(domain))
            new_attribute .append(str(banner))
            csv_output [port] = new_attribute 
 
 except socket.error:
     pass
 finally:
        sock.close()

def banner_get(server_address,port):
        print( "Trying to reach port ", port)
        objet_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       
        try:
            objet_socket.connect((server_address, port))
            objet_socket.send('GET HTTP/1.1 \r\n')
            banner = objet_socket.recv(100)
            objet_socket.close()
            return banner
        except:
             return "Banner not found !!"

def csv_maker(csv_output ):
      csv_columns = ['Port', 'IP', 'Service', 'Domain', 'Banner']
      with open('portSweep.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()
        for key in csv_output .keys():
            f.write("%s, %s, %s, %s, %s\n" % (key, csv_output [key][0], csv_output [key][1], csv_output [key][2], csv_output [key][3]))
      print('File portSweep.csv generated successuffly !!')
if __name__ == "__main__":
    server_address = input('Enter the server IP : ')
    portscan(server_address)
    print(csv_output )
    csv_maker(csv_output )
  