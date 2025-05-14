import socket

class URL:
    def __init__(self,url): #The URL Parser Splits http://example.org/index.html
        self.scheme, url = url.split("://",1)
        assert self.scheme == "http" # Helps us in debugging. If "True" nothing happens if false cause problem
        
        if "/" not in url:
            url = url + "/"
        self.host, url = url.split("/",1)
        self.path = "/" + url
        
    def response(self): #Socket Setup + Connection
        s = socket.socket(
            family=socket.AF_INET, # Using IPv4 addresses 
            type=socket.SOCK_STREAM, # Setting up a stream socket (TCP)
            proto=socket.IPPROTO_TCP  
        )
        s.connect((self.host,80))
    
   