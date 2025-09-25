from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>
  <center><font color="blue" face="Times new roman" size="99">
        <b>Lists of protocols in TCP/IP Model</b>
        </font></center>
        <font color="red">
        <h2>Application Layer - HTTP, FTP, DNS, Telnet<br>
        Transport Layer - TCP & UDP<br>
        Network Type - IPV4/TPV6<br>
        Link Layer - Ethernet/h2>
        </font>
</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',1700)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()