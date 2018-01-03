#!/usr/bin/python 

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

import os

def myNetwork():

    net = Mininet( topo=None,
                    link = TCLink,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s19 = net.addSwitch('s19', cls=OVSKernelSwitch)
    s18 = net.addSwitch('s18', cls=OVSKernelSwitch)
    s20 = net.addSwitch('s20', cls=OVSKernelSwitch)
    s15 = net.addSwitch('s15', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s17 = net.addSwitch('s17', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)
    s16 = net.addSwitch('s16', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.1.2', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.1.3', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.1.0.2', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.1.0.3', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.1.2', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.1.3', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.2.0.2', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.2.0.3', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.1.2', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.1.3', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.3.0.2', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.3.0.3', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.1.2', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.1.3', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(s1, s5, 0, 0, bw=100)
    net.addLink(s1, s9, 1, 0, bw=100)
    net.addLink(s1, s13, 2, 0, bw=100)
    net.addLink(s1, s17, 3, 0, bw=100)

    net.addLink(s2, s5, 0, 1, bw=100)
    net.addLink(s2, s9, 1, 1, bw=100)
    net.addLink(s2, s13, 2, 1, bw=100)
    net.addLink(s2, s17, 3, 1, bw=100)

    net.addLink(s3, s6, 0, 0, bw=100)
    net.addLink(s3, s10, 1, 0, bw=100)
    net.addLink(s3, s14, 2, 0, bw=100)
    net.addLink(s3, s18, 3, 0, bw=100)

    net.addLink(s4, s6, 0, 1, bw=100)
    net.addLink(s4, s10, 1, 1, bw=100)
    net.addLink(s4, s14, 2, 1, bw=100)
    net.addLink(s4, s18, 3, 1, bw=100)

    net.addLink(s5, s7, 2, 0, bw=100)
    net.addLink(s5, s8, 3, 0, bw=100)

    net.addLink(s6, s7, 2, 1, bw=100)
    net.addLink(s6, s8, 3, 1, bw=100)

    net.addLink(s9, s11, 2, 0, bw=100)
    net.addLink(s9, s12, 3, 0, bw=100)
    net.addLink(s10, s11, 2, 1, bw=100)
    net.addLink(s10, s12, 3, 1, bw=100)
    net.addLink(s13, s15, 2, 0, bw=100)
    net.addLink(s13, s16, 3, 0, bw=100)
    net.addLink(s14, s15, 2, 1, bw=100)
    net.addLink(s14, s16, 3, 1, bw=100)
    net.addLink(s17, s19, 2, 0, bw=100)
    net.addLink(s17, s20, 3, 0, bw=100)
    net.addLink(s18, s19, 2, 1, bw=100)
    net.addLink(s18, s20, 3, 1, bw=100)
    
    net.addLink(s7, h1, 2, 0, bw=100)
    net.addLink(s7, h2, 3,  0, bw=100)
    net.addLink(s8, h3, 2,  0, bw=100)
    net.addLink(s8, h4, 3,  0, bw=100)
    net.addLink(s11, h5, 2,  0, bw=100)
    net.addLink(s11, h6, 3,  0, bw=100)
    net.addLink(s12, h7, 2,  0, bw=100)
    net.addLink(s12, h8, 3,  0, bw=100)
    net.addLink(s15, h9, 2,  0, bw=100)
    net.addLink(s15, h10, 3,  0, bw=100)
    net.addLink(s16, h11, 2,  0, bw=100)
    net.addLink(s16, h12, 3,  0, bw=100)
    net.addLink(s19, h13, 2,  0, bw=100)
    net.addLink(s19, h14, 3,  0, bw=100)
    net.addLink(s20, h15, 2,  0, bw=100)
    net.addLink(s20, h16, 3,  0, bw=100)


    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s14').start([c0])
    net.get('s1').start([c0])
    net.get('s4').start([c0])
    net.get('s2').start([c0])
    net.get('s19').start([c0])
    net.get('s18').start([c0])
    net.get('s20').start([c0])
    net.get('s15').start([c0])
    net.get('s11').start([c0])
    net.get('s6').start([c0])
    net.get('s17').start([c0])
    net.get('s10').start([c0])
    net.get('s12').start([c0])
    net.get('s5').start([c0])
    net.get('s8').start([c0])
    net.get('s7').start([c0])
    net.get('s9').start([c0])
    net.get('s13').start([c0])
    net.get('s16').start([c0])
    net.get('s3').start([c0])

    
    for i in range(20):
        cmd = "sudo ovs-vsctl set bridge %s protocols=OpenFlow13" % ("s"+str(i))
        os.system(cmd)


    c0.cmdPrint("sudo ifconfig s1 10.4.1.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s2 10.4.1.2 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s3 10.4.2.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s4 10.4.1.2 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s5 10.0.2.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s6 10.0.3.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s7 10.0.0.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s8 10.0.1.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s9 10.1.2.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s10 10.1.3.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s11 10.1.0.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s12 10.1.1.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s13 10.2.2.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s14 10.2.3.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s15 10.2.0.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s16 10.2.1.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s17 10.3.2.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s18 10.3.3.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s19 10.3.0.1 netmask 255.255.255.0")
    c0.cmdPrint("sudo ifconfig s20 10.3.1.1 netmask 255.255.255.0")


    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
