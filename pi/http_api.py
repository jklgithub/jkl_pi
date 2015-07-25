#http_api.py coding:utf-8 对外暴漏的各种借口，以及对外部http接口的访问

# import sys
# import BaseHTTPServer
# from SimpleHTTPServer import SimpleHTTPRequestHandler
# HandlerClass    = SimpleHTTPRequestHandler
# ServerClass     = BaseHTTPServer.HTTPServer
# Protocol        = "HTTP/1.0"
#
# def startHttpSevvice(port):
#     server_address                  = ('127.0.0.1', port)
#
#     HandlerClass.protocol_version   = Protocol
#     httpd                           = ServerClass(server_address, HandlerClass)
#
#     sa                              = httpd.socket.getsockname()
#     print "Serving HTTP on", sa[0], "port", sa[1], "..."
#     httpd.serve_forever()
#
# if __name__ == '__main__':
#     startHttpSevvice(8002)

#import BaseHTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
import cgi

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('-----------------do_GET')
        input(self)

    def do_POST(self):
        print('-----------------do_POST')
        input(self)

def input(self):
    form = cgi.FieldStorage()
    parsed_path = urlparse.urlparse(self.path)
    message_parts = [
            'CLIENT VALUES:',
            'client_address=%s (%s)' % (self.client_address,
                                        self.address_string()),
            'command=%s' % self.command,
            'path=%s' % self.path,
            'real path=%s' % parsed_path.path,
            'query=%s' % parsed_path.query,
            'request_version=%s' % self.request_version,
            '',
            'SERVER VALUES:',
            'server_version=%s' % self.server_version,
            'sys_version=%s' % self.sys_version,
            'protocol_version=%s' % self.protocol_version,
            '',
            'HEADERS RECEIVED:',
        ]
    for name, value in sorted(self.headers.items()):
        message_parts.append('%s=%s' % (name, value.rstrip()))
    message_parts.append('')
    message = '\r\n'.join(message_parts)
#    print(message)

    self.send_response(200)
    self.end_headers()
    self.wfile.write(message)


if __name__ == '__main__':
    #  server = BaseHTTPServer.HTTPServer(('0.0.0.0',8002), WebRequestHandler)
    server = HTTPServer(('127.0.0.1', 8002), WebRequestHandler)
    server.serve_forever()



