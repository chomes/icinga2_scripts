<h1> Icinga Scripts </h1>

Icinga scripts are used for creating config files for adding new hosts to the server on the icinga server.

This can by done by :
1) Using ansible scripts to install the repo and packages onto the host using yum and apt.
2) Using ansible to import a service.conf file onto icinga server that will pick up services for windows/linux hosts.
2) Using a python script to create host files for new hosts you install.

#Future versions
* Automate adding a linux node onto ansible 
* Automate adding a windows node onto ansible
* Automate host conf using argparse rather then inputs

<h2> How to use scripts </h2>

* For ansible it's required to have ansible installed on whatever host you use ansible on and then run the playbook.
* Knowledge of ansible is required great tutorials can be found online for this.

* For python scripts simply running python3 on ubuntu or your linux distro, you can also download the binary files
I'll create if you want to run it out of the box and simply run the bin file.  