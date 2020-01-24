import socket 448
Host = "www.targget-siste.com
HostToIP  = socket.gethostbyname(Host)
or port in range(20,100):
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.5)
result = sock.connect_ex((HostToIP, port))
if result == 0:
    print "[+] Port {}:      Open".format(port)
    else:
    print "[-] Port {}:      Closed".format(port)
    sock.close()
except:
    pass
