## Module 1: Exploring YANG Models

#### Task 1 - Open a YANG Model

```
cat ietf-interfaces.yang
```
#### Task 2 - Viewing a Standard YANG Model as a Tree

```
pyang -f tree ietf-interfaces.yang
```
#### Task 3 - Viewing a Native YANG Model as a Tree

```
pyang -f tree cisco-platform-software.yang 
```

## Module 2: Working with NETCONF

#### Task 0 - Generate Traffic for Counters
```
python generate_traffic.py &
```

#### Task 1 - Retrieving Device Configuraiton with NETCONF
```
python nc_get-config_full.py
```

#### Task 2 - Retrieving Specific Configuraiton Details with NETCONF
```
python nc_get-config_int.py
```

#### Task 3 - Retrieving Operational Details with NETCONF

```
python nc_get_nat.py
```
#### Task 4 - Retrieving A Specific XPATH

```
python generate_traffic_xpath.py &
python nc_xpath_nat.py
```


## [Moving on the Wrap Up!](DEVWKS_1001_Guided_3.md)

## [Return to the Table of Contents](../../README.md)

