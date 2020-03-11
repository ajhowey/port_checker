#!/usr/bin/env python

# import psutil
try:
	import psutil
except:
	print("\nYou need to install the 'psutil' library.")
	print("Run the following command at the command line:\n\n\t'pip install psutil'\n")
	quit()
 
def check_listening_port(port):
    """Return True if the given TCP port is busy and in LISTEN mode."""
    for conn in psutil.net_connections(kind='tcp'):
        if conn.laddr[1] == port and conn.status == psutil.CONN_LISTEN:
            return True
    return False
 
PORTS = [20,21,22,23,25,37,53,80,123,143,161,162,389,443,512,513,514,636]
for PORT in PORTS:
	STATUS = check_listening_port(PORT)
	if STATUS == True:
		print("Port", PORT, "is currently active and listening.")
	else:
		print("Port", PORT, "is not currently active.")


