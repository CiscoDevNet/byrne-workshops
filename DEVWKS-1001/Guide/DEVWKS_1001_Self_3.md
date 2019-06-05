## Module 1: Exploring YANG Models

At this point you may be asking yourself "What is a Data Model?" The simplest definition is a well understood agreed upon method to describe "something". As an example consider this simple "data model" for a person:

* Person
	* Gender - male, female, other
	* Height - feet/inches, or meters
	* Weight - pounds, kilos, or my personal favorite stones
	* Hair Color - brown, blonde, black, red, other
	* Eye Color - brown, blue, green, hazel, other

YANG (Yet Another Next Generation) was developed by the IETF NETMOD (Network Modeling) Working Group and published as RFC 6020 in 2010. YANG has become the de facto data modeling language. But YANG is more than just a modeling language. It is also the data models and the data itself. When we talk about YANG, depending on the context, we mean YANG as a language, YANG as a data model, and YANG data.

A data model does nothing more than describe or represent data. This is a way to agree how to describe something, for example a person:

* Person
 * Gender, e.g. male or female
 * Height, e.g. feet and inches or meters
 * Weight, e.g. pounds or kilograms
 * Eye Color, e.g. blue, green, brown, or hazel
 * Hair Color, e.g. blond, brown, or black

Even with a generic data model such as this simple example, we can describe a person in a manner that is easily understood. Although YANG data models could be used to describe anything, they were developed to describe network devices and the services we build with those devices.

A YANG data model might describe a network device data or network service data. Some examples of each include:

* Device Data Model
 * Interface
 * VLAN
 * EIGRP

* Service Data Model
 * L3 MPLS VPN
 * VRF
 * System Management

For the purpose of our lab we will be working with device level data models.

## [On to the YANG Lab Exercises](DEVWKS_1001_Self_4.md)
## [Return to the Table of Contents](../../README.md)

#### Special Thanks to Curtis Smith for letting me *borrow* his explanion of YANG. Check out his [github repo](http://github.com/curtissmith).