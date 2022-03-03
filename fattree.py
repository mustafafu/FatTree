from mininet.topo import Topo
import logging
import os


logging.basicConfig(filename='./fattree.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

class FatTree(Topo):
    # Let's assume we have N port switches for a two stage fat tree network.
    # We will have N edge switches, and N/2 core switches.
    #     CS_1 CS_2 ... CS_{N/2}
    #     |\ \ \ | \ \ \
    #     ES_1 ES_2 ... ES_{N}
    # Each edge switch is connected to each core switch.
    # Each edge switch is then connected to N/2 hosts

    def __init__( self, N):
        " Create Fat Tree topo."
        self.CoreSwitchList = []
        self.EdgeSwitchList = []
        self.HostList = []
        self.portCount = N
        self.CoreSwitchCount = self.portCount/2                  # N/2
        self.EdgeSwitchCount = self.portCount                    # N
        self.HostCount = self.portCount/2 * self.EdgeSwitchCount # N*N/2

        # Init Topo
        Topo.__init__(self) #using mininet inheritance directly
  
        self.createTopo()
        logger.debug("Finished topology creation!")

        self.createLinks()

        logger.debug("Finished adding links!")

    


    """
    Create Switch and Hosts
    """

    def createTopo(self):
        self.createCoreLayerSwitch(self.CoreSwitchCount)
        self.createEdgeLayerSwitch(self.EdgeSwitchCount)
        self.createHost(self.HostCount)

    def createCoreLayerSwitch(self, NUMBER):
        logger.debug("Create Core Layer")
        for swIdx in range(1,NUMBER+1):
            switchString = '{}{}{:03d}'.format('c','s',swIdx)
            logger.debug('...\t'+ switchString)
            self.CoreSwitchList.append(self.addSwitch(switchString))

    def createEdgeLayerSwitch(self, NUMBER):
        logger.debug("Create Edge Layer")
        for swIdx in range(1,NUMBER+1):
            switchString = '{}{}{:03d}'.format('e','s',swIdx)
            logger.debug('...\t'+ switchString)
            self.EdgeSwitchList.append(self.addSwitch(switchString))

    def createHost(self, NUMBER):
        logger.debug("Create Host")
        for hostIdx in range(1,NUMBER+1):
            hostString = '{}{:03d}'.format('h',hostIdx)
            logger.debug('...\t'+ hostString)
            self.HostList.append(self.addHost(hostString))

    """
    Add Link
    """
    def createLinks(self):
        logger.debug("Add link Core to Agg.")
        for coreSwitchIdx, coreSwitch in enumerate(self.CoreSwitchList):
            for edgeSwitchIdx,edgeSwich in enumerate(self.EdgeSwitchList):
                # here if we are connecting core switch i to edge switch j, its a fully bipartite network in two stage fat tree
                logString = 'Creating link from Core Switch {}, to Edge Switch {}'.format(coreSwitchIdx+1,edgeSwitchIdx+1)
                logger.debug('...\t'+ logString)
                self.addLink(coreSwitch,edgeSwich)  
        # Creating Edge switch to Host links
        hostIdx = 0
        for edgeSwitchIdx,edgeSwich in enumerate(self.EdgeSwitchList):
            for switchHostIdx in range(0,self.portCount/2): #ports/2 hosts per switch
                # here if we are connecting edge switch i to hosts 0.5*self.portCount*(i-1)+1 to 0.5*self.portCount*(i)
                logString = 'Creating link from Edge Switch {}, to Host {}'.format(coreSwitchIdx+1, hostIdx+1)
                logger.debug('...\t'+ logString)
                self.addLink(edgeSwich,self.HostList[hostIdx])
                hostIdx = hostIdx + 1

        


# This is for "mn --custom"
topos = { 'fattree' : ( lambda k : FatTree(k))}
