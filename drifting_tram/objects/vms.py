from __future__ import print_function
import libvirt
from drifting_tram import virtualization
import jinja2

class Vms():
    def __init__(self, hypervisor_type='qemu', host=''):
        self._hypervisor_type = hypervisor_type
        self._host = host
        self.connection = self._connect_to_hypervisor()

    def create(self, name):
        print(name)

    def _get_connection_uri_string(self):
        connection_uri_string = '{0}://{1}/{2}'.format(self._hypervisor_type,
                                                       self._host,
                                                       'system')
        return connection_uri_string

    def _connect_to_hypervisor(self):
        connection = libvirt.open(self._get_connection_uri_string())
        return connection

    def dumpxml(self):
        xml = virtualization.xml
        iface = self.connection.interfaceDefineXML(xml)
        print(type(iface))
        print(iface.XMLDesc())
        iface.create(0)
        return iface




