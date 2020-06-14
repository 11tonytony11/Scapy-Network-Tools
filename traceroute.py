from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
import Constants
import ping



def trace(target):
    """
    :param target: Target url/ip to be traced
    :return: None
    """

    _, dest_ip = ping.ping(target)
    for _ttl in range(1, Constants.MAX_TTL):

        # Create and send ICMP Packets
        packet = IP(dst=target, ttl=_ttl) / ICMP()
        reply = sr1(packet, verbose=0)

        # If reply is empty
        if reply is None:
            continue

        # Special Print for destination
        if reply.src in dest_ip:
            print("Hop {0}: at {1}".format(_ttl, reply.src))
            print("-----------------------------------------")
            print ("Reached {0} in {1} hops".format(target, _ttl))
            break

        # Print Log
        else:
            print("Hop {0}: at {1}".format(_ttl, reply.src))

trace("ynet.co.il")
