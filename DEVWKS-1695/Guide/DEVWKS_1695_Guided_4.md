## Module 3 - Working with Python in GuestShell

#### Task 1 - Opening the Python Interpreter

Command:

```
python
```

#### Task 2 - Using the Interactive Interpreter

```
x = "Hello World!"
print (x)
```

#### Task 3 - Built-in Python API

Command:

```
import cli
```

Command:

```
cli.clip("show ip int brief")
```

#### Task 4 - Creating an Interface with the Python API

```
cli.cli("conf t; int loop 66; ip address 192.168.166.1 255.255.255.255")

cli.clip("show ip int brief")
```

#### Task 5 - Exiting the Interpreter and Return to Router Prompt

```
exit ()
exit

```

## [Conintue to: Using EEM with GuestShell](DEVWKS_1695_Guided_5.md)

## [Return to the Table of Contents](../../README.md)