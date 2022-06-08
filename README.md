# ansible-role-virtinstall

![GitHub](https://img.shields.io/github/license/jam82/ansible-role-virtinstall) ![GitHub last commit](https://img.shields.io/github/last-commit/jam82/ansible-role-virtinstall) ![GitHub issues](https://img.shields.io/github/issues-raw/jam82/ansible-role-virtinstall) ![Travis (.com) branch](https://img.shields.io/travis/com/jam82/ansible-role-virtinstall/main?label=travis)

**Ansible role for deploying libvirt guests with virt-install.**

Currently kickstart and preseed via initrd-inject and pxe boot are supported.
Cloud-Init support will be added in the future.

## Supported Platforms

| OS Family | Distribution  | Latest | Supported Version(s) | Comment |
|-----------|---------------|--------|----------------------|---------|
| RedHat    | Fedora        | :heavy_check_mark: | 36 | |

## Requirements

- ansible >=2.9
- virt-install

## Variables

Variables and defaults for this role.

### defaults/main.yml

```yaml
---
# role: ansible-role-virtinstall
# file: defaults/main.yml

# name of the guest in libvirt
virtinstall_name: "{{ inventory_hostname_short | d('test') }}"

# the host virt-install is executed from, all tasks are delegated to this host.
# this is different than the inventory_host which is the guest to be created
virtinstall_host: "localhost"

# generate MAC address(es) from hostname and network card index
virtinstall_gen_mac_from_name: true

# FQDN used only for MAC generation,  define this in hosts inventory.
virtinstall_fqdn: "{{ inventory_hostname | d('test.jam82.de') }}"

# secure boot on fedora
virtinstall_boot:
  - loader=/usr/share/OVMF/OVMF_CODE.secboot.fd
  - loader.readonly=yes
  - loader.type=pflash
  - nvram.template=/usr/share/OVMF/OVMF_VARS.secboot.fd
  - loader_secure=yes
# default to local qemu system connection
virtinstall_connection: qemu:///system
virtinstall_console: pty,target_type=serial
# disks of the VM as list, direct params of `virt-install --disk`
virtinstall_disks:
  - "path=/tmp/{{ virtinstall_name }}.qcow2,format=qcow2,size=32,target.bus=virtio"
# virt-install --extra-args "..."
# inst.ks file has to exist or virt-install fails.
virtinstall_extra_args:
  # - "inst.ks=file:/{{ virtinstall_name }}.cfg"
  - console=tty0
  - console=ttyS0,115200
  - ipv6.disable=1
# system management mode needed for secure boot
virtinstall_features:
  - smm.state=on
# graphics cards of the guest
virtinstall_graphics:
  - spice
# inject kickstart or preseed file
virtinstall_initrd_inject: ''  # /tmp/test.ks
# install location, cann install directly from mirror
virtinstall_location: https://ftp.fau.de/almalinux/8/BaseOS/x86_64/os
# guest memory
virtinstall_memory: 4096
# guest networks, do not specify mac=52:54... when virtinstall_gen_mac_from_fqdn
virtinstall_networks:
  - bridge:br0
# with noautoconsole virt-install terminates after spinning up the install
# and leaves the guest shutdown after intsallation
virtinstall_noautoconsole: true
# os-variant, run `osinfo-query os` to get a list of supported OSs
virtinstall_os_variant: almalinux8
# sound card to attach to the guest
virtinstall_sound: none
# number of vcpus
virtinstall_vcpus: 4
# virtualization type used for the guest: kvm, qemu, xen, etc...
virtinstall_virt_type: kvm
```

## Dependencies

- community.libvirt
- jam82.general

As my login to ansible galaxy is screwed since some years because of an interrupted initial login, you need to use github as install source.

```yaml
---
# file: requirements.yml
collections:
  - name: git+https://github.com/jam82/ansible-collection-general.git
    version: main
```

## Example Playbook

```yaml
---
# role: ansible-role-virtinstall
# play: virtinstall
# file: virtinstall.yml

- hosts: all
  become: true
  gather_facts: true
  roles:
    - role: ansible-role-virtinstall
```

## License and Author

- Author:: [jam82](https://github.com/jam82/)
- Copyright:: 2022, [jam82](https://github.com/jam82/)

Licensed under [MIT License](https://opensource.org/licenses/MIT).
See [LICENSE](https://github.com/jam82/ansible-role-virtinstall/blob/master/LICENSE) file in repository.

## References

- [community.libvirt.virt module](https://docs.ansible.com/ansible/latest/collections/community/libvirt/virt_module.html)
- [virt-install(1) - Linux man page](https://linux.die.net/man/1/virt-install)
