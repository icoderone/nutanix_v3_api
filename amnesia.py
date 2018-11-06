import json, requests


class nutanixApiv3(object):
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password

    def vm_create(self, body):
    	'''required params in body:
            {memory_mb, name, num_vcpus ,cluster_reference{kind, uuid}, metadata{"kind": "vm"}}
        '''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.post(self.base_url + 'vms', json=body, verify=False)
        return data

    def vm_update(self, vm_uuid, body):
    	'''required params in body:
            {memory_mb, name, num_vcpus ,cluster_reference{kind, uuid},  metadata{"kind": "vm", "spec_version"}, "hardware_clock_timezone"}
        '''
        requests.packages.urllib3.disable_warnings()
        s = requests.Session()
        s.auth = (self.username, self.password)
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        data = s.put(self.base_url + 'vms/%s' %vm_uuid, json=body, verify=False)
        return data