#!/usr/bin/env python

"""
Create a 1024-host network, and run the CLI on it.
If this fails because of kernel limits, you may have
to adjust them, e.g. by adding entries to /etc/sysctl.conf
and running sysctl -p. Check util/sysctl_addon.
"""

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import OVSSwitch
from mininet.topolib import TreeNet
from mininet.examples.treeping64 import HostV4

setLogLevel('info')
network = TreeNet(depth=2, fanout=2, host=HostV4,
                  switch=OVSSwitch, waitConnected=True)
network.run(CLI, network)
