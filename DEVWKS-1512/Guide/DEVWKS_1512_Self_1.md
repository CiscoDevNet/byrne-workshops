## Introduction

Welcome to the Self Guided Lab Guide for Becoming the Jinja Ninja: Using YAML and Jinja Templating to Create Resuable Code. The purpose of this guide is to provide an introduction to using tools like YAML and Jinja for creating templates to be used in network automation. 

The idea of using configuration templates is not new. Network engineers have always used some form of templating, typically common configurations stored in notepad, for commonly repeated configuration tasks. Built around the idea of a global search and replace engineers will parse through and fill in the device specific details as needed.

As the industry starts to shift towards network automation how we template our configurations is changing. Now, rather than directly modifying our automation code, we will create a template file that can be called by our code and substituting the device specific details that are read in as variables. 

Before we start talking about the individual components let's briefly identify the foundations for reusable code

### Foundations for Reusable Code
- Scripting Language - This is fairly self-explanatory. The scripting language will be used to generate our device configuration. Typical options here are Python or Ansible.
- Templates - These are a set of reusable configuration and operational command sets. It includes logic for substitution for device specific parameters. Examples here include Jinja2 for configurations and TextFSM for operational commands.
- Structured Data - This is data that exists in a fixed field within a record or file. The idea here is if the data has some type of predictable format we can write code that can parse and extract the data to be used in our templates.

## [Module 1 - Introduction to YAML](DEVWKS_1512_2.md)
## [Return to the Table of Contents](../../README.md)
