# EX01 Developing a Simple Webserver
## Date:26.10.24

## AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
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
```

## OUTPUT:
![alt text](<Screenshot 2024-10-26 053544.png>)
![alt text](<Screenshot 2024-10-26 053558.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
