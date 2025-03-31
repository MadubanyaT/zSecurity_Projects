#!/usr/bin/env python

import subprocess
import optparse  # allows arguments from the user through the terminal eg --interface ... --help etc


def get_Args():
    _parser = optparse.OptionParser()
    _parser.add_option('-i', '--interface', dest='interface', help='name of the interface to change its MAC address')
    _parser.add_option('-m', '--mac', dest='new_mac', help='new MAC address')
    (options, arguments) = _parser.parse_args()

    if not options.interface:
        _parser.error('[-] Specify an interface, use --help for more info.')
    if not options.new_mac:
        _parser.error('[-] Enter a new MAC address, use --help for more info.')

    return options


def change_Mac(interface, new_mac):
    print(f'+[+[+ Changing MAC address for: {interface} to {new_mac}')
    subprocess.run(['ifconfig', interface, 'down'])
    subprocess.run(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.run(['ifconfig', interface, 'up'])
    subprocess.run(['ifconfig', interface])


options = get_Args()
change_Mac(options.interface, options.new_mac)