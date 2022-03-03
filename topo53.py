"""Custom topology example

   Fig53 in slides

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        switchA = self.addSwitch( 's1' )
        switchB = self.addSwitch( 's2' )
        switchC = self.addSwitch( 's3' )
        switchD = self.addSwitch( 's4' )
        switchE = self.addSwitch( 's5' )

        # Add links
        self.addLink( leftHost, switchA )
        self.addLink( rightHost, switchD )
        self.addLink( switchA, switchB )
        self.addLink( switchA, switchC )
        self.addLink( switchB, switchD )
        self.addLink( switchB, switchE )
        self.addLink( switchC, switchD )
        self.addLink( switchC, switchE )
        self.addLink( switchD, switchE )


topos = { 'mytopo': ( lambda: MyTopo() ) }
