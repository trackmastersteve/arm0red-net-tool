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
  
