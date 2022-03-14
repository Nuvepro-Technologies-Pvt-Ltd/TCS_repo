import sys 
import json
import base64
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient

    
def start_tests(credentials,subscriptionId,args):
    x=args.decode('utf-8')
    b = base64.b64decode(args).decode() 
    inputs = json.loads(b)
    
    vm_name = inputs["arg1"]
    
    totalTests=0
    
    totalPass=0
    
    

    totalTests +=1
    
    count =test1_check_vm_name(credentials,subscriptionId,vm_name)
    if count == None:
        count = 0
    totalPass += count
    

    result =  {"Total":totalTests ,"Passed":totalPass}
    
    jsonStr = json.dumps(result)
    print(jsonStr)
    
    return jsonStr
    
def test1_check_vm_name(credentials,subscriptionId,vm_name):
        
        try:
            
            client = ComputeManagementClient(credentials, subscriptionId)
            vms = client.virtual_machines.list_all()
            for vm in vms:
                if vm.name == vm_name:
                    print(vm.name)
                    return 1
                else:
                    return 0                   

        except Exception as e:
        
            return 0

