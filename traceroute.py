from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1
import Constants
import ping



def trace(target):
    """
    :param target: Target url/ip to be traced
    :return: trace output for gui
    """

    _, dest_ip = ping.ping(target)
    output = []
    for _ttl in range(1, Constants.MAX_TTL):

        # Create and send ICMP Packets
        packet = IP(dst=target, ttl=_ttl) / ICMP()
        reply = sr1(packet, verbose=0)

        # If reply is empty
        if reply is None:
            continue

        # Special Print for destination
        if reply.src in dest_ip:
            output.append("Hop {0}: at {1}\n".format(_ttl, reply.src))
            output.append("-----------------------------------------\n")
            output.append("Reached {0} in {1} hops\n".format(target, _ttl))
            break

        # Print Log
        else:
            output.append("Hop {0}: at {1}\n".format(_ttl, reply.src))

    return ''.join(output)