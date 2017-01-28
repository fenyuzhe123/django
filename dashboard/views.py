from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response
from dashboard.models import *

# Create your views here.
##### UCS Inventory
def ucs_list_data(request):
	from django.db import connection, transaction
	sql='select UCS,chassis_SN,chassis_ID,SolotId,Serial,usrLbl,Model,Adaptor,IOM,CPU,NumOfCpus,NumOfCores,AvailableMemory,AssignedToDn,Firmware,Update_date from latest_ucs_inventory'
	cursor = connection.cursor()
	cursor.execute(sql)
	instance = cursor.fetchall();
	######convert data to json
	
	card=[]
	for obj in instance:
		dic={}
		dic['Ucs']=obj[0]
		dic['chassis_SN']=obj[1]
		dic['chassis_ID']=obj[2]
		dic['SolotId']=obj[3]
		dic['Serial']=obj[4]
		dic['usrLbl']=obj[5]
		dic['Model']=obj[6]
		dic['Adaptor']=obj[7]
		dic['IOM']=obj[8]
		dic['CPU']=obj[9]
		dic['NumOfCpus']=obj[10]
		dic['NumOfCores']=obj[11]
		dic['AvailableMemory']=obj[12]
		dic['AssignedToDn']=obj[13]
		dic['Firmware']=obj[14]
		dic['Update_date']=obj[15]
		card.append(dic)
	data = {
			'records':card,
	       } 
	return JsonResponse(data)
	
def ucs_list(request):
	import json
	from django.db import connection, transaction
	title='ucs list'
	sql="select Update_date from latest_ucs_inventory limit 1"
	cursor = connection.cursor()
	cursor.execute(sql)
	updatedate=cursor.fetchall()
	for x in updatedate:
		y=x[0]	
    
	updatedate=y
	data = {
		
		'title': title,
		'updatedate': updatedate,
		}
	return render_to_response("ucs_list.html", data)
	
##### VM Inventory
def vm_list_data(request):
	from django.db import connection, transaction
	sql='select Virtual_Machine_Name,Guest_OS_Name,VMStatus,OS_Family,NumSocket,Total_Core,MemoryMB,IpAddress,MAC,Network,VLAN_ID,Network_Adapter,VMDisk_Count,ESXHost,ClusterName,DataCenter,Element_Manager,GuestId,VMXpath,VMTools_verison,VMTools_Status,VMDisk_AllocatedInKB,Total_Disk_UsageInKB,Product,Market from latest_vm_inventory'
	cursor = connection.cursor()
	cursor.execute(sql)
	instance = cursor.fetchall();
	######convert data to json
	card=[]
	for obj in instance:
		dic={}
		dic['Virtual_Machine_Name']=obj[0]
		dic['Guest_OS_Name']=obj[1]
		dic['VMStatus']=obj[2]
		dic['OS_Family']=obj[3]
		dic['NumSocket']=obj[4]
		dic['Total_Core']=obj[5]
		dic['MemoryMB']=obj[6]
		dic['IpAddress']=obj[7]
		dic['MAC']=obj[8]
		dic['Network']=obj[9]
		dic['VLAN_ID']=obj[10]
		dic['Network_Adapter']=obj[11]
		dic['VMDisk_Count']=obj[12]
		dic['ESXHost']=obj[13]
		dic['ClusterName']=obj[14]
		dic['DataCenter']=obj[15]
		dic['Element_Manager']=obj[16]
		dic['GuestId']=obj[17]
		dic['VMXpath']=obj[18]
		dic['VMTools_verison']=obj[19]
		dic['VMTools_Status']=obj[20]
		dic['VMDisk_AllocatedInKB']=obj[21]
		dic['Total_Disk_UsageInKB']=obj[22]
		dic['Product']=obj[23]
		dic['Market']=obj[24]
		card.append(dic)
	data = {'records':card}
	return JsonResponse(data)
	
def vm_list(request):
	import json
	from django.db import connection, transaction
	title='vm list'
	data = {
		
		'title': title,
		}
	return render_to_response("vm_list.html", data)	




#####  incident 
def inc_list_data(request):
	from django.db import connection, transaction
	sql='select number,state,short_description,opened_at,caller_id,u_business_service,u_item_type,u_service_name,u_issue_type,assigned_to from incident_info'
	cursor = connection.cursor()
	cursor.execute(sql)
	instance = cursor.fetchall();
	######convert data to json
	card=[]
	for obj in instance:
		dic={}
		dic['number']=obj[0]
		dic['state']=obj[1]
		dic['short_description']=obj[2]
		dic['opened_at']=obj[3]
		dic['caller_id']=obj[4]
		dic['u_business_service']=obj[5]
		dic['u_item_type']=obj[6]
		dic['u_service_name']=obj[7]
		dic['u_issue_type']=obj[8]
		dic['assigned_to']=obj[9]
		card.append(dic)
	data = {'records':card}
	return JsonResponse(data)


def inc_list(request):
	import json
	from django.db import connection, transaction
	title='incident list'
	sql="select update_time from incident_info limit 1"
	cursor = connection.cursor()
	cursor.execute(sql)
	updatedate=cursor.fetchall()
	for x in updatedate:
		y=x[0]	
    
	updatedate=y
	data = {
		
		'title': title,
		'updatedate': updatedate,
		}
	return render_to_response("inc_list.html", data)


#####  change
def change_list_data(request):
	from django.db import connection, transaction
	sql='select number,state,start_date,short_description,type,approval,cab_date,assigned_to from change_info'
	cursor = connection.cursor()
	cursor.execute(sql)
	instance = cursor.fetchall();
	######convert data to json
	card=[]
	for obj in instance:
		dic={}
		dic['number']=obj[0]
		dic['state']=obj[1]
		dic['start_date']=obj[2]
		dic['short_description']=obj[3]
		dic['type']=obj[4]
		dic['approval']=obj[5]
		dic['cab_date']=obj[6]
		dic['assigned_to']=obj[7]
		card.append(dic)
	data = {'records':card}
	return JsonResponse(data)
	
	
def change_list(request):
	import json
	from django.db import connection, transaction
	title='change list'
	sql="select update_time from change_info limit 1"
	cursor = connection.cursor()
	cursor.execute(sql)
	updatedate=cursor.fetchall()
	for x in updatedate:
		y=x[0]	
    
	updatedate=y
	data = {
		
		'title': title,
		'updatedate': updatedate,
		}
	return render_to_response("change_list.html", data)
	
	
##### UCS fault
def fault_list_data(request):
	from django.db import connection, transaction
	sql='select * from ucs_fault'
	cursor = connection.cursor()
	cursor.execute(sql)
	instance = cursor.fetchall();
	######convert data to json
	card=[]
	for obj in instance:
		dic={}
		dic['Ucs']=obj[0]
		dic['lasttransition']=obj[1]
		dic['severity']=obj[2]
		dic['type']=obj[3]
		dic['dn']=obj[4]
		dic['descr']=obj[5]
		dic['timestamp']=obj[6]
		card.append(dic)
	data = {'records':card}
	return JsonResponse(data)
	

def fault_list(request):
	import json
	from django.db import connection, transaction
	title='ucs fault list'
	sql="select timestamp from ucs_fault limit 1"
	cursor = connection.cursor()
	cursor.execute(sql)
	updatedate=cursor.fetchall()
	for x in updatedate:
		y=x[0]	
    
	updatedate=y
	sql1="select count(*) from ucs_fault where severity = 'critical'"
	sql2="select count(*) from ucs_fault where severity = 'major'"
	sql3="select count(*) from ucs_fault where severity = 'minor'"
	sql4="select count(*) from ucs_fault where severity = 'warning'"
	cursor.execute(sql1)
	critical=cursor.fetchall()
	for x in critical:
		y=x[0]
	critical=y
	cursor.execute(sql2)
	major=cursor.fetchall()
	for x in major:
		y=x[0]
	major=y
	cursor.execute(sql3)
	minor=cursor.fetchall()
	for x in minor:
		y=x[0]
	minor=y
	cursor.execute(sql4)
	warning=cursor.fetchall()
	for x in warning:
		y=x[0]
	warning=y
	data = {
		
		'title': title,
		'updatedate': updatedate,
		'critical': critical,
		'major':major,
		'minor':minor,
		'warning':warning,
		}
	return render_to_response("fault_list.html", data)

##### VM creation&deletion
def creation_list_data(request):
	from django.db import connection, transaction
	sql="SELECT * from vm_creation where DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= str_to_date(createdtime,'%m/%d/%Y %h:%i:%s %p') order by str_to_date(createdtime,'%m/%d/%Y %h:%i:%s %p') desc "
	cursor = connection.cursor()
	cursor.execute(sql)
	instance = cursor.fetchall();
	######convert data to json
	card=[]
	for obj in instance:
		dic={}
		dic['createdtime']=obj[0]
		dic['username']=obj[1]
		dic['details']=obj[2]
		dic['tag']=obj[3]
		dic['timestamp']=obj[4]
		card.append(dic)
	data = {'records':card}
	return JsonResponse(data)

def creation_list(request):
	import json
	from django.db import connection, transaction
	title='vm creation list'
	sql="select timestamp from vm_creation where (timestamp = (select max(timestamp) from vm_creation))"
	cursor = connection.cursor()
	cursor.execute(sql)
	updatedate=cursor.fetchall()
	for x in updatedate:
		y=x[0]	
    
	updatedate=y
	
	sql1="select count(*) from vm_creation where DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= str_to_date(createdtime,'%m/%d/%Y %h:%i:%s %p') and tag = 'created'"
	sql2="select count(*) from vm_creation where DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= str_to_date(createdtime,'%m/%d/%Y %h:%i:%s %p') and tag = 'removed'"
	cursor.execute(sql1)
	created=cursor.fetchall()
	for x in created:
		y=x[0]
	created=y
	
	cursor.execute(sql2)
	removed=cursor.fetchall()
	for x in removed:
		y=x[0]
	removed=y
	
	
	data = {
		
		'title': title,
		'updatedate': updatedate,
		'created': created,
		'removed': removed,
		}
	return render_to_response("creation_list.html", data)


##### operation event
def event_list_data(request):
	from django.db import connection, transaction
	sql="SELECT * from vm_event where DATE_SUB(CURDATE(), INTERVAL 5 DAY) <= str_to_date(createdtime,'%m/%d/%Y %h:%i:%s %p') order by str_to_date(createdtime,'%m/%d/%Y %h:%i:%s %p') desc "
	cursor = connection.cursor()
	cursor.execute(sql)
	instance = cursor.fetchall();
	######convert data to json
	card=[]
	for obj in instance:
		dic={}
		dic['createdtime']=obj[0]
		dic['username']=obj[1]
		dic['details']=obj[2]
		card.append(dic)
	data = {'records':card}
	return JsonResponse(data)


def event_list(request):
	import json
	from django.db import connection, transaction
	title='opertation list'
	data = {
		'title': title,
		}
	return render_to_response("event_list.html", data)
