Role Name
=========

Role for installing razor server.

Razor is an advanced provisioning application which can deploy both bare-metal and virtual systems. It's aimed at solving the problem of how to bring new metal into a state where your existing DevOps/configuration management workflows can take it over.

Newly added machines in a Razor deployment will PXE-boot from a special Razor Microkernel image, then check in, provide Razor with inventory information, and wait for further instructions. Razor will consult user-created policy rules to choose which tasks to apply to a new node, which will begin to follow the task directions, giving feedback to Razor as it completes various steps. Tasks can include steps for handoff to a DevOps system such as Puppet or to any other system capable of controlling the node (such as a vCenter server taking possession of ESX systems).

Requirements
------------
- razor-server
- rubygems
- ipmitool

Role Variables
--------------

# Test variables

Variable to specify the configuration template.
```
razor_conf_template: config.yaml.j2 
```

This is an example of variables used for test, found in testvars.yml
```
db_user: razor
db_name: razor_prd
db_password: RaZordbPass
```

Dependencies
------------

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: rngkll.razor }

License
-------
MIT

Author Information
------------------

Alvaro Segura Del Barco
