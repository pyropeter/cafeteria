from scapy.all import *
# Useful stuff
import mitm
import sys

print "Skript gestartet..\n\n"


def handle_cl_args():
    for args in sys.argv:
	    if len(sys.argv) != 1:
	        if args == "-c":
	            show_config()
	        elif args == "-v":
	            show_version()
	        else:
	            do_nothing()
	    else:
	        no_args()


def show_config():
    print "Aktuelle Konfiguration:\n"
    print conf
    print "\n\n"
    

def show_version():
    print "Aktuelle Version:\n"
    print "0.1"
    print "\n\n"
    
def no_args():
    print "You need to enter some arguments...\n"
    
    
def do_nothing():
    print ""
    
    
handle_cl_args()