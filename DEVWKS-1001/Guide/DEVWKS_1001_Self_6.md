## Working with NETCONF

#### Task 0 - Generate Traffic for Counters.

Before we start the lab we need to generate some counters interface counters so we have some data to work with. While not a requirement looking at interface counters as a 0 isn't overly exciting :).

Type or Paste:

```
python generate_traffic.py &
```

#### Task 1 - Retrieving Device Configuration with NETCONF

We are using this example for two purposes. The first this will give us an opportunity to look at device data modeled in YANG. The second we will be looking at the actual code to see how we can use ncclient, a python NETCONF client, for sending and receiving YANG data on a network device. Before we execute the code let's take a look at a couple of things within the code.

Type or Paste:

```
cat python nc_get-config_full.py
```
First let's look at the libraries we are working with:

- **from ncclient import manager** - As stated previously ncclient is a python NETCONF client. It is used in code to establish a NETCONF session and execute one of the documented actions. We are specifically working with the manager function.
- import xml.dom.minidom - In our code we are using xml.dom.minidom to process xml in a more 'readable' format. 

Next let's take a look at the variables we are defining

- HOST - this is the IP address of the network device. This is typically a loopback interface on a device. In our case we are sending the traffic to the hypervisor running on our laptop (Vagrant).
- Port - By default NETCONF uses TCP port 830. Again we are using a high port number as the virtual router is running in a hypervisor on our laptop.
- USER/PASS - Used for session establishment.

Finally let's take a look at what's happening in the main portion of the code. We will use this block of code in every example so it's important that we understand what's happening.

```
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:
```

In this block we are defining our session parameters and assigning it to the variable of m. When called we will establish a session with the defined variables. We can then use these session details to execute multiple NETCONF actions. Any of the values not defined as a variable are essentially mandatory values. In particular the option for look_for_keys allows the session to establish if you haven't previously retrieved a device's key.

Finally let's get to the NETCONF! Let's look at the line:

results = m.get_config('running')

In this statement the code will establish a connection to the router using the session details we defined in the with statement (assigned to the value of m) and we will send the NETCONF action 'get_config' targeted at the running data store. The router will respond with an XML payload providing the full YANG modeled configuration formatted in XML.

The output is massive. Let's look at a few details.

Type or Paste:

```
python nc_get-config_full.py
```

Scroll back to the top of the output and locate the first two lines 

```
<rpc-reply message-id="urn:uuid:02bd67dd-d127-42e3-9c6f-4b668e004f74" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
	<data>
		<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
```

There are three important pieces of information here. 

- First the line that reads rpc-reply with a long identifier. This message-id is used to re-assemble NETCONF messaging that may be spread across multiple packets. 
- Second the line that reads 'data'. Everything past this point is no longer part of the NETCONF communication. This is YANG data modeled in XML.
- Third the line that starts with native xmlns is used to identify the YANG model represented in the next portion of the output. Everything under this XML key is from the Cisco-IOS-XE-native YANG model.

Now let's look at the bottom of the output. If we scroll up a bit from the bottom we will see the interface configuration as represented by the ietf-interfaces YANG model. As a hint look for 'interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"'

While this output is interesting it's probably more detail than we need. Let's look at how we can filter some of the data.

#### Task 2 - Retrieving Specific Configuration Details with NETCONF

In this example we will be supplying the NETCONF get_config action with a filter. Specifically we will be retrieving the configuration of GigabitEthernet2. The filter will be applied by the remote device's agent process to only return the portion of the YANG model we are interested in.

Let's take a look at the code

```
cat nc_get-config_int.py
```

So let's talk about what's new in this code. First we are including a new Python library.

- xmltodict - This Python library takes XML and converts it to a dictionary. We will use the key value pairs to pull out the data and report it back in a more readable format.

Next we have the variable defined at FILTER. This XML structure represents the portion of the YANG model we want to have returned. Specifically we want the GigabitEthernet2 index from the interface container that's part of the ietf-interfaces YANG model.

Now let's look at our NETCONF request

```
results = m.get_config('running', FILTER)
```

With this code we will be using our session details (explained in the previous example) to send a NETCONF get_config. The target will be the running data store. With the get_config action we will pass the XML filter to the agent process. The network device will process the request and return the data matching the XML filter.

Let's take a look:

Type or Paste:

```
python nc_get-config_int.py
```
The output is broken into two parts. The first is the raw XML output as parsed by xml.dom.minidom. What's more interesting is to look at the formatted output from xmltodict.

```
*******************************************************
Interface Details:
  Name: GigabitEthernet2
  Description: This is Interface 2
  Type: ianaift:ethernetCsmacd
  Enabled: true
*******************************************************
```
As you can see we've pulled the YANG leaf values from GigabitEthernet 2 and presented the details in a more consumable format.

Let's move on to looking at opertional data.

#### Task 3 - Retrieving Operational Details with NETCONF

In this example we will be using the NETCONF action 'get' to retrieve both the configuration of an ACL as well at the number of matches on each ACE.

Let's look at the code

```
cat nc_get_nat.py
```

In keeping with the theme of discussing what we added let's hit the highlights.

First if we look at the FILTER variable notice that we are using two different YANG models. This speaks back to the idea that a YANG container either has configuraiton or operational data. 

Next let's look at our NETCONF request

```
results = m.get(FILTER)
```
Keep in mind that when sending a 'get' action it must be exectued against the running data store. Hence the fact we don't need to specify it as part of the NETCONF action.

The rest of the code is just parsing out the details as supplied by xmltodict.

Let's look at the formatted output:

```
Access-List Name: CISCO_LIVE_IN
 For ACE: 10
  Protocol: icmp
   Host IP: 8.8.0.0
   Wildcard Mask: 0.0.255.255
   Action: deny
 For ACE: 20
  Protocol: icmp
   Host IP: 208.67.0.0
   Wildcard Mask: 0.0.255.255
   Action: permit
 For ACE: 30
  Protocol: ip
   Action: permit
 For SEQ number: 10 the number of ACE matches is: 0
 For SEQ number: 20 the number of ACE matches is: 200
 For SEQ number: 30 the number of ACE matches is: 604
```

#### Task 4 - retrieving As Specific XPATH

One of the interesting functions with NETCONF is the ability to directly request a leaf value using a special called an XPATH. In this example we will querry the router every 7 seconds to watch for incrementing ACE matches.

A quick note before we step into the code. When we run the code we will actually be kicking off two scripts. The first 'generate_traffic_xpath.py' is logging into the router and sending pings to simulate a host sending traffic.

Let's look at the code

```
cat nc_xpath_nat.py
```

The critical change in this example is the NETCONF request.

```
results = m.get(filter=('xpath', "access-lists/access-list/access-list-entries/access-list-entry[rule-name='20']/access-list-entries-oper-data/match-counter"))
```
In this example we are still using 'get' with a filter but the type is defined as xpath and we explicitly provide the path through the YANG model for the details we want. If you inspect closely you can see that we are looking for the list entry that matches the key for rule-name=20. 

A couple of additional notes in the code. I'm using the time library to insert pauses in the code. The reason is to first allow the first set of pings to start and then to allow sufficient time to see the counters increment. 

Finally, the code will loop 5 times. Each time the code will make the NETCONF request using the session details and send the output to the console.

Let's run it:

Type or Paste:

```
python generate_traffic_xpath.py &
python nc_xpath_nat.py

```
After the code executes you should see output similar to what's below.

```
 For SEQ number: 20 the number of ACE matches is: 205
 For SEQ number: 20 the number of ACE matches is: 205
 For SEQ number: 20 the number of ACE matches is: 215
 For SEQ number: 20 the number of ACE matches is: 225
 For SEQ number: 20 the number of ACE matches is: 225
```

And that's it. Let's wrap this up.

## [Moving on to the Wrap Up!](DEVWKS_1001_Self_7.md)
## [Return to the Table of Contents](../../README.md)
