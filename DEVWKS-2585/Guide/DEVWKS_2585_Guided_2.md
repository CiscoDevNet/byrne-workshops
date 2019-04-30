## Module 1: Crafting the RESTCONF URI

#### Task 1 - Viewing a YANG Model
```
pyang -f tree ietf-interfaces.yang
```
#### Task 2 - Using cURL to Craft a RESTCONF Call
```
curl -k -u vagrant:vagrant \
  https://127.0.0.1:2225/restconf/data/Cisco-IOS-XE-native:native/hostname \
  -H 'Accept: application/yang-data+json' \
  -H 'Content-Type: application/yang-data+json' \
```
#### Task 3 - Changing the Encoding to XML

```
curl -k -u vagrant:vagrant \
  https://127.0.0.1:2225/restconf/data/Cisco-IOS-XE-native:native/hostname \
  -H 'Accept: application/yang-data+xml' \
  -H 'Content-Type: application/yang-data+xml' \
```


## [Moving on to Module 2](DEVWKS_2585_Guided_3.md)
## [Return to the Table of Contents](../../README.md)

