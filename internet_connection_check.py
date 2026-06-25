import socket

try:
    # Attempting to establish a connection to google.com on port 80
    socket.create_connection(('google.com', 80))
    print("Good Connection")
    
except:
    # Executed if the connection attempt fails
    print("No Internet yet")