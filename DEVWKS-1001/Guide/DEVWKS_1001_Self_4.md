## YANG Lab Exercises

**Before we get started** - It's important to note that YANG Models are broken into two categories. The first, called Standard Models, are created by standards bodies (IETF, IEEE, OpenConfig) and are meant to address multi-vendor environments. The second, called Native Models, are created by individual network vendors. The purpose of a Native Model is to extend additional data models not provided by the Standards bodies.

**Before we get started 2** - Make sure to enter into the correct lab directory.

```
cd DEVWKS-1001/code
```


#### Task 1 - Open a YANG Model

In this exercise we will view the contents of a YANG model downloaded from the [YANG Model](https://github.com/YANGModels/Yang) git repository.

Let's take a look at the YANG file.

Type or Paste:

```
cat ietf-interfaces.yang
```

First it's important to note that the documentation for the model is the model itself. Every detail an operator would need to understand what the model represents is contained within. While this is helpful in getting an understanding it's a little cumbersome if a developer wanted to quickly view relevant details.

To do that we need to look at a tool like **pyang**

#### Take 2 - Using pyang to Explore a Standard YANG Model

Pyang is a Python based YANG validator. It can be used to quickly display a YANG model allowing a developer to quickly asses what's available in a YANG model. Let's take a look.

Type or Paste:

```
pyang -f tree ietf-interfaces.yang
```


We are going to step through the relevant components using a sample output edited for brevity.

```
module: ietf-interfaces
  +--rw interfaces
  |  +--rw interface* [name]
  |     +--rw name                        string
  |     +--rw description?                string
  |     +--rw type                        identityref
  |     +--rw enabled?                    boolean
  |     +--rw link-up-down-trap-enable?   enumeration {if-mib}?
  +--ro interfaces-state
     +--ro interface* [name]
        +--ro name               string
        +--ro type               identityref
        +--ro admin-status       enumeration {if-mib}?
        +--ro oper-status        enumeration
        +--ro last-change?       yang:date-and-time
        +--ro if-index           int32 {if-mib}?
        +--ro phys-address?      yang:phys-address
        +--ro higher-layer-if*   interface-state-ref
        +--ro lower-layer-if*    interface-state-ref
        +--ro speed?             yang:gauge64
        +--ro statistics
```

In this example we are looking at the IETF YANG representation of an interface. We know this as the YANG model tells us directly on the first line :).

Working our way down the tree we see our first YANG construct a **container**

-   +--rw interfaces
-   +--ro interfaces-state

A container is a grouping of similar configuration or operational data. How do we know? The model tells us by using:

- rw - for configuration (read write)
- ro - for operational (read only)

This is equivalent to configuration mode (interfaces container) and exec mode (interfaces-state container).

Within each container is our next construct the **list**. A list is an index of data sets contained in the container. In our example the container would contain a list of interfaces present on the platform. If we were to look at actual YANG data (we will in an upcoming exercise) we would see multiple interfaces under the two containers.

We can identify individual list entires by the **key value** represented by the **[name]** field in the model. Again, if we were looking at real YANG data the key value would be GigabitEthernet 0, GigabitEthernet 1, etc.

Under our list entries are called **leaf values**. A leaf is an individual piece of modeled in YANG. Looking at the configuration data we see 5 leaf values.

- name
- description?
- type
- enabled?
- link-up-down-trap-enable?

By default all leaf values must be included unless specifically defined as optional. An optional field is identified by a **?** at the end of the leaf value name. Consider this in terms of configuring an interface via the CLI. To configure the interface you must explicitly enter the interface mode by specifying the type (Ethernet) and the name (GigabitEthernet0) but you don't have to include a description as part of the configuration.

Finally, the second column defines the type of data that the model expects. For something like a description the model expects a string but for the enabled leaf an operator must send a boolean. If you were to configure an interface and send any other value than true or false for the enabled leaf the action would generate an error and would not process.

#### Task 3 - Viewing a Native YANG Model

In this example I am just representing that a Cisco Native model will can be viewed in the same format as the Standard Model. Take a look.

Type or Paste:

```
pyang -f tree cisco-platform-software.yang
```

With that let's move on to NETCONF!

## [Introduction to NETCONF](DEVWKS_1001_Self_5.md)
## [Return to the Table of Contents](../../README.md)