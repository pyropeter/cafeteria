from scapy.all import *
# Useful stuff
import mitm
import sys

print "Skript gestartet..\n\n"


def handleCLargs():
    for args in sys.argv:
        if len(sys.argv) != 1:
            if args == "-c":
                showConfig()
            elif args == "-v":
                showVersion()
            else:
                doNothing()
        else:
            noArgs()


def showConfig():
    print "Aktuelle Konfiguration:\n"
    print conf
    print "\n\n"
    

def showVersion():
    print "Aktuelle Version:\n"
    print "0.1"
    print "\n\n"
    
def noArgs():
    print "You need to enter some arguments...\n"
    
    
def doNothing():
    print ""
    
    
handleCLargs()


# vim:set ts=4 sw=4 et: