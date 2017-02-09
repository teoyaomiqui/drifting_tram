vm_xml = """

<domain type='kvm'>
    <name>{0}</name>
    <memory>1048576</memory>
    <os>
        <type>hvm</type>
        <boot dev="hd" />
    </os>
    <features>
        <acpi/>
    </features>
    <vcpu>{1}</vcpu>
    <devices>
        <disk type='file' device='disk'>
            <driver type='qcow2' cache='none'/>
            <source file='/var/lib/libvirt/images/trusty1.img'/>
            <target dev='vda' bus='virtio'/>
        </disk>
        <disk type='file' device='disk'>
            <source file='/var/lib/libvirt/images/user-data.img'/>
            <target dev='vdb' bus='virtio'/>
        </disk>
        <interface type='network'>
            <source network='default'/>
            <model type='virtio'/>
        </interface>
    </devices>
</domain>
</code>
"""