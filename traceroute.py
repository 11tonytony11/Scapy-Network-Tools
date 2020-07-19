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

        latency = round((reply.time - packet.sent_time) * 1000 - Constants.LATENCY_OFFSET)
        # Special Print for destination
        if reply.src in dest_ip:
            tmp = "Hop {0}: at {1} {3} Response Time: {2}\n".format(_ttl, reply.src, latency, "X")
            output.append(tmp.replace("X", " " * (45 - len(tmp))))
            output.append("-----------------------------------------\n")
            tmp = "Reached {0} in {1} hops {3} Response Time: {2}\n".format(target, _ttl, latency, "X")
            output.append(tmp.replace("X", " " * (45 - len(tmp))))
            break

        # Print Log
        else:
            tmp = "Hop {0}: at {1} {3} Response Time: {2}\n".format(_ttl, reply.src, latency, "X")
            output.append(tmp.replace("X", " " * (45 - len(tmp))))

    return ''.join(output)