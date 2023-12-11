#!/usr/bin/env python2.7 
# -*- coding: utf-8 -*-

'''
###     TOR  IRC           ###        Fully anonymous text chat. Launch it using your python language interpreter in a bash shell / Konsole.
###     TorTextChat (TTC)  ###

  release home site                   https://gist.github.com/torifier/f1a7c1ac7b6b003cd9e1c187df2c5347
  TorTextChat version   1.981
  find chat partners, see also  :     https://beamstat.com/chan/general
  rendez-vous site beamstat.com :     http://bm6hsivrmdnxmw2f.onion.to/chan/torirc-rendezvous
  referral, see also stem       :     https://stem.torproject.org/tutorials/double_double_toil_and_trouble.html
  UBF = Ultimate BM Forum       :            bitmessage.mybb.im
  UBF release thread            :     http://bitmessage.mybb.im/viewtopic.php?id=21
  original Project homepage     :     https://github.com/froozen/torirc
  new Project homepage          :     https://github.com/torifier
  wiki                          :     https://github.com/torifier/torirc/wiki
  project alias name            :     TTC =  TorTextChat


  The project simply consists of this very file - a single python script.
  No additional file is needed from  github.com/froozen/torirc
  to run torIRC . Very handy and kewl !
  TorIRC is also published on Bitmessage, chan "general" as a torIRC.tar archive file 
  to avoid indentation problems after text-copy-paste. 
  Right-click, "save BM as file" named "torIRC.tar" and untar the .py scriptfile.
  Else, save this whole text as a file named   " torIRC.py "                         ---  it is a python v2.7 executable script


  Actually, 'torIRC' is a bit of a misnomer (taken over the original project name) since no IRC protocol is involved at all.
  torIRC uses very simple raw text exchange without any protocol as such on the python level. It works with both python2.7 and pypy.
  Maybe this project will later be renamed 'TTC' = TorTextChat .

 With TOR running, run torIRC as        ./torIRC.py    --server MY-CHAT              ---  this will start a chat server, now you need clients to connect to it

 The server will tell you how to connect , such as :


[I] Adding hidden service...  hit CTRL-C to stop your chat server 
[C] Hostname is     savjd7h4riras2aq.onion
[I] Server Active
[I] Connect with the command 

    ./torirc.py --connect=savjd7h4riras2aq.onion  

#################### ./torirc.py --connect              will run the client mode, so you can actually chat

#################### ./torirc.py --server               will run the server mode, to which the clients must connect. CTRL-C will stop server.


In the Client window, you'll see sth. like:

         ~$./torirc.py  -c x6nz4zuolgq5hhkr.onion
         Trying to connect to x6nz4zuolgq5hhkr.onion:11009
         clientConnection: Connected to x6nz4zuolgq5hhkr.onion


Now you can start to text chat !    In the client window, type    /help    for a documentation help text.
It takes ca. one minute, then you have a chat server going !   So kewl !
No need to edit /etc/tor/torrc  - except sometimes. 
Make sure the port numbers match up between this file (user var section) and torrc .

Test TOR-IRC by opening 3 Konsole-windows, then run 1 server and also run 2 clients. Then you can chat with yourself in the 2 client windows.
Expect 2-5 seconds of delay for every chat line.


STEM is located at             https://stem.torproject.org

Full auto mode with STEM library, 
install STEM and all other prerequisites beforehand with your package manager. 
Run run_tests.py -a   inside STEM lib dir from downloaded stem-master.zip to see if anything is reported missing , e.g. :

socksiPy             https://pypi.python.org/pypi/SocksiPy

### stem needs:
mock
pyflakes
pep8
pycrypto
tox

don't forget stem itself !


TO DO: use re-usable onions like in the mini Tor-WebServer at
https://gist.github.com/anonymous/a4b798b1a31a2a0d8caaf4770387b540






### to reduce the torIRC project into this single one .py-file, the original README file is attached below:
### no additional files needed, tor-IRC is now an "all-in-one-file project"     :-)



                       TorIRC


Anonymous IRC-like multiuser chat using TOR hidden services, with emphasis in network-analysis protection.

This is a simple client/server chat using TOR hidden services and the python Stem controller library, implemented in a single python file. 
License is GNU-GPL
Usage:

torirc.py [options]

Options:
  -h, --help                          show this help message and exit
  -c CONNECT, --connect=some-Server
                                      Acts as client, connect to server
  -s, --server                        Acts as server

Example use:

This is a console-only application. 
You need a recent version of TOR configured and in your path. 
Also the time of the computer needs to be correct or else TOR won't connect.

In the Server:

~$ sudo -u debian-tor ./torirc.py -s #EXAMPLESRV
[I] Connecting to TOR via Stem
[I] Tor relay is alive. 369347 bytes read, 317787 bytes written.
[C] Tor Version: 0.2.3.22-rc (git-4a0c70a817797420)
[C] Socks port is: 9050
[I] Adding hidden service...
[C] Hostname is x6nz4zuolgq5hhkr.onion
[I] Server Active
[I] Connect with the command "./torirc.py --connect=x6nz4zuolgq5hhkr.onion"

In the Client:

~$./torirc.py  -c x6nz4zuolgq5hhkr.onion
Trying to connect to x6nz4zuolgq5hhkr.onion:11009
clientConnection: Connected to x6nz4zuolgq5hhkr.onion

You will be assigned a randomly generated nick. You need to set your nick with '/nick' and you are good to go. If you want multiple chatrooms, start multiple servers, each one will auto-generate their own hidden-service url.
Objectives

Anonymous/Encrypted chat resistant to:

    Network analysis techniques
    Exploits
    Crypto attacks
    Trust minimization

To reach those objectives the design of torirc follows:

    Simplicity: Small means less bugs and easier to audit
    Interpreted language: Avoid most memory corruption bugs
    Minimize library use: Again, less code susceptible to bugs
    Entropy maximization: When possible, random delays and useless data is transmitted.

Discussion of choices

    Python: I selected python because it's what I know, and the interpreter is relatively small. Second choice would have been Java, but the JRE is too big and cumbersome. Also Python usually comes installed in most Linux distros. Also TOR has Stem, a very nice python-controller lib.

    TOR: big ugly chunk of C code that I do not trust entirely, but at this time is the only software that provides the functionality that I need, that is, hidden services and onion routing. Also, the current version of torirc doesn't have his own cryptography routines and uses TOR for it, but this may change in the future.

Alternatives

Here are alternative software and why I do not like it:

    IRC over tor: This is the best alternative, but only if you don't use any public server. Anyway this is vulnerable to exploits as IRC servers and clients tend to be huge pieces of C code. Also Network analysis is trivial with this protocol.

    MSN/Gtalk/Pidgin: Horrible choices, huge codebases, hundreds of libraries riddled with bugs, vulnerable to exploits, central server sees all your (often plaintext) messages, etc. Some plugins like OTR fix some shortcomings, but network analysis is also trivial.

    Silc: They wrote their own crypto, that's a big mistake. Also, it's written in C. I do believe they also don't protect against network analysis.

    torchat: Nice alternative but only P2P, latest versions started to creep with unsafe functionality like emoticons, etc.

Network analysis protections

This still is experimental software so no strong network-analysis-proof must be assumed. At this moment:

    Thanks to TOR, nobody, the server or the clients, known the IP address of nobody else.
    However, the server knows when a client is connected.
    The client periodically sends random data at random intervals.
    Every message is padded to minimum_message_len (currently 256 bytes)
    The server doesn't accurately report the number of clients in the chatroom, it only erases a nick approximately a day after it disconnects (this delay is also random)

Network analysis is a hard problem and there are hundreds of side-channels that can be used to determine if a user is connected or not. This information can be the difference between life and death for some people, so it's a useful problem to tackle IMHO.
Stem

Latest tor-irc version uses the Stem python library to connect and control TOR, and now it makes uses of the system TOR daemon instead of spawning it's own TOR process. This is more clean but it requires you to install the Stem library and configure the TOR control port. If you do not want to do this, the torirc-nostem.py script doesn't uses Stem, but it's bigger and uglier.



still TO DO:
Authentication                    # to restrict access to the tor process
Network-timing analysis graph



errors   TODO

 [E] Ephemeral hidden services were added in tor version 0.2.7.1-alpha

[notice]                       debian jessie :      Tor v0.2.5.12 (git-e7d9695a6fd06d08) running on Linux with Libevent 2.0.21-stable, OpenSSL 1.0.1t 


https://packages.debian.org/jessie-backports/amd64/tor/download
has the needed 0.2.8  with ephemerals   :-)

###  python source part below









fixed June 19th, 2016 by some BitMessage person

Copyright (C) 2012-2013, Alfredo Ortega <alfred@groundworkstech.com>
All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2, or (at your option)
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA,
or google it.

licence see:  https://github.com/alfred-gw/torirc/blob/master/COPYING

'''

__author__="alfred"
__date__ ="$Jul 30, 2013$"

import curses
from   threading import Thread
from   optparse  import OptionParser
import time,os,subprocess
import socket,select,random,sys
import tempfile







## ---------- Start of user-configurable variables ----------------

minimum_message_len=256

# Network-related variables
tor_server='127.0.0.1'

# Used if can't load it from configuration
tor_server_control_port=9051   # 9051                TBB / TOR
tor_server_socks_port=9050     # 9050
########################################################################################################  adjust this if you want
hidden_service_interface='127.0.0.1'
hidden_service_port=11009

## Time "noise". Increase this value in dire situations
clientRandomWait=1   # Random wait before sending messages
clientRandomNoise=10 # Random wait before sending the "noise message" to the server
serverRandomWait=1   # Random wait before sending messages 

## Gui
buddywidth=20

## ---------- End of user-configurable variables -----------------







# lists for the gui
chantext=[]
roster=[]

## Tor stem glue class

class torStem():
        def connect(self,addr='127.0.0.1',cport=9051):

                print("[I] Connecting to TOR via Stem library")
                # Load Stem lib
                try:
                        from stem.control import Controller
                except:
                        print("[E] Cannot load stem module.")
                        print("[E] Try installing python-stem with the package manager of your distro ('pacman' or whatever)")
                        exit(0)
                # Connect to TOR
                self.controller = Controller.from_port(address=addr,port=cport)
                self.controller.authenticate()  # provide the password here if you set one
        
                bytes_read = self.controller.get_info("traffic/read")
                bytes_written = self.controller.get_info("traffic/written")
        
                print("[I] Tor relay is alive. %s bytes read, %s bytes written." % (bytes_read, bytes_written))
                print("[C] Tor Version: %s" % str(self.controller.get_version()))
                # Get socks port
                try:
                    self.SocksPort=self.controller.get_conf("SocksPort")
                    if self.SocksPort==None:
                            self.SocksPort=9050
                    else:   self.SocksPort=int(self.SocksPort)
                    print("[C] Socks port is: %d" % self.SocksPort)
                except: 
                    print("[E] Failed to get Socks port, trying 127.0.0.1:9050...")
                    self.SocksPort=9050
                    pass






                # Add hidden service  ----------------------------------------------- error fixed now in 2016
                print("[I] Adding hidden service.  Hit CTRL-C to stop server afterwards.  Please wait ca. one minute until hidden service is ready.")
                
                self.hostname = self.controller.create_ephemeral_hidden_service({hidden_service_port: '%s:%d' % (hidden_service_interface, hidden_service_port)}, await_publication = True).service_id + '.onion'
                print("[C] Hostname is %s" % self.hostname)



        def disconnect(self):
          # Remove hidden service
          print("Removing hidden service and shutting down torIRC." )
 
          self.controller.remove_ephemeral_hidden_service(self.hostname.replace('.onion', ''))
 
  
  
  
  
            
            
# stuff from 2013 not working any longer :              



                #newHiddenServiceDir=tempfile.mkdtemp()
                #self.origConfmap = self.controller.get_conf_map("HiddenServiceOptions")
                #self.controller.set_options([
                        #('HiddenServiceDir' ,self.origConfmap["HiddenServiceDir"]),
                        #('HiddenServicePort',self.origConfmap["HiddenServicePort"]),
                        #('HiddenServiceDir',newHiddenServiceDir),
                        #('HiddenServicePort',"%d %s:%d" % (hidden_service_port,hidden_service_interface,hidden_service_port))
                        #])
                #self.hostname=open("%s/hostname" % newHiddenServiceDir,"rb").read().strip()




        #def disconnect(self):
          ## Remove hidden service
          #print("Removing hidden service..."
          #self.controller.set_options([
                #('HiddenServiceDir',self.origConfmap["HiddenServiceDir"]),
                #('HiddenServicePort',self.origConfmap["HiddenServicePort"])
                #])




## Log Mode (Server logs to stdout, client do not)
STDoutLog=False

# Add padding to a message up to minimum_message_len
def addpadding(message):
        if len(message)<minimum_message_len:
                message+=chr(0)
                for i in range(minimum_message_len-len(message)):
                        message+=chr(random.randint(ord('a'),ord('z')))
        return message
                

## Return sanitized version of input string
def sanitize(string):
        out=""
        for c in string:
                if (ord(c)==0): break # char(0) marks start of padding
                if (ord(c)>=0x20) and (ord(c)<0x80):
                        out+=c
        return out

## Log function
## Logs to STDOut or to the chantext channel list
def log(text):
        if (STDOutLog):
                print(text)
        else:
                maxlen=width-buddywidth-1
                while (True):
                        if (len(text[:maxlen])>0):
                                chantext.append(text[:maxlen])
                        text=text[maxlen:]
                        if text=='':
                                break
                redraw(stdscr)
                stdscr.refresh()


### Server class
# Contains the server socket listener/writer

class Server():
        # Server roster dictionary: nick->timestamp
        serverRoster={}

        ## List of message queues to send to clients
        servermsgs=[]

        ## channel name
        channelname=""

        ## Eliminate all nicks more than a day old
        def serverRosterCleanThread(self):
                while True:
                        time.sleep(10)
                        current=time.time()
                        waittime = random.randint(60*60*10,60*60*36)         # 10 hours to 1.5 days
                        for b in self.serverRoster:
                                if current-self.serverRoster[b]>waittime:    # Idle for more than the time limit
                                        self.serverRoster.pop(b)             # eliminate nick
                                        waittime = random.randint(60*60*10,60*60*36)
                        
        ## Thread attending a single client
        def serverThread(self,conn,addr,msg,nick):
                log("(ServerThread): Received connection - a buddy connected !")
                conn.setblocking(0)
                randomwait=random.randint(1,serverRandomWait)
                while (True):
                        try:
                                time.sleep(1)
                                ready = select.select([conn], [], [], 1.0)
                                if ready[0]:
                                        data=sanitize(conn.recv(minimum_message_len))
                                        if len(data)==0: continue
                                        message="%s: %s" % (nick,data)
                                        # Received PING, send PONG
                                        if data.startswith("/PING"):
                                                message=""
                                                msg.append(data)
                                                continue
                                        # Change nick. Note that we do not add to roster before this operation
                                        if data.startswith("/nick "): 
                                                newnick=data[6:].strip()
                                                if newnick.startswith("--"):continue
                                                log("Nick change: %s->%s" % (nick,newnick))
                                                nick=newnick
                                                self.serverRoster[newnick]=time.time() # save/refresh timestamp
                                                message="Nick changed to %s" % newnick
                                                msg.append(message)
                                                continue
                                        # Return roster
                                        if data.startswith("/roster"):
                                                message = "--roster"
                                                message+=" %s" % self.channelname
                                                totalbuddies=len(self.servermsgs)
                                                for r in self.serverRoster:
                                                        message+=" %s" % r
                                                        totalbuddies-=1
                                                message+=" --anonymous:%d" % totalbuddies
                                                msg.append(message)
                                                continue
                                        if data.startswith("/serverhelp"):
                                                msg.append("These are the commands which are supported:")
                                                msg.append("     /serverhelp         : Send this help text")
                                                msg.append("     /roster             : Send the list of connected buddies")
                                                msg.append("     /nick <my-new-name> : Changes your nickname")
                                                continue
                                        # refresh timestamp
                                        self.serverRoster[nick]=time.time() 
                                        # Send 'message' to all queues
                                        for m in self.servermsgs:
                                                m.append(message)
                                # We need to send a message
                                if len(msg)>0:
                                        randomwait-=1 # Wait some random time to add noise
                                        if randomwait==0:
                                                m = addpadding(msg.pop(0))
                                                conn.sendall(m)
                                                randomwait=random.randint(1,serverRandomWait)
                                # Random wait before sending noise to the client
                                if random.randint(0,clientRandomNoise)==0: 
                                        ping="/PING "
                                        for i in range(120):
                                                ping+="%02X" % random.randint(ord('a'),ord('z'))
                                        msg.append(ping)
                        except:
                                self.servermsgs.remove(msg)
                                conn.close()
                                print("exiting: msgs %d" % len(self.servermsgs))
                                raise

        ## Server main thread
        def serverMain(self,channel_name):
                global STDOutLog
                STDOutLog=True
                self.channelname=channel_name
                # Connects to TOR and create hidden service
                self.ts=torStem()
                try:
                        self.ts.connect(tor_server,tor_server_control_port)
                except Exception as e:
                        log("[E] %s" % e)
                        log("[E] Check if the control port is activated in /etc/tor/torrc")
                        log("[E] Try to run as the same user as tor, i.e.   sudo -u debian-tor ./torirc.py -s MY-CHAT  (maybe useful or not) ")
                        exit(0)
##                                                                                          advice is not useful in Arch Linux with user "tor" 
                # Start server socket
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
                s.bind((hidden_service_interface,hidden_service_port))          
                log('[I] chat Server now Active')
                log('[I] Connect in order to chat typing the command "%s --connect=%s"' % (sys.argv[0],self.ts.hostname))
                s.listen(5)
                # Create server roster cleanup thread
                t = Thread(target=self.serverRosterCleanThread, args=())
                t.daemon = True
                t.start()
                while True:
                        try:
                                conn,addr = s.accept()
                                cmsg=[]
                                nick="anon_%d" % random.randint(0,10000)
                                cmsg.append("Welcome %s, this is %s" % (nick,self.channelname))
                                self.servermsgs.append(cmsg)
                                t = Thread(target=self.serverThread, args=(conn,addr,cmsg,nick))
                                t.daemon = True
                                t.start()
                        except KeyboardInterrupt:
                                self.ts.disconnect()
                                log("[I] (Main chat Server Thread): Exiting")
                                exit(0)
                        except:
                                pass

## Client commands
commands =[]

def chat_help():
        pass

# Client Help
def chat_help(args): 
        chantext.append("\ttor-IRC, %s %s" % (__author__,__date__))
        chantext.append("\tCommands available:")
        for c in commands:
                chantext.append("\t\t/%s: %s" % (c[0],c[2]))
        return ""
commands.append(("help",chat_help,"Local help"))


# Server help
def chat_server_help(args): 
        return "/serverhelp"
commands.append(("serverhelp",chat_server_help,"Request server commands help text"))

# Quit
def chat_quit(args): 
        exit(0)
commands.append(("quit",chat_quit,"Exit the python application 'TOR-IRC'"))

## --- end client commands

## Client GUI functions

count=0
cmdline=""
inspoint=0
pagepoint=0

def changeSize(stdscr):
        global width,height
        size = stdscr.getmaxyx()
        width=size[1]
        height=size[0]

def redraw(stdscr):
        global textpad
        global roster
        stdscr.clear()
        # draw Text
        line=height-3
        for i in reversed(range(len(chantext)-pagepoint)):
                try:
                        stdscr.addstr(line,0,chantext[i],0)
                        if line==0: break
                        else: line-=1
                except:
                        pass
        # draw roster
        for i in range(len(roster)):
                buddy=roster[i]
                stdscr.addstr(i,width-buddywidth+1,str(buddy),0)
        # draw lines
        stdscr.hline(height-2,0,curses.ACS_HLINE,width)
        stdscr.vline(0,width-buddywidth,curses.ACS_VLINE,height-2)
        # prompt
        prompt="~ "
        stdscr.addstr(height-1,0,"%s%s" % (prompt,cmdline),0)
        stdscr.move(height-1,len(prompt)+inspoint)

# Process command line
# Returns string to send to server
def processLine(command):
        if command.startswith("/"):
                comm=command[1:].split(' ')
                for t in commands:
                        if comm[0].startswith(t[0]):
                                func=t[1]
                                return func(comm)
        return command


# Client connection thread
def clientConnectionThread(stdscr,ServerOnionURL,msgs):
        global roster
        # Try to load Socksipy
        try:
                import socks
        except:
                print("[E] Cannot load socksiPy module.")
                print("[E] Try installing python-socksiPy with package manager of your distro : pypi.python.org/pypi/SocksiPy  ")
                exit(0)
        while(True):
                try: 
                        log("Trying to connect to %s:%d" % (ServerOnionURL,hidden_service_port))
                        ## Connects to TOR via Socks
                        s=socks.socksocket(socket.AF_INET,socket.SOCK_STREAM)
                        s.setproxy(socks.PROXY_TYPE_SOCKS5,tor_server,tor_server_socks_port)
                        s.settimeout(100)
                        s.connect((ServerOnionURL,hidden_service_port))
                        s.setblocking(0)
                        log("clientConnection: Connected to %s" % ServerOnionURL)
                        log("clientConnection: Autorequesting roster...")
                        msgs.append("/roster")
                        randomwait=random.randint(1,clientRandomWait)
                except:
                        log("clientConnection: Cannot connect! retrying...")
                        time.sleep(1)
                        continue
                try:
                        while(True):
                                time.sleep(1)
                                ready = select.select([s], [], [], 1.0)
                                # received data from server
                                if ready[0]:
                                        data=sanitize(s.recv(minimum_message_len))
                                        # received pong (ignore)
                                        if data.find("/PING ")>-1:
                                                continue 
                                        # received roster list
                                        if data.startswith("--roster"):
                                                roster=[]
                                                for i in data.split(' ')[1:]:
                                                        roster.append(i)
                                        # Write received data to channel
                                        log(data)
                                # We need to send a message
                                if len(msgs)>0:  
                                        randomwait-=1 # Wait some random time to add noise
                                        if randomwait==0:
                                                m = addpadding(msgs.pop(0))
                                                s.sendall(m)
                                                randomwait=random.randint(1,clientRandomWait)
                                # send noise in form of PINGs
                                if random.randint(0,clientRandomNoise)==0:
                                        ping="/PING "
                                        for i in range(120):
                                                ping+="%02X" % random.randint(0,255)
                                        #log("Sending %s" % ping)
                                        msgs.append(ping)
                except:
                        s.close()
                        pass


## Client main procedure
def clientMain(stdscr,ServerOnionURL):
        global cmdline
        global inspoint
        global pagepoint
        global width,height
        changeSize(stdscr)
        redraw(stdscr)
        
        ## Message queue to send to server
        msgs=[]
        t = Thread(target=clientConnectionThread, args=(stdscr,ServerOnionURL,msgs))
        t.daemon = True
        t.start()

        # Main Loop
        while True:
                input=stdscr.getch()

                # event processing
                if (input == curses.KEY_RESIZE):
                        changeSize(stdscr)
                # Basic line editor
                if (input == curses.KEY_LEFT) and (inspoint>0):
                                inspoint-=1
                if (input == curses.KEY_RIGHT) and (inspoint<len(cmdline)):
                                inspoint+=1
                if (input == curses.KEY_BACKSPACE) and (inspoint>0):
                        cmdline=cmdline[:inspoint-1]+cmdline[inspoint:]
                        inspoint-=1
                if (input == curses.KEY_DC) and (inspoint<len(cmdline)):
                        cmdline=cmdline[:inspoint]+cmdline[inspoint+1:]
                if (input == curses.KEY_HOME):
                        inspoint=0
                if (input == curses.KEY_END):
                        inspoint=len(cmdline)
                #PgUp/PgDown
                if (input == curses.KEY_PPAGE):
                        pagepoint+=height-2
                        if len(chantext)-pagepoint<0:
                                pagepoint=len(chantext)
                if (input == curses.KEY_NPAGE):
                        pagepoint-=height-2
                        if pagepoint<0: pagepoint=0
                #History: TODO
                """
                if (input == curses.KEY_UP):
                if (input == curses.KEY_DOWN):
                """
                if (input == 10):
                        tosend=processLine(cmdline)
                        if len(tosend)>0:
                                msgs.append(tosend)
                        cmdline=""
                        inspoint=0

                # Ascii key
                if input>31 and input<128:
                        if len(cmdline)<(width-5):
                                cmdline=cmdline[:inspoint]+chr(input)+cmdline[inspoint:]
                                inspoint+=1
                redraw(stdscr)

# Client
# Init/deinit curses 
def Client(ServerOnionURL):
  global stdscr
  global STDOutLog 
  STDOutLog=False

  try:
      # Initialize curses
      stdscr=curses.initscr()
      curses.noecho()
      curses.cbreak()
      stdscr.keypad(1)
      # Enter the main loop
      clientMain(stdscr,ServerOnionURL)
      # Set everything back to normal
      stdscr.keypad(0)
      curses.echo()
      curses.nocbreak()
      # Terminate curses
      curses.endwin() 
      exit(0)
  except:
      # In event of error, restore terminal to sane state.
      stdscr.keypad(0)
      curses.echo()
      curses.nocbreak()
      curses.endwin()
        

# Main proc:
# Parse options, invoke Server or Client
if __name__=='__main__':
  parser = OptionParser()
  parser.add_option("-c", "--connect", action="store", type="string", dest="connect",      help="Acts as client, connect to server")
  parser.add_option("-s", "--server" , action="store", type="string", dest="channel_name", help="Acts as server")
        # no arguments->bail
  if len(sys.argv)==1:
        parser.print_help()
        exit(0)
  (options, args) = parser.parse_args()
  if options.channel_name:
        s=Server()
        s.serverMain(options.channel_name)
  else:
        if len(options.connect)>0:
                Client(options.connect)
        else: parser.print_help()
