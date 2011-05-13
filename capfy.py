from scapy.all import *
# Useful stuff
import mitm, sys, random


jetzig = ["Current","Actual","Latest","Prevailing","Up-to-date"]

print "Script started...\n\n"


def handleCLargs():
    for arg in sys.argv:
        if len(sys.argv) != 1:
            if arg == "-c":
                showConfig()
            elif arg == "-v":
                showVersion()
            else:
                doNothing()
        else:
            noArgs()


def showConfig():
    print j()+" configuration:\n"
    print conf
    print "\n\n"
    

def showVersion():
    print j()+" version:\n"
    print "0.1"
    print "\n\n"
    
def noArgs():
    print "You need to enter some arguments...\n"
    print "Available arguments:"
    print "-c - Shows your current configuration"
    print "-v - Shows current version\n"
    
    
def doNothing():
    print ""
    
def j():
    return jetzig[random.randint(0,4)]
    

handleCLargs()


# vim:set ts=4 sw=4 et: