import socket
targets = input("Enter the targets(split them by ' ' if multiple) ")
ports= int(input("Enter the number of ports you want to scan "))
for i in targets.split(' '):
    print("Scanning for ports in"+ i)
    for j in range(ports):
        try:
            s = socket.socket()
            s.connect((i,j))
            print("port opened"+str(j))
            s.close()
        except:
            pass  
