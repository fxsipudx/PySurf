import socket

class URL:
    def __init__(self,url): #The URL Parser Splits http://example.org/index.html
        self.scheme, url = url.split("://",1)
        assert self.scheme == "http" # Helps us in debugging. If "True" nothing happens if false cause problem
        
        if "/" not in url:
            url = url + "/"
            
        self.host, url = url.split("/",1)
        self.path = "/" + url
        
    def request(self): #Socket Setup + Connection
        s = socket.socket(
            family=socket.AF_INET, # Using IPv4 addresses 
            type=socket.SOCK_STREAM, # Setting up a stream socket (TCP)
            proto=socket.IPPROTO_TCP  
        )
        # Create a TCP socket and connect to the host
        s.connect((self.host,80))
        
        # Compose HTTP GET request
        request = f"GET {self.path} HTTP/1.0\r\nHost: {self.host}\r\n\r\n"
        s.send(request.encode("utf8"))
        
        response = s.makefile("r",encoding="utf8",newline="\r\n")
        status_line = response.readline()
        version,status,explanation = status_line.split(" ",2)
        
        response_headers = {}
        
        while True:
            line = response.readline()
            if line == "\r\n":
                break
            header,value = line.split(":",1)
            response_headers[header.casefold()] = value.strip()
        
        assert "transfer-encoding" not in response_headers
        assert "content-encoding" not in response_headers
        
        content = response.read()
        s.close()
        return content        
            
            
        
        
        
    
        
        
    
   