# jenkins

The `jenkins` bundle installs the popular automation service [Jenkins](https://jenkins.io/) from the official yum repo.
It additionally configures some basic options set within it's `sysconfig` file

## Compatibility

This bundle has been tested on the following systems:

| OS          | `[x]` |
| ----------- | ----- |
| Fedora 24   | `[x]` |
| Fedberry 24 | `[ ]` |

## Requirements

* Java

## Integrations

* Bundles:
  * [yum](https://github.com/rullmann/bundlewrap-yum)
    * If `yum`-bundle is available OpenJDK is installed automatically.

## Metadata

All options are optional. Please take a look into `files/sysconfig` for available options.
