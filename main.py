import nmap
scaner = nmap.PortScanner()
scaner.scan('104.26.0.24','1-1024', '-v -sS -sV -sC -A -O')

for host in scaner.all_hosts():
    print("Host: ", host)
    for proto in scaner[host].all_protocols():
        lport = scaner[host][proto].keys()
        for port in lport:
            print("   Port: ", port)
            print("   Name: ", scaner[host][proto][port]['name'])
            print("   State: ", scaner[host][proto][port]['state'])
            print("   Version: ", scaner[host][proto][port]['version'])
            if 'product' in scaner[host][proto][port]:
                print("   Product: ", scaner[host][proto][port]['product'])
            if 'extrainfo' in scaner[host][proto][port]:
                print("   Extra Info: ", scaner[host][proto][port]['extrainfo'])




