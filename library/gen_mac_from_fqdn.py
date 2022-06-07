#!/usr/bin/python

# Copyright: (c) 2020, Jonas Mauer <jam@kabelmail.net>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

import hashlib

__metaclass__ = type

DOCUMENTATION = r'''
---
module: gen_mac_from_fqdn

short_description: Generate MAC(s) from FQDN and networks

version_added: "1.0.0"

description: Generate reproducable MAC address(es) from an FQDN and its network list.

options:
    fqdn:
        description: This is the FQDN of a VM to generate a MAC(s) for.
        required: true
        type: str
    networks:
        description: This is a list of networks for virtinstall.
        required: true
        type: list

author:
    - Jonas Mauer (@jam82)
'''

EXAMPLES = r'''
- name: Test MAC generation
  gen_mac_from_fqdn:
    fqdn: test.mauer.in
    networks:
        - network=default
        - bridge:br0,model.type=virtio
'''

RETURN = r'''
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample:
        "test.mauer.in",
        [
            "network=default",
            "bridge:br0"
        ]
message:
    description: The output message that the module generates.
    type: str
    returned: always
    sample: 'goodbye'
macs:
    description: The list with the MAC address in order of 'networks'.
    type: list
    returned: always
    sample: [
        '02:09:07:10:12:02',
        '02:06:13:00:22:09'
    ]
'''

from ansible.module_utils.basic import AnsibleModule


def get_md5(name: str):
    return hashlib.md5(name.encode('utf-8')).hexdigest()

def split_n(list: list, n: int):
    return [list[index : index + n] for index in range(0, len(list), n)]

def gen_mac(name: str, networks: list):
    macs = []
    # we just care for the index of the network element
    for idx, net in enumerate(networks):
        # get hash from fqdn + network index, e.g. get_md5('test.mauer.in-1')
        md5  = get_md5(name + '-' + str(idx))
        # md5 = 6abba68431...
        # we split it by 2 so parts = [6a, bb, a6, 84, 31, ..]
        parts = split_n(md5, 2)
        # x2:xx.. is a private mac prefix, so we use 02
        # and add the first 5 elements of parts
        elements = ["02",parts[0],parts[1],parts[2],parts[3],parts[4]]
        # then we join elements by ':' to get the mac address
        # which in this case is "02:6a:bb:a6:84:31"
        mac = ':'.join(elements)
        # and append it to the list of macs that we return
        macs.append(mac)
    return macs

def run_module():
    module_args = dict(
        fqdn=dict(type='str', required=True),
        networks=dict(type='list', required=True),
    )

    result = dict(
        changed=False,
        original_message='',
        message='',
        macs='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    result['original_message'] = [
        module.params['fqdn'],
        module.params['networks']
    ]
    result['message'] = 'goodbye'
    result['macs'] = gen_mac(module.params['fqdn'], module.params['networks'])

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
