## Module 4 - Using EEM with GuestShell

#### Task 1 - Retrieving the Python Script

Command:

```
guestshell run wget https://raw.githubusercontent.com/CiscoDevNet/byrne-workshops/clus19/DEVWKS-1695/code/eem_script.py
```

#### Task 2 - Move the Python Script to an Reachable Path

Command:

```
guestshell run cp eem_script.py /bootflash/
```

Verify:

```
dir bootflash:eem_script.py
```

#### Task 3 - Configuring the EEM Script

Commands:

```
conf t
event manager applet interface_Shutdown
 event syslog pattern "Interface Loopback66, changed state to administratively down"
 action 0.0 cli command "en"
 action 1.0 cli command "guestshell run python /flash/eem_script.py Loopback66"	
 action 2.0 puts "$_cli_result"
!
end
!
wr mem
```

#### Task 4 - Generate the 'Down' Condition

Command:

```
term mon
conf t
logging monitor informational
int loop 66
shutdown
end
```

## [Moving On to the Wrap Up!](DEVWKS_1695_Guided_6.md)
## [Return to the Table of Contents](../../README.md)