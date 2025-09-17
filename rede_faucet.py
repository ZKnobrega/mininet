#!/usr/bin/python3
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_net():
    net = Mininet(controller=RemoteController('c0', ip='127.0.0.1', port=6653), waitConnected=True)
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    s1 = net.addSwitch('s1', dpid='0000000000000001') # DPID deve ser 0x1
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_net()
