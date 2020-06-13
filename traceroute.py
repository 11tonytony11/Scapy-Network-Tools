from scapy.layers.inet import UDP, IP
from scapy.sendrecv import sr1
import Constants
import nslookup


def trace(target):
    """
    :param target: Target url/ip to be traced
    :return: None
    """

    dest_ip = nslookup.nslookup(target)

    for _ttl in range(Constants.MAX_TTL):

        # Create and send ICMP Packets
        packet = IP(dst=target, ttl=_ttl) / UDP(dport=Constants.TRACE_PORT)
        reply = sr1(packet, verbose=0)

        # Special Print for destination
        if reply.src in dest_ip:
            print("Hop {0}: at {1}".format(_ttl, reply.src))
            print("-----------------------------------------")
            print ("Reached {0} in {1} hops".format(target, _ttl))
            break

        # Print Log
        else:
            print("Hop {0}: at {1}".format(_ttl, reply.src))

trace("tech-il.co.il")