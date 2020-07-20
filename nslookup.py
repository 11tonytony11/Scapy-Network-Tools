from scapy.layers.dns import DNSQR, DNS, UDP, IP, DNSRR
from scapy.sendrecv import sr1
from scapy.volatile import RandShort

import Constants


def nslookup(url):
    """
    :param url: Target Website
    :return: string to be shown on screen
    """
    output = []
    # Creating and sending DNS query
    ans = sr1(IP(dst=Constants.DNS_IP) / UDP(sport=RandShort(), dport=Constants.DNS_PORT) /
              DNS(rd=1, qd=DNSQR(qname=url, qtype=Constants.RECORD_TYPE)), verbose=0)

    # Creating and returning list of resolved ips
    for idx in range(ans[DNS].ancount):
        if Constants.RECORD_TYPE == "A":
            output.append(ans[DNSRR][idx].rdata)
        else:
            output.append(ans.an[0][idx].exchange.decode())

    return "found {0} {1} Record(s):\n{2}\n".format(len(output), Constants.RECORD_TYPE, '\n'.join(output))
