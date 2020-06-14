from scapy.layers.inet import ICMP, IP
from scapy.sendrecv import sr1
import Constants

def ping(target):
    """
    :param target: Target Website/ip
    :return: List of ip addresses
    """

    packet = IP(dst=target) / ICMP()
    ans = sr1(packet, verbose=0)

    latency = ans.time - packet.sent_time
    latency = (latency * 1000) - Constants.LATENCY_OFFSET

    return latency, ans.src  # Scapy latency is 40ms higher than real in my PC