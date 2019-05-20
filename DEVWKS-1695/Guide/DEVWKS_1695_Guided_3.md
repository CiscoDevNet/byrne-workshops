# Module 2: Running Linux Apps and Utilities

#### Task 1 - Installing Linux Packages with YUM

Command:

```
sudo yum install -y iperf3
```

#### Task 2 - Network Testing with iPerf

Command:

```
iperf3 -c bouygues.iperf.fr -p 5201 -f K
```

#### Task 3 - Checking for Open Ports with nmap

Command:

```
sudo yum install -y nmap
```

Command:

```
nmap www.cisco.com
```

##### Task 4 - Working with File Structures

Command:

```
exit
```

Generate Some Text:

```
show tech | redirect bootflash:/showtech.txt
```

Command:

```
dir bootflash: | inc showtech.txt
guestshell run bash
```

Command:

```
ls -la /bootflash/showtech.txt
```

Command:

```
cat /bootflash/showtech.txt | grep PnP
```


## [Conintue to: Working with Python in GuestShell](DEVWKS_1695_Guided_4.md)

## [Return to the Table of Contents](../../README.md)