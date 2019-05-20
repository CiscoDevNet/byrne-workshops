#Makefile

prepenv:
	@echo "*** Creating Virtual Environment ***"
	( \
		python3 -m venv venv; \
		source venv/bin/activate; \
		pip install --upgrade pip; \
		pip install -r requirements.txt; \
)

vagrant:
	@echo "*** Stopping Existing VMs ***"
	vboxmanage list runningvms | sed -E 's/.*\{(.*)\}/\1/' | xargs -L1 -I {} VBoxManage controlvm {} savestate
	@echo "*** Bringing Up the Router ***"
	vagrant up

provision_1001:
	@echo "*** Configuring the Router ***"
	python provision/provision_lab.py -hn DEVWKS-1001

prep_1001:
	@echo "*** Opening the Lab Guide File ***"
	open https://github.com/CiscoDevNet/byrne-workshops/blob/clus19/DEVWKS-1001/Guide/DEVWKS_1001_Guided_1.md

provision_1512:
	@echo "*** Configuring the Router ***"
	python provision/provision_lab.py -hn DEVWKS-1512

prep_1512:
	@echo "*** Opening the Lab Guide File ***"
	open https://github.com/CiscoDevNet/byrne-workshops/blob/clus19/DEVWKS-1512/Guide/DEVWKS_1512_Guided_1.md

provision_1695:
	@echo "*** Configuring the Router ***"
	python provision/provision_lab.py -hn DEVWKS-1695

prep_1695:
	@echo "*** Opening the Lab Guide File ***"
	open https://github.com/CiscoDevNet/byrne-workshops/blob/clus19/DEVWKS-1695/Guide/DEVWKS_1695_Guided_1.md

provision_2585:
	@echo "*** Configuring the Router ***"
	python provision/provision_lab.py -hn DEVWKS-2585

prep_2585:
	@echo "*** Opening the Lab Guide File ***"
	open https://github.com/CiscoDevNet/byrne-workshops/blob/clus19/DEVWKS-2585/Guide/DEVWKS_2585_Guided_1.md

start_1001: vagrant provision_1001 prep_1001
start_1512: vagrant provision_1512 prep_1512
start_1695: vagrant provision_1695 prep_1695
start_2585: vagrant provision_2585 prep_2585

cleanup:
	@echo "*** Destroying the Vagrant box ***"
	vagrant destroy -f
	rm ~/code/byrne-workshops/DEVWKS-2585/code/test_python.py
