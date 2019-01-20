<h1> Icinga Scripts </h1>

Icinga scripts are used for creating config files for adding new hosts to the server on the icinga server.

This can by done by :
1) Using ansible scripts to install the repo and packages onto the host using yum and apt and also configuring client.
2) Using ansible to install basic packages except mysql server (on ubuntu due to splash screen) and import services.conf
to allow linux and windows services to be picked up in the configs
2) Using a python script to create host files for new hosts you install.

#Future versions
* Automate adding a windows node onto ansible
* Automate host conf using argparse rather then inputs

<h2> How to use scripts </h2>

* For ansible it's required to have ansible installed on whatever host you use ansible on and then run the playbook.
* Knowledge of ansible is required great tutorials can be found online for this.
* The default user I am using is ansible but feel free to change this around.
* Please note that while the rhel/centos ansible script should work ec2 isn't fully supported, if you have some ansible knowledge,
you can change the script around to remove the epel repo and instead enable the following repos on your ec2 host:
rhui-REGION-rhel-server-extras 
rhui-REGION-rhel-server-optional

* For python scripts simply running sudo python3 on ubuntu or your linux distro, you can also download the binary files
I'll create if you want to run it without having python so you can just start up and go.  