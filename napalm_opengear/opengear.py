
"""Napalm driver for OpenGear Linux"""

import re
import socket

from napalm.base.helpers import textfsm_extractor
from napalm.base.helpers import mac, ip
from napalm.base.netmiko_helpers import netmiko_args
from napalm.base.utils import py23_compat

from napalm.base import NetworkDriver
from napalm.base.exceptions import ConnectionException


class OpenGearDriver(NetworkDriver):

    def __init__(self, hostname, username, password, timeout=60, optional_args=None):
        self.device = None
        self.hostname = hostname
        self.username = username
        self.password = password
        self.timeout = timeout

        if optional_args is None:
            optional_args = {}

        self.netmiko_optional_args = netmiko_args(optional_args)

    def _send_command(self, command):
        try:
            if isinstance(command, list):
                for cmd in command:
                    output = self.device.send_command(cmd)
                    if "% Invalid" not in output:
                        break
            else:
                output = self.device.send_command(command)
            return output
        except (socket.error, EOFError) as e:
            raise ConnectionException(str(e))

    def open(self):
        """Open a connection to the device."""
        self.device = self._netmiko_open(
            'linux',
            netmiko_optional_args=self.netmiko_optional_args,
        )

    def close(self):
        self._netmiko_close()

    def get_arp_table(self, vrf=u''):
        if vrf:
            msg = "VRF support has not been added for this getter on this platform."
            raise NotImplementedError(msg)

        command = "arp -van"
        arp_entries = self._send_command(command)
        arp_entries = textfsm_extractor(self, 'show_arp', arp_entries)

        table = []
        for idx, arp in enumerate(arp_entries):
            entry = {
                'interface': arp['interface'],
                'ip': ip(arp['ip']),
                'mac': mac(arp['mac']),
            }

            table.append(entry)

        return table

    def get_config(self, retrieve='all'):
        config = {
            'startup': u'Not implemented',
            'running': u'',
            'candidate': u'Not implemented',
        }

        if retrieve in ['all', 'running']:
            config['running'] = self._send_command("config -g config")

        return config

    def is_alive(self):
        null = chr(0)
        if self.device is None:
            return {'is_alive': False}

        try:
            # Try sending ASCII null byte to maintain the connection alive
            self.device.write_channel(null)
            return {'is_alive': self.device.remote_conn.transport.is_active()}
        except (socket.error, EOFError):
            # If unable to send, we can tell for sure that the connection is unusable
            return {'is_alive': False}

        return {'is_alive': False}
