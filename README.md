# jenkins

The `jenkins` bundle installs the popular automation service [Jenkins](https://jenkins.io/) from the official dnf repo.
It additionally configures some basic options set within it's `sysconfig` file

## Maintenance notice

As of February 2018 this bundle will not be mainained anymore. If you encounter any issues I cannot help.

## Requirements

* Java

## Integrations

* Bundles:
  * [dnf](https://github.com/rullmann/bundlewrap-dnf)
    * If `dnf`-bundle is available OpenJDK is installed automatically.
  * [monit](https://github.com/rullmann/bundlewrap-monit)

## Metadata

All options are optional. Please take a look into `files/sysconfig` for available options.
