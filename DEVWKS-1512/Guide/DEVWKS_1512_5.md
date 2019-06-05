## Module 2 Exercises : Working with Jinja Templating

In the following lab examples we will walk through using Jinja to create CLI output that can be directly pasted into a router. Using these templates are a fundamental step in creating code that can push the configuration out. That concept is a bit out of scope for this lab.

We will use the same high level approach to generating the output

- Read in the template
- Render the template with the appropriate variables
- Process the output

#### Task 1 - Creating a Simple Jinja Template

In this lab we will be using a Jinja template to create both a VLAN and the associated SVI. Let's take a look at the code

Type or Paste:

```
cat jinja_create_vlan.py
```

The output:

```
from jinja2 import Template

template_in = Template("""
            vlan {{ id }}
             name {{vlan_name }}
            !
            interface vlan {{ id }}
             ip address {{ ip_addr }} {{ mask }}
             """)

template_out = template_in.render(id=200,
                                  vlan_name='DATA',
                                  ip_addr='192.168.1.1',
                                  mask="255.255.255.0")

print(template_out)
```
First we import Template from the jinja2 library.

In the next portion of the code we will 'read in' the template and assign it to a variable called template_in. We do this in the format of Template(template language).

After reading in the template we render the template with the supplied variables. In this example we will be providing inputs for

- VLAN ID
- VLAN Name
- IP Address
- Netmask

To do so we use the template we read in with a .render extension and we supply the variables between the parentheses and assign it to the variable of template_out.

Once we render the template we process the output. In this case we print the rendered template. Let's run the code and look at the output.


Type or Paste:

```
python jinja_create_vlan.py
```

And the output is:

```
            vlan 200
             name DATA
            !
            interface vlan 200
             ip address 192.168.1.1 255.255.255.0
```

This exercise was intended as an example to show the idea behind Read, Render, Process. The code itself isn't very reusable. Let's look at an example where we actually 'read in' an external template.

#### Task 2 - Using Jinja Loops

In this example the python code is provided for you. As an exercise you will be writing the Jinja template to configure 3 VLANs and the associated SVI.

Let's look at the python code:

```
cat jinja_loop.py
```
There are two interesting pieces of data we should look at. First is the addition of the device_details variable. This is the list of interfaces we will be configuring. Each list index is a key:value pair that we will be rendering into the template.

Next, rather than directly write the template into the code we will read in an external file and assign it to the variable of config_in

```
with open("jinja_loop.j2") as f:
    config_in = Template(f.read())
```

In the render step rather than define the variables in code we will pull them out of the list in a Jinja for loop.

Let's get started writing our template. To ensure that we use a properly named file (for no other reason that it's defined in the code) let's use the following to create that file.

```
rm jinja_loop.j2
touch jinja_loop.j2
open -a TextEdit jinja_loop.j2
```

The template should look like the following:

```
{% for input in inputs %}

vlan {{ input.id }}
 name {{ input.name }}
interface vlan {{ input.id }}
 Description {{ input.desc }}
 IP address {{ input.address }} {{ input.mask }}

{% endfor %}
```

Let's look at the parts of the template.

- {% for input in inputs %} - This line sets our loop. If we look back at the code we see that we are rendering the variables as defined with 'inputs=' in the Python code. 
- {{ input.id }} - Our variable substitution format is changed slightly from our previous example. We use the 'input' to represent an instance of our list of interfaces. The .id is a specific key from the dictionary.
- {% endfor %} - This ends our for loop.

Let's run the code and check the output.

```
python jinja_loop.py
```

And the output:

```
vlan 101
 name DATA
interface vlan 101
 Description This is the SVI
 IP address 10.0.10.1 255.255.255.0



vlan 201
 name VOICE
interface vlan 201
 Description This is the VOICE SVI
 IP address 10.0.20.1 255.255.255.0



vlan 301
 name GUEST
interface vlan 301
 Description This is the GUEST SVI
 IP address 10.0.30.1 255.255.255.0
```

So what happens if we need to configure multiple types of interfaces such as L2, L3, or Trunks? Let's take a look at an example.

#### Task 3 - Using Jinja Conditionals

In this example we will be using a single template to configure multiple interface types. The list of interfaces contain a mix of L2, L3, and Trunked interfaces as well as a subset of interfaces that should be a shutdown state. Let's take a look at the code:

```
cat jinja_conditional.py
```

As a hint the template will include the following

- A loop so we can iterate through all interfaces in the list.
- A conditional that matches on the type of interface
- A conditional that matches on the enabled state.

Let's create our template file

```
rm jinja_conditional.j2
touch jinja_conditional.j2
open -a TextEdit jinja_conditional.j2
```

Our template should look like the following:

```
{% for input in inputs -%}

interface {{ input.interface }}
{% if input.mode == "trunk" -%}
switchport mode {{ input.mode }}
switchport trunk allowed vlan {{ input.allowed }}
spanning-tree portfast mode trunk

{% elif input.mode == "access" -%}
switchport mode {{ input.mode }}
switchport access vlan {{ input.vlan }}
spanning-tree portfast

{% else -%}
no switchport
ip address {{ input.address }} {{ input.mask }}
{% endif -%}

{% if input.enabled == "true" -%}
no shutdown

{% else -%}
shutdown

{% endif -%}

{% endfor -%}
```
Let's take a look at the highlights.

- {% for input in inputs -%} - This is our initial loop condition
- {% if input.mode == "trunk" -%} - This is our first conditional that will match on the key 'mode' in the list.
	- Conditionals are in the format of if, elif, .. , else. Our additional statements:
		- {% elif input.mode == "access" -%}
		- {% else -%} - This line would catch the routed port. It can be defined explicitly  (intput.mode == "routed")
- {% endif -%} - We must close our conditional before starting the conditional for the enabled state.
- {% endfor -%} - Closing our loop.

And let's run the code and look at the output:

Type or Paste:

```
python jinja_conditional.py
```

And the output:

```
interface GigabitEthernet 0/24
switchport mode trunk
switchport trunk allowed vlan 10,20,30-35
spanning-tree portfast mode trunk

no shutdown

interface GigabitEthernet 0/2
switchport mode access
switchport access vlan 10
spanning-tree portfast

no shutdown

interface GigabitEthernet 0/3
switchport mode access
switchport access vlan 20
spanning-tree portfast

shutdown

interface GigabitEthernet 0/1
no switchport
ip address 10.10.20.1 255.255.255.252
no shutdown
```

The only important note is the random spacing. This is an artifact from the blank lines I used in the template to make it a bit more readable. Keep in mind that Jinja will render exactly what's in the Template.

Now that we've looked at Jinja let's take an example that includes reading in YAML data to be rendered into a Jinja template.

## [Module 3: Pulling it All Together](DEVWKS_1512_6.md)
## [Return to the Table of Contents](../../README.md)