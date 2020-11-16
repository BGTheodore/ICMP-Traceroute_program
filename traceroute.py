import socket
import time
port = 6332 
maxhop = 50

def Traceroute(nomDestination):  
    adresseDestination= socket.gethostbyname(nomDestination)
    icmp = socket.getprotobyname( "icmp")
    udp = socket.getprotobyname("udp")
    tempsExec = 1
    while True:
        envoiPaquet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
	    receptionPaquet = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp) 
        envoiPaquet.setsockopt(socket.SOL_IP, socket.IP_TTL, tempsExec)
        receptionPaquet.bind(("", port)) 
        envoiPaquet.sendto("TEST", (nomDestination, port)) 

        hopPaquet = None
        hopNom = None

        try:
            donnee, hopPaquet = receptionPaquet.recvfrom(512) 
            hopPaquet= hopPaquet[0]
            try:
                hopNom = socket.gethostbyaddr(hopPaquet)[0] 

            except socket.error:
                hopNom = hopPaquet
        except socket.error: 
            print('timeout error')
        finally:
            envoiPaquet.close()
            receptionPaquet.close()

        if hopPaquet is not None: 
            actuel= "%s (%s)" % (hopNom, hopPaquet)
        else:
            actuel = "*" 
        print "%d\t%s" % (tempsExec, actuel)

        tempsExec += 1

        if actuel == adresseDestination or tempsExec > maxhop: 
            break

if __name__ == "__main__":
    nomDestination = raw_input('Enter the destination : ')
    print('Traceroute to {} ({}) on port : {}, {} hops max'.format(nomDestination, socket.gethostbyname(nomDestination), port ,maxhop))
    startTime = time.time() 
    Traceroute(nomDestination)