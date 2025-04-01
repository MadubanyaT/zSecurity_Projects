#!/usr/bin/env python

import re
import subprocess
import optparse  # allows arguments from the user through the terminal eg --interface ... --help etc


def get_Args():
    _parser = optparse.OptionParser()
    _parser.add_option('-i', '--interface', dest='interface', help='name of the interface to change its MAC address')
    _parser.add_option('-m', '--mac', dest='new_mac', help='new MAC address')
    (option, arguments) = _parser.parse_args()

    if not option.interface:
        _parser.error('[-] Specify an interface, use --help for more info.')
    if not option.new_mac:
        _parser.error('[-] Enter a new MAC address, use --help for more info.')

    return option


def change_Mac(interface, new_mac):
    print(f'[++] Changing MAC address for: {interface} to {new_mac}')
    subprocess.run(['ifconfig', interface, 'down'])
    subprocess.run(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.run(['ifconfig', interface, 'up'])


def get_current_MAC(interface):
    ifconfig_re = subprocess.run(['ifconfig', interface], capture_output=True)
    mac_re = re.search('\\w\\w:\\w\\w:\\w\\w:\\w\\w:\\w\\w:\\w\\w', str(ifconfig_re))

    if mac_re:
        return mac_re.group(0)
    else:
        print('[--] No mac address on the specified interface.')


options = get_Args()

current_mac = get_current_MAC(options.interface)
print(f'The current MAC address: {str(current_mac)}')

change_Mac(options.interface, options.new_mac)

current_mac = get_current_MAC(options.interface)
if current_mac == options.new_mac:
    print(f'[++] MAC address was successfully changed to: {current_mac}')
else:
    print('[--] MAC address was not changed.')
