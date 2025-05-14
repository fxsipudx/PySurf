import socket

class URL:
    def __init__(self,url):
        self.scheme, url = url.split("://",1)
        assert self.scheme == "http" # Helps us in debugging. If "True" nothing happens if false cause problem
        
        if "/" not in url:
            url = url + "/"
        self.host, url = url.split("/",1)
        self.path = "/" + url
        
    def response(self):
        s = socket.socket(
            family=socket.AF_INET, # Using IPv4 addresses 
            type=socket.SOCK_STREAM, # Setting up a stream socket (TCP)
            proto=socket.IPPROTO_TCP  
        )