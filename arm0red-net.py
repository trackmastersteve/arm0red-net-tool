import sys
import socket
import getopt
import threading
import subprocess


# define some global variables
listen              = False
command             = False
upload              = False
execute             = ""
target              = ""
upload_destination  = ""
port                = 0


def usage():
  print "arm0red Net Tool"
  print
  print "Usage: arm0red-net.py -t target_host -p port"
  print "-l --listen                    - listen on [host]:[port] for incoming connections"
  print "-e --execute=file_to_run       - execute the given file upon receiving a connection"
  print "-c --command                   - initialize a command shell"
  print "-u --upload=destination        - upon receiving connaction upload a file and write to destination"
  print
  print
  print "Examples: "
  print "arm0red-net.py -t 192.168.1.1 -p 5555 -l -c"
  print "arm0red-net.py -t 192.168.1.1 -p 5555 -l -u=c:\\target.exe"
  print "arm0red-net.py -t 192.168.1.1 -p 5555 -l -e=\"cat /etc/passwd\""
  print "echo 'ABCDEFGHI' | ./arm0red-net.py -t 192.168.1.23 -p 135"
  sys.exit(0)

  def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
    
    if not len(sys.argv[1:]):
      usage()
      
    # read the command line options
    try:
      opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:", ["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
      print str(err)
      usage()

    for o,a in opts:
      if o in ("-h","--help"):
        usage()
      elif o in ("-l","--listen"):
        listen = True
      elif o in ("-e","--execute"):
        execute = a
      elif o in ("-c","--commandshell"):
        command True
      elif o in ("-u","--upload"):
        upload_destination = a
        
