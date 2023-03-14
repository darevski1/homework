#### Exercise 1 – Basic network stuff


* **Easy Use the arp command and paste the output from the arp table on your system:**
  
  arp  - stands for Address resolution protocol is used to resolve ip address to to MAC addresess. MAC address is physical address of a device. Whenever a device needs to comunicate with another device on a local area network it needs MAC address for that device. arp stores MAC addreses in his local cache ARP cache. ARP Table is used to keep the record of the IP address and MAC address of the devices source and destination device for the communication between two devices

    ds@ds-HP-ProBook-440-G6:~$ arp -a

    ? (192.168.100.236) at 00:21:b7:2f:bf:4f [ether] on enp2s0 <br />
    ? (192.168.100.149) at 00:21:b7:7e:d1:11 [ether] on enp2s0 <br />
    ? (192.168.100.137) at 00:21:b7:d5:f2:e1 [ether] on enp2s0 <br />
    ? (192.168.100.141) at 00:21:b7:d5:f2:b1 [ether] on enp2s0 <br />
    70-100-168-192.dsl1-erie.roc.ny.frontiernet.net (192.168.100.70) at 58:20:b1:4e:bc:23 [ether] on enp2s0 <br />
    ? (192.168.100.231) at e0:70:ea:f9:2c:10 [ether] on enp2s0 <br />
    node-81s.pool-1-1.dynamic.totinternet.net (192.168.1.1) at 00:1f:33:28:81:80 [ether] on wlp0s20f3 <br />
    ? (192.168.100.147) at 00:21:b7:e5:37:ce [ether] on enp2s0 <br />
    ? (192.168.100.1) at 04:76:b0:26:5a:74 [ether] on enp2s0 <br />
    nothing.attdns.com (192.168.100.135) at e0:70:ea:f9:2c:5a [ether] on enp2s0 <br />
    ? (192.168.100.44) at e0:70:ea:f9:2c:b4 [ether] on enp2s0 <br />
    ETH-240-ML3471ND.kultur.uni-hamburg.de (192.168.100.134) at 00:21:b7:d5:f6:c6 [ether] on enp2s0 <br />


* **Use the route command and paste the output from the routing table on your system:** 
* **Use the traceroute command on your system and observe the hops to Google’s DNS, 8.8.8.8** 
  
  - traceroot is command line 

* **Paste the full output from the command bellow showing all the hops from your system to 8.8.8.8** 