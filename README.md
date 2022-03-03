# FatTree
Mininet Fattree topology (two stage)

The original Fat-Tree explanation in [Sigcomm'08 : A Scalable, Commodity Data Center Network Architecture](http://ccr.sigcomm.org/online/files/p63-alfares.pdf).

## To run
Move to the directory where 'fattree.py' is located. The topology is created according to the number of ports in the switch devices. The number of switches and topology is adjusted according to the number of ports. 
To create a two-stage fattree topology using 4 port switches:
```
sudo mn --custom ./fattree.py --topo fattree,4 --controller remote
```
