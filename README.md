# ansible-infra
# 

## About 
This is a collections of roles/ playbooks to post-configure Red Hat Satellite 6 server, perform actions in Red Hat Virtualization and other examples useful in case of testing or demoing product features.
\
\
Everything has been written keeping in mind the usage of Ansible Automation Platform. 

## Author, Copyright and License
This repo contains code created by Gianfranco Sigrisi.\
It is free software licensed under the terms of the GNU General Public License GPL v3 or later.

## Motivation
I've wrote this Playbook because I do a lot of experiments in my LAB.\
On a daily base, I use Red Hat Satellite, Ansible Automation Platform and Red Hat Virtualization to try new stuff and 
sometimes it breaks.\
\
Manual installation takes a lot of time and all I want to do is *automate*. 

## Scope
This playbook is not meant for daily tasks such as creating and provision new hosts.\
It can be useful in case specific operations are needed after the initial base OS installation.

## How to use
The code has been created to be used both from cli and Ansible Automation Platform. 

### Variables Examples

```
global_parameters:
  - parameter_type: 'json'
    name: "kernel_settings_sysctl"
    value: [{ name: fs.file-max, value: 400000 },{ name: kernel.threads-max, value: 65536},{ name: vm.swappiness,value: 40}]
  - parameter_type: 'json'
    name: timesync_ntp_servers
    value: [{ hostname: 82.197.164.46, iburst: true },{ hostname: 82.197.188.130, iburst: true}]
  - parameter_type: 'array'
    name: "resolv_search"
    value: [domain1.com, domain2.com]
  - { name: ansible_roles_check_mode, value: false  }
  - { name: bootloader-append, value: nofb }
  - { name: disable-firewall, value: 'false' }
  - { name: enable-epel, value: false }
  - { name: enable-luks, value: false }
  - { name: enable-puppet5, value: false }
  - { name: enable-remote-execution-pull, value: false }
```

## Contributions
Contributions are welcome, just send me a pull-request.
