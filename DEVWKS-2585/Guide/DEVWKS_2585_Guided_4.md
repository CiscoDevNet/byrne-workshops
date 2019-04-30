## Module 3: Making RESTCONF API Calls with Python

#### Task 7 - Generate the API Call with Postman

Put:

```
https://{{host}}:{{port}}/restconf/data/Cisco-IOS-XE-native:native/hostname
```

Body:

```
{
    "Cisco-IOS-XE-native:hostname": "<< INSERT TEXT HERE>>"
}
```

# **DO NOT HIT SEND**

From the Postman UI

1. On the right hand side under the send button click **code**
2. In the window that pops up change the drop down to **Python Requests**
3. Select **Copy to Clipboard**

Create the File:

```
touch test_python.py
```

Open the file:

```
open -a TextEdit test_python.py 
```
1. Past the contents of your buffer into the open file.
2. On the line that starts with **payload** replace <<INSERT TEXT HERE>> with a new hostanme. **NOTE: The rules for creating hostnames still apply!**
3. Replace the line that starts with **response** with:

```
response = requests.request("PUT", url, data=payload, headers=headers, verify=False)
```

4. Save the file

```
response = requests.request("PUT", url, data=payload, headers=headers, verify=False)
```


Execute the Script

```
python test_python.py
```

Validate the Hostname Change

URI

```
https://{{host}}:{{port}}/restconf/data/Cisco-IOS-XE-native:native/hostname
```

## [Moving on the Wrap Up!](DEVWKS_2585_Guided_5.md)

## [Return to the Table of Contents](../../README.md)