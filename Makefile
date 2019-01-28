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

provision_2561:
	@echo "*** Configuring the Router ***"
	provision/provision_rtr.py

prep_2561:
	@echo "*** Opening the Task File ***"
	open DEVWKS-2561/tasklist.txt

provision_2585:
	@echo "*** Configuring the Router ***"
	provision/provision_rtr.py

prep_2585:
	@echo "*** Opening the Task File ***"
	open DEVWKS-2585/tasklist.txt

start_2561: vagrant provision_2561 prep_2561
start_2585: vagrant provision_2585 prep_2585



cleanup:
	@echo "*** Destroying the Vagrant box ***"
	vagrant destroy -f
	rm DEVWKS-2585/code/make_python.py
