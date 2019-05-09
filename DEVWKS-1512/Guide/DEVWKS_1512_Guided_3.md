## Module 2: Jinja Templating

#### Task 1: Hello VLAN

```
cat jinja_create_vlan.py
```

```
python jinja_create_vlan.py
```

#### Task 2: Using Jinja Loops

**In This Exercise We Will be Building the Template Together**

View Python File:

```
cat jinja_loop.py
```

Create the Jinja Template File and Open It for Editing:

```
rm jinja_loop.j2
touch jinja_loop.j2
open -a TextEdit jinja_loop.j2
```

Execute the Template:

```
python jinja_loop.py
```

Want to Just See the Template?

<details><summary>CLICK ME</summary>
<p>

```
{% for input in inputs %}

vlan {{ input.id }}
 name {{ input.name }}
interface vlan {{ input.id }}
 Description {{ input.desc }}
 IP address {{ input.address }} {{ input.mask }}

{% endfor %}
```

</p>
</details>

#### Task 3: Using Jinja Conditionals

**In This Exercise We Will be Building the Template Together**

View Python File:

```
cat jinja_conditional.py
```

Create the Jinja Template File and Open It for Editing:

```
rm jinja_conditional.j2
touch jinja_conditional.j2
open -a TextEdit jinja_conditional.j2
```

Execute the Template:

```
python jinja_conditional.py
```

Want to Just See the Template?

<details><summary>CLICK ME</summary>
<p>

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

</p>
</details>



## [Let's Add in Some YAML](DEVWKS_1512_Guided_4.md)
## [Return to the Table of Contents](../../README.md)