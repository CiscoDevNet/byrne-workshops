# byrne-workshops
This repository contains lab tasts and code in support of two Cisco Live DevNet Workshops.

DEVWKS-2561 - Hands on Exploration of NETCONF and YANG 

DEVWKS-2585 - Hands on Kicking the Tires of RESTCONF

The individual sessions can be found in their respective sub directory. If you'd like to run the labs on your the Makefile will build your enviornment. The labs can be launched with

```
make start-2561
```
or 

```
make start-2585
```

The make files will attempt to bring up a vagrant image (not included in the repository), configure the router, and launch the Lab Guide.
