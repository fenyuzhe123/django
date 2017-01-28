from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class UcsInventory(models.Model):
    ucs = models.CharField(db_column='Ucs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chassis_id = models.CharField(db_column='chassis_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chassis_sn = models.CharField(db_column='chassis_SN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    slotid = models.CharField(db_column='SlotId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usrlbl = models.CharField(db_column='usrLbl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    serial = models.CharField(db_column='Serial', max_length=255)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mfgtime = models.CharField(max_length=255, blank=True, null=True)
    adaptor = models.CharField(db_column='Adaptor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iom = models.CharField(db_column='IOM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpu = models.CharField(db_column='CPU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numofcpus = models.CharField(db_column='NumOfCpus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numofcores = models.CharField(db_column='NumOfCores', max_length=255, blank=True, null=True)  # Field name made lowercase.
    availablememory = models.CharField(db_column='AvailableMemory', max_length=255, blank=True, null=True)  # Field name made lowercase.
    assignedtodn = models.CharField(db_column='AssignedToDn', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField()
    uuid = models.CharField(db_column='UUID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firmware = models.CharField(db_column='Firmware', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ucs_inventory'


class VmInventory(models.Model):
    hostname = models.CharField(db_column='HostName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    insuuid = models.CharField(db_column='InsUUID', primary_key=True, max_length=255)  # Field name made lowercase.
    os_family = models.CharField(db_column='OS_Family', max_length=255, blank=True, null=True)  # Field name made lowercase.
    moref = models.CharField(db_column='MoRef', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numsocket = models.CharField(db_column='NumSocket', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numcorespersocket = models.CharField(db_column='NumCoresPerSocket', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_core = models.CharField(db_column='Total_Core', max_length=255, blank=True, null=True)  # Field name made lowercase.
    memorymb = models.CharField(db_column='MemoryMB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vmstatus = models.CharField(db_column='VMStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    network = models.CharField(db_column='Network', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vlan_id = models.CharField(db_column='VLAN_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    network_adapter = models.CharField(db_column='Network_Adapter', max_length=255, blank=True, null=True)  # Field name made lowercase.
    block_productcol = models.CharField(max_length=255, blank=True, null=True)
    ipaddress = models.CharField(db_column='IpAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vmdisk_count = models.CharField(db_column='VMDisk_Count', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esxhost = models.CharField(db_column='ESXHost', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clustername = models.CharField(db_column='ClusterName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    element_manager = models.CharField(db_column='Element_Manager', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datacenter = models.CharField(db_column='DataCenter', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guestid = models.CharField(db_column='GuestId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    market = models.CharField(db_column='Market', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_disk_count = models.CharField(db_column='Total_Disk_Count', max_length=255, blank=True, null=True)  # Field name made lowercase.
    folderlocation = models.CharField(db_column='FolderLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vmxpath = models.CharField(db_column='VMXpath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vmtools_verison = models.CharField(db_column='VMTools_verison', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vmtools_status = models.CharField(db_column='VMTools_Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    os_version = models.CharField(db_column='OS_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vmdisk_allocatedinkb = models.CharField(db_column='VMDisk_AllocatedInKB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rdmdisk_allocatedinkb = models.CharField(db_column='RDMDisk_AllocatedInKB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_storageallocatedingb = models.CharField(db_column='Total_StorageAllocatedinGB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_disk_usageinkb = models.CharField(db_column='Total_Disk_UsageInKB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rdmdisk_count = models.CharField(db_column='RDMDisk_Count', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hddetails = models.CharField(db_column='HDDetails', max_length=255, blank=True, null=True)  # Field name made lowercase.
    template = models.CharField(db_column='Template', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rdmflag = models.CharField(db_column='RDMFlag', max_length=255, blank=True, null=True)  # Field name made lowercase.
    org = models.CharField(db_column='Org', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prod_id = models.CharField(db_column='prod_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productfound = models.CharField(db_column='ProductFound', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rail_nodepath_id = models.CharField(db_column='Rail_NodePath_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rail_nodepath_name = models.CharField(db_column='Rail_NodePath_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='DeviceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qb_id = models.CharField(db_column='QB_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dc_id = models.CharField(db_column='DC_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sizing = models.CharField(db_column='Sizing', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vm_inventory'
		
class IncidentInfo(models.Model):
    number = models.CharField(primary_key=True, max_length=255)
    state = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    opened_at = models.CharField(max_length=255, blank=True, null=True)
    caller_id = models.CharField(max_length=255, blank=True, null=True)
    u_business_service = models.CharField(max_length=255, blank=True, null=True)
    u_item_type = models.CharField(max_length=255, blank=True, null=True)
    u_service_name = models.CharField(max_length=255, blank=True, null=True)
    u_issue_type = models.CharField(max_length=255, blank=True, null=True)
    assigned_to = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incident_info'


class ChangeInfo(models.Model):
    number = models.CharField(primary_key=True, max_length=255)
    state = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    approval = models.CharField(max_length=255, blank=True, null=True)
    cab_date = models.CharField(max_length=255, blank=True, null=True)
    assigned_to = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_info'		


class VmEvent(models.Model):
    createdtime = models.CharField(db_column='CreatedTime', max_length=255)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255)  # Field name made lowercase.
    fullformattedmessage = models.CharField(db_column='FullFormattedMessage', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vm_event'


class VmCreation(models.Model):
    createdtime = models.CharField(db_column='CreatedTime', max_length=255)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255)  # Field name made lowercase.
    fullformattedmessage = models.CharField(db_column='FullFormattedMessage', max_length=255)  # Field name made lowercase.
    tag = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vm_creation'



class UcsFault(models.Model):
    ucs = models.CharField(db_column='Ucs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lasttransition = models.CharField(max_length=255, blank=True, null=True)
    severity = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    dn = models.CharField(max_length=255, blank=True, null=True)
    descr = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ucs_fault'
