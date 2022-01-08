#Library Crap
import http.server
import socketserver
import configparser
import os.path

#Custom GoTo function (thanks Tim Peters from Stack Overflow)
def goto(linenum):
    global line
    line = linenum

#Activate Config File Parser and read Settings
parser = configparser.ConfigParser()
parser.read('settings.config')

#Set port from Config
port = parser.get('PORT', 'Port')
portint = int(port)

#Check if Index File Exists
if os.path.isfile('index.html') == True:
    print('Starting Server...')
    goto(38)
else:
    print('ERROR: CAN NOT FIND INDEX.HTML - WILL RUN IN DIRECTORY LISTING MODE')
    goto(38)

#Starting Server
linenum = '38'
print("Simple Py Web Server.")
print("v0.1")
print("So far HTTPS doesnt work, and you can not run it in background.")
print(" ")

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", portint), Handler) as httpd:
    print(f"Site Hosted at 127.0.0.1:{portint}")
    httpd.serve_forever()
    
