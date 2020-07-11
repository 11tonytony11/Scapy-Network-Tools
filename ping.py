from scapy.layers.inet import ICMP, IP
from scapy.sendrecv import sr1
import Constants

def ping(target, iterations = 1):
    """
    :param target: Target Website/ip
    :return: List of ip addresses
    """
    latency_record = []
    for i in range (iterations):
        packet = IP(dst=target) / ICMP()
        ans = sr1(packet, verbose=0)

        latency_record.append(round((ans.time - packet.sent_time) * 1000 - Constants.LATENCY_OFFSET))

    return latency_record, ans.src  # Scapy latency is 40ms higher than real in my PC