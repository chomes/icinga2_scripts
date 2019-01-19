# author: chomes@github
# Version: 1.0
# Future version: Adding argparse as a one line command rather then using inputs all the time.
from pathlib import Path


def config_startup():
    host_os = input("What host are you adding for 1 : Windows, 2: Linux  ")
    while True:
        if host_os == "1":
            break
        elif host_os == "2":
            break
        else:
            print("You didn't choose a number, try again")
            continue

    if host_os == "1":
        conf_create_windows()
    elif host_os == "2":
        conf_create_linux()


def conf_create_linux():
    while True:
        short_list = []
        shortname = input("What is the name you gave icinga for this linux machine? ")
        short_list.append(shortname)
        host = input("What is the external IP or FQDN for the host? ")
        hostip = host
        short_list.append(host)
        print("Here is your host details: ")
        for checks in short_list:
            print(checks)
        confirm = input("Are you happy with this information? y or n ").lower()
        if confirm == "y":
            break
        else:
            continue
    print("Pre checks done, creating conf file")
    template_linux(host, hostip, shortname)


def conf_create_windows():
    while True:
        short_list = []
        shortname = input("What is the name you gave icinga for this Windows machine? ")
        short_list.append(shortname)
        hostip = input("What's the IP address internally for the host? ")
        short_list.append(hostip)
        host = input("What is the external IP or FQDN for the host? ")
        short_list.append(host)
        print("Here is your host details: ")
        for checks in short_list:
            print(checks)
        confirm = input("Are you happy with this information? y or n ").lower()
        if confirm == "y":
            break
        else:
            continue
    print("Pre checks done, creating conf file")
    template_windows(host, hostip, shortname)


def template_windows(host, hostip, shortname):
    conf_file = """
    object Zone "%s" {
      endpoints = [ "%s" ]
      parent = "master"
    }
    
    object Endpoint "%s" {
      host = "%s"
    }
    
    
    object Host "%s" {
      import "generic-host"
      address = "%s"
      vars.ping_win_address = "%s"
      vars.os = "Windows"
      vars.remote_client = "%s"
      vars.notification["mail"] =  {
        groups = [ "icingaadmins" ]
      }
    }
    """ % (shortname, shortname, shortname, host, shortname, host, hostip, shortname)
    with open("/etc/icinga2/conf.d/hosts.d/{}.conf".format(shortname), "w") as file:
        file.write(conf_file)
    print("Your config has been created, you can edit it in /etc/icinga2/conf.d/hosts.d/{}.conf  "
          "Don't forget to restart the icinga2 server for the changes to take affect!".format(shortname))


def template_linux(host, hostip, shortname):
    conf_linux = """
    object Zone "%s" {
      endpoints = [ "%s" ]
      parent = "master"
    }
    
    object Endpoint "%s" {
      host = "%s"
    }
    
    
    object Host "%s" {
      import "generic-host"
      address = "%s"
      vars.os = "Linux"
      vars.disks["disk /"] = {
        disk_partitions = "/"
      }
      vars.procs["procs"] = {
      }
      vars.users["users"] = {
      }
      vars.client_endpoint = "%s"
      vars.notification["mail"] = {
        groups = [ "icingaadmins" ]
      }
    } 
    """ % (shortname, shortname, shortname, host, shortname, hostip, shortname)
    with open("/etc/icinga2/conf.d/hosts.d/{}.conf".format(shortname), "w") as file:
        file.write(conf_linux)
    print("Your config has been created, you can edit it in /etc/icinga2/conf.d/hosts.d/{}.conf "
          "Don't forget to restart the icinga2 server for the changes to take affect!".format(shortname))


host_folder = Path("/etc/icinga2/conf.d/hosts.d")
if host_folder.is_dir():
    print("Directory exists, starting function.")
else:
    print("Directory doesn't exist, creating folder.")
    host_folder.mkdir(0o755)

print("Starting config")
config_startup()
