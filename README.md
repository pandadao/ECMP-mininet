# Assignment 2 

Completed the A, B, C questions, using mininet script generating a fat tree topology.

![alt tag](https://github.com/pandadao/ECMP-mininet/blob/master/fattree-topology.PNG)

## pre requirement of environment:
Ubuntu 14.04 with mininet and ryu controller.

## How to use:
```shell
		$ git clone https://github.com/pandadao/ECMP-mininet.git
		$ cd ECMP-mininet 
		$ ryu-manager --observe-link ryu.app.simple_switch_13
```
`After you open the ryu controller, you can see the following information like the picture:`
![alt tag](https://github.com/pandadao/ECMP-mininet/blob/master/ryu-controller-information.png)


### next steps:

Open a newterminal and type the following instruction:
```shell
		$ sudo python my-fattree.py 
```

And you will see the mininet create fat tree with k=4 topology information like the pictures:

![alt tag](https://github.com/pandadao/ECMP-mininet/blob/master/mininet-running.png)
![alt tag](https://github.com/pandadao/ECMP-mininet/blob/master/mininet-links.png)



### This project didn't complete.
