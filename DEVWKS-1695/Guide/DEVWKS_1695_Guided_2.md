# Module 1: Enabling GuestShell

#### Task 1 - Enabling IOX

Configuraiton:

```
conf t
iox
end
```

Verify:

```
show iox-service
```

#### Task 2 - Configuring GuestShell

Configuraiton:

```
conf t
app-hosting appid guestshell
 app-vnic gateway0 virtualportgroup 0 guest-interface 0
  guest-ipaddress 192.168.35.2 netmask 255.255.255.0
 app-default-gateway 192.168.35.1 guest-interface 0
 app-resource profile custom
  cpu 1500
  memory 512
 name-server0 208.67.222.222
 end
``` 

Command:

```
guestshell enable
```

Verify:

```
show app-hosting detail
```

#### Task 3 - Executing Commands in GuestShell

Command:

```
guestshell run hostnamectl
```

Command:

```
guestshell run pwd
```

Command:

```
guestshell run bash
```

Task 4 - Executing Commands from GuestShell to IOS-XE

Command:

```
dohost 'show interfaces | inc protocol | address | Duplex | rate'
```


## [Conintue to: Running Linux Apps and Utilities](DEVWKS_1695_Guided_3.md)

## [Return to the Table of Contents](../../README.md)