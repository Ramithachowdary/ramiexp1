from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<h1>LAPTOP CONFIGURATION</h1>
<body>

    <table border="5" cellspacing="10" cellpadding="6">
        <TR> 
            <TH>Device name	</TH>
            <TH>DESKTOP-MOHHBTU </TH>  
        </TR>  
        <TR>
            <TD>Processor</TD> 
            <TD>13th Gen Intel(R)Core(TM) i5-1335U 1.30 GHz</TD> 
            
        </TR>
        <TR>
            <TD>Installed RAM</TD> 
            <TD>16.0 GB (15.7 GB usable)</TD> 
            
        </TR>
        <TR>
            <TD>System type</TD> 
            <TD >64-bit operating system, x64-based processor</TD> 
          
            
        </TR></table>

</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()