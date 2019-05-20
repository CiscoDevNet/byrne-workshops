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
#### Task 4 - Viewing YANG Formatted Data
```
python yang_data_output.py
```

## Module 2: Working with NETCONF

#### Task 0 - Generate Traffic for Counters
```
python generate_traffic.py
```

#### Task 1 - Saying Hello with NETCONF
```
python nc_capabilities.py
```

#### Task 2 - Retreiving Device Configuraiton with NETCONF
```
python nc_get-config_full.py
```

#### Task 3 - Retreiving Specific Configuraiton Details with NETCONF
```
python nc_get-config_int.py
```

#### Task 4 - Retreiving Operational Details wiht NETCONF

```
python nc_get_nat.py
```
#### Task 5 - Retreiving A Specific XPATH

```
python generate_traffic_xpath.py &
python nc_xpath_nat.py
```

#### Task 6 - Modifying the Hostname with NETCONF

```
python nc_edit_hostname.py
python nc_verify_hostname.py
```

## [Moving on the Wrap Up!](DEVWKS_1001_Guided_3.md)

## [Return to the Table of Contents](../../README.md)

