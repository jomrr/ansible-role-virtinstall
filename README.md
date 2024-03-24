# Ansible role virtinstall

![GitHub](https://img.shields.io/github/license/jam82/ansible-role-virtinstall) ![GitHub last commit](https://img.shields.io/github/last-commit/jam82/ansible-role-virtinstall) ![GitHub issues](https://img.shields.io/github/issues-raw/jam82/ansible-role-virtinstall)

**Ansible role for deploying libvirt guests with virt-install.**

## Description

Perform unattended install of libvirt guests with virt-install.

## Prerequisites

This role has no special prerequisites.

### System packages (Fedora)

- `python3` (Python 3.8 or later)

### Python (requirements.txt)

- ansible >= 2.15

## Dependencies (requirements.yml)

```yaml
collections:
  - community.libvirt
  - {'name': 'git+https://github.com/jam82/ansible-collection-general', 'version': 'main'}

roles:
  - {'name': 'git+https://github.com/jam82/ansible-role-libvirtd', 'version': 'main'}
```

## Supported Platforms

| OS Family | Distribution | Version | Container Image |
|-----------|--------------|---------|-----------------|
| RedHat | AlmaLinux | 8 | [jam82/molecule-almalinux:8]( https://hub.docker.com/r/jam82/molecule-almalinux ) |
| | | 9 | [jam82/molecule-almalinux:9]( https://hub.docker.com/r/jam82/molecule-almalinux ) |
| Alpine | Alpine | 3.18 | [jam82/molecule-alpine:3.18]( https://hub.docker.com/r/jam82/molecule-alpine ) |
| | | 3.19 | [jam82/molecule-alpine:3.19]( https://hub.docker.com/r/jam82/molecule-alpine ) |
| Archlinux | Archlinux | latest | [jam82/molecule-archlinux:latest]( https://hub.docker.com/r/jam82/molecule-archlinux ) |
| Debian | Debian | 11 | [jam82/molecule-debian:11]( https://hub.docker.com/r/jam82/molecule-debian ) |
| | | 12 | [jam82/molecule-debian:12]( https://hub.docker.com/r/jam82/molecule-debian ) |
| | | 13 | [jam82/molecule-debian:13]( https://hub.docker.com/r/jam82/molecule-debian ) |
| RedHat | Fedora | 39 | [jam82/molecule-fedora:39]( https://hub.docker.com/r/jam82/molecule-fedora ) |
| | | 40 | [jam82/molecule-fedora:40]( https://hub.docker.com/r/jam82/molecule-fedora ) |
| | | rawhide | [jam82/molecule-fedora:rawhide]( https://hub.docker.com/r/jam82/molecule-fedora ) |
| Suse | OpenSuse Leap | 15 | [jam82/molecule-opensuse leap:15]( https://hub.docker.com/r/jam82/molecule-opensuse leap ) |
| Debian | Ubuntu | 20.04 | [jam82/molecule-ubuntu:20.04]( https://hub.docker.com/r/jam82/molecule-ubuntu ) |
| | | 22.04 | [jam82/molecule-ubuntu:22.04]( https://hub.docker.com/r/jam82/molecule-ubuntu ) |
| | | 24.04 | [jam82/molecule-ubuntu:24.04]( https://hub.docker.com/r/jam82/molecule-ubuntu ) |

## Role Variables

No role default variables specified, see [defaults/main.yml](defaults/main.yml).

## Example Playbook

Example playbooks(s) that show how to use this role.

## Simple example playbook

A simple default example playbook for using jam82.virtinstall.
```yaml
---
# name: "jam82.virtinstall"
# file: "playbook_virtinstall.yml"

- name: "PLAYBOOK | virtinstall"
  hosts: "virtinstall_hosts"
  gather_facts: true
  roles:
    - role: "jam82.virtinstall"
```

## Author(s) and License

- :octocat:                 Author::    [jam82](https://github.com/jam82)
- :triangular_flag_on_post: Copyright:: 2022, Jonas Mauer
- :page_with_curl:          License::   [MIT](LICENSE)

## References

- [man virt-install(1)](https://manpages.org/virt-install)

---
