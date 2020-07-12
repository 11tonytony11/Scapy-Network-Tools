from scapy.layers.dns import DNSQR, DNS, UDP, IP, DNSRR
from scapy.sendrecv import sr1
import Constants


def nslookup(url, record_type = "A"):
    """
    :param url: Target Website
    :param record_type: DNS Record type
    :return: string to be shown on screen
    """

    output = []
    try:
        # Creating and sending DNS query
        ans = sr1(IP(dst = Constants.DNS_IP) / UDP(dport = Constants.DNS_PORT) / DNS(rd = 1, qd = DNSQR(qname=url, qtype=record_type)), verbose=0)

        # Creating and returning list of resolved ips
        for idx in range(ans[DNS].ancount):
            output.append(ans[DNSRR][idx].rdata)

    except Exception as e:
        print("Error! could not find IP addres, don\'t forget to run as admin")

    return "found {0} {1} Record(s):\n{2}".format(len(output),record_type, '\n'.join(output))