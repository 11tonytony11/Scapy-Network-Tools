from scapy.layers.inet import ICMP, IP
from scapy.sendrecv import sr1
import Constants

def ping(target, iterations = 1):
    """
    :param target: Target Website/ip
    :return: output string for gui, target server
    """
    latency_record = []
    for i in range (iterations):
        packet = IP(dst=target) / ICMP()
        ans = sr1(packet, verbose=0)

        # Prepare output for gui
        latency = round((ans.time - packet.sent_time) * 1000 - Constants.LATENCY_OFFSET)  # Scapy latency is 40ms higher than real in my PC
        latency_record.append("Got answer from: {0} in {1} ms\n".format(ans.src, latency))

    return ''.join(latency_record), ans.src