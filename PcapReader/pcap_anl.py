# http://dpkt.readthedocs.io/en/latest/_modules/examples/print_packets.html 참고
import dpkt
import datetime
import socket
from dpkt.compat import compat_ord

def mac_addr(address):

    return ':'.join('%02x' % compat_ord(b) for b in address)

def packets(pcapfile):
    for timestamp, buf in pcapfile:
        print ('시간: ',str(datetime.datetime.utcfromtimestamp(timestamp)))

        eth = dpkt.ethernet.Ethernet(buf)
        print('맥 어드레스: ',mac_addr(eth.src), mac_addr(eth.dst), eth.type)

        ip  = eth.data
        print('IP: 출발지: %s -> 목적지: %s len=%d \n' % (socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst), ip.len))

def start():
    with open('example1.pcap', 'rb') as file:
        pcapfile = dpkt.pcap.Reader(file)
        packets(pcapfile)

if __name__ == '__main__':
    start()
