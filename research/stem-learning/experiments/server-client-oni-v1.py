from optparse import OptionParser
import sys
import datetime
from threading import Thread
import socket
import random
import time

hidden_service_interface = '127.0.0.1'
hidden_service_port = 11009

tor_server = '127.0.0.1'
tor_server_control_port = 9051
tor_server_socks_port = 9050

buffer_size = 2048

server_roster = dict()

class Server:
    messages = []

    def __init__(self, hostname):self.hostname=hostname

    def connect(self):
        # global server_roster
        # todo: setup server roster appending

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((hidden_service_interface, hidden_service_port))
        log("Server now active")
        log("Connect with `%s -c %s`" % (sys.argv[0], self.hostname))
        s.listen(5)

        # create server connection roster
        while True:
            try:
                conn, addr = s.accept()

                nick = "user_%d" % random.randint(0, 1000)
                log("Connection established to %s" % nick)
                wel_msg = "Welcome %s" % nick

                self.messages.append(wel_msg)

                handle = Thread(target=self.handle_client, args=(conn, addr, nick))
                handle.daemon = True
                handle.start()

            except KeyboardInterrupt:
                log("Server closing.")
                exit(0)

            except:continue

    def handle_client(self, conn, addr, nickname):
        while True:
            try:
                data = conn.recv(buffer_size)
                if not data:break
                log("%s >> %s" % (nickname, sanitize(data)))
                msg = (add_padding('hello there')).encode()
                conn.send(msg)
                log("server >> " + sanitize(msg))
            except:break
        conn.close()
        log("Connection closed to %s" % nickname)

class TorStem:
    def connect(self, addr = '127.0.0.1', con_port = 9051):
        """Connects to the Tor control port and starts the server connection.

        Args:
            addr (str, optional): Address of the tor server. Defaults to '127.0.0.1'.
            con_port (int, optional): Control port of the tor server. Defaults to 9051.
        """
        log("Connecting to Tor Server via Stem module")
        try:
            from stem.control import Controller
        except:
            log("Cannot load stem module.")
            log("Try installing python-stem with your local package manager.")
            exit(0)

        # Connect to Tor
        # make sure you run tests locally
        self.controller = Controller.from_port(address=addr, port=con_port)
        self.controller.authenticate()

        bytes_read = self.controller.get_info("traffic/read")
        bytes_written = self.controller.get_info("traffic/written")

        log("Tor relay is alive. %s bytes read, %s bytes written." % (bytes_read, bytes_written))
        log("Tor Version: %s" % str(self.controller.get_version()))

        # Get socks port
        try:
            self.SocksPort = self.controller.get_conf("SocksPort")
            if self.SocksPort == None:
                self.SocksPort = 9050
            else:self.SocksPort = int(self.SocksPort)
            log("Socks port is: %d" % self.SocksPort)
        except:
            log("Failed to get Socks port, trying 127.0.0.1:9050...")
            self.SocksPort = 9050
            pass

        # displaying onion url
        self.hostname = self.controller.create_ephemeral_hidden_service({hidden_service_port: '%s:%d' % (hidden_service_interface, hidden_service_port)}, await_publication = True).service_id + '.onion'
        log("Hostname is %s" % self.hostname)

def add_padding(data: str):
    """
    * `data`: The unicode string to be padded

    Appends the necessary buffer data to the message
    """
    global buffer_size
    if len(data) < buffer_size:
        data += chr(0)
        data = bytearray(data.encode())
        for _ in range(0, buffer_size - len(data)):
            data += chr(random.randint(33, 127)).encode() # ord('!'), ord('~') all unicode English alphabet
    return data

def sanitize(data: str):
    if len(data) > 0:
        return str(data.split(bytearray(chr(0).encode()))[0]) # split on \x0 and return relevant data
    else:return

def log(*args) -> str:
    arg_strs = []
    arg_print = True
    if len(args) > 1 and type(args[-1]) is bool:
        arg_print = args[-1]
        args = args[:-1]
    for arg in args:
        string = "[%s] %s" % (datetime.datetime.now().strftime("%H:%M:%S"), arg)
        if arg_print is False:
            arg_strs.append(string)
            continue
        print(string)
    if arg_print is False: return arg_strs

def clean_print_msg(data: str):
    # junk_start = data.find(chr(0))
    data_txt = data.split(chr(0))[0] + ' '
    clean_print =  '...' #'.' * (buffer_size-junk_start-1)
    log(data_txt + clean_print)

def main_client(destination) -> None:
    # todo[x]: continue the client to allow for receiving messages
    # todo[ ]: allow the client to send real-time information
    # todo[x]: fix the client issue with the double message print with (server1-client1-test):

    try: # import the socks library
        import socks
    except:
        log("Failed to import SocksiPy module.")
        log("Please install SocksiPy before proceeding.")
        exit(0)

    # perform client connection
    while True:
        try:
            log("Attempting connection to %s:%d" % (destination, hidden_service_port))

            s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            s.setproxy(socks.PROXY_TYPE_SOCKS5, tor_server, tor_server_socks_port)
            s.settimeout(0)
            s.connect((destination, hidden_service_port))
            s.setblocking(0)

            log("Client Connection: Connected to %s" % destination)
            break;
            # log("Client connection: Requesting roster...")
        except:
            log("Client Connection: Cannot connect. Retrying...")
            continue

    while True: # configure the socket connection and send an obfuscated message
        try:
            # todo
            # : setup message obfuscation
            # : sending `None` after the message

            # the very beta rendition of client message sending
            msg = input(log('> ', False)[0])
            msg = add_padding(msg)

            x = bytearray(msg)

            _result = s.send(x)

            data = None
            while not data:
                try:
                    # note: look at recvfrom func
                    data = s.recv(buffer_size)
                except:pass
            log("server >> " + sanitize(data))
        except KeyboardInterrupt:break

    s.close()
    log("Client Connection: Disconnected from Server")
    return

def main_server(hostaddr='') -> None:
    ts = TorStem()
    try:
        ts.connect()
    except:
        log("Failed to connect to Tor Server Control Port.")
        log("Try running the `tor` service manually via the terminal.")
        exit(0)
    
    server = Server(ts.hostname)
    server.connect()

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-c", "--client", action="store", type="string", dest="destination", help="Target client server")
    parser.add_option("-s", "--server", action="store", type="string", dest="server", help="Target domain for the tor server")
    # parser.add_option("-p", "--port", action="store", type="int", dest="port", help="Defines the operating port")

    if len(sys.argv)==1:
        parser.print_help()
        exit(0)

    (options, _args) = parser.parse_args()
    # log(options)
    # if options.port != None : tor_server_socks_port = int(options.port)

    if options.server:
        main_server(options.server)
    else:
        if len(options.destination) > 0:
            main_client(options.destination)
        else : parser.print_help()
    
