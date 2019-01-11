# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "iosxe/16.09.01"

  # IOS XE 16.7+ requires virtio for the network adapters.
  config.vm.network :private_network, virtualbox__intnet: "link1", auto_config: false, nic_type: "virtio"
  config.vm.network :private_network, virtualbox__intnet: "link2", auto_config: false, nic_type: "virtio"

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL

end
