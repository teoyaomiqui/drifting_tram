#!/usr/bin/python
import libvirt
import sys
import os
import uuid
import random
import subprocess

mac =   "52:54:00:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        )
xmlconfig = """

<domain type='kvm'>
  <name>{}</name>
  <memory unit='KiB'>2000000</memory>
  <currentMemory unit='KiB'>2000000</currentMemory>
  <vcpu placement='static'>1</vcpu>
  <os>
   <type arch='x86_64' machine='pc-i440fx-xenial'>hvm</type>
   <boot dev='hd'/>
  </os>
  <features>
    <acpi/>
    <apic/>
    <pae/>
  </features>
  <clock offset='utc'/>
  <on_poweroff>destroy</on_poweroff>
  <on_reboot>destroy</on_reboot>
  <on_crash>destroy</on_crash>
  <devices>
    <interface type='bridge'>
      <mac address='{}'/>
      <source bridge='virbr0'/>
      <target dev='vnet1'/>
      <model type='virtio'/>
      <alias name='net0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
    </interface>
    <serial type='pty'>
      <source path='/dev/pts/11'/>
      <target port='0'/>
      <alias name='serial0'/>
    </serial>
    <console type='pty' tty='/dev/pts/11'>
      <source path='/dev/pts/11'/>
      <target type='serial' port='0'/>
      <alias name='serial0'/>
    </console>
    <channel type='spicevmc'>
      <target type='virtio' name='com.redhat.spice.0' state='disconnected'/>
      <alias name='channel0'/>
      <address type='virtio-serial' controller='0' bus='0' port='1'/>
    </channel>

    <graphics type='spice' port='5900' autoport='yes' listen='127.0.0.1'>
      <listen type='address' address='127.0.0.1'/>
      <image compression='off'/>
    </graphics>


  </devices>
</domain>







""".format(sys.argv[1],mac)

connection = libvirt.open('qemu:///system')
if connection == None:
    print 'Connection was failed'
    sys.exit(1)
domName = sys.argv[1]
#try:
#    dom = connection.lookupByName(domName)
#    print 'Domain already exists'
#    sys.exit(1)
#except:
#    pass
dom_define = connection.defineXML(xmlconfig)
print mac
dom = connection.lookupByName(domName)
dom.create()
