# FatTree
Mininet Fattree topology (two stage)

## To run
Move to the directory where 'fattree.py' is located. The topology is created according to the number of ports in the switch devices. The number of switches and topology is adjusted according to the number of ports. 
To create a two-stage fattree topology using 4 port switches:
```
sudo mn --custom ./fattree.py --topo fattree,4 --controller remote
```
