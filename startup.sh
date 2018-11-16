#!/usr/bin/env bash

# Copyright (c) {{current_year}} Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.0 (the "License"). You may obtain a copy of the
# License at
#
#               https://developer.cisco.com/docs/licenses
#
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

echo
echo ***Stopping All Other Virtual Box Instances***
echo
vboxmanage list runningvms | sed -E 's/.*\{(.*)\}/\1/' | xargs -L1 -I {} VBoxManage controlvm {} savestate

echo
echo ***SETTING BASH PROMPT***
echo

export PS1='\W$ '

echo
echo ***CREATING VIRTUAL ENVIRONMENT***
echo
virtualenv venv --python=python3

echo
echo ***STARTING VIRTUAL ENVIRONMENT***
echo
source ./venv/bin/activate

echo
echo ***INSTALLING REQUIREMENTS***
echo
pip install -r requirements.txt

echo
echo ***STARTING VAGRANT***
echo

vagrant up

echo
echo ***Launching Router Provisioning Script***
echo

cd provision
python provision_gs.py
cd ..

echo
echo ***Opening up the Task List***
echo

open tasklist.txt

echo ***THE STARTUP SCRIPT IS COMPLETE.***
