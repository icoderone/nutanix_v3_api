import json
from amnesia import nutanixApiv3


body = {
  "spec": {
    "description": "string",
    "resources": {
      "num_vcpus_per_socket": 2,
      "memory_size_mib": 4096,
      "disk_list": [
        {
          "device_properties": {
            "disk_address": {
              "adapter_type": "SCSI",
              "device_index": 1
            },
            "device_type": "DISK"
          },
          "disk_size_mib": 25258
        }
      ],
      "nic_list": [
        {
          "nic_type": "NORMAL_NIC",
          "subnet_reference": {
            "kind": "subnet",
            "uuid": "565784d2-7a68-4a16-a1bd-92473760f607"
          }
        }
      ]
    },
    "name": "nuran_v3api1",
    "cluster_reference": {
      "kind": "cluster",
      "uuid": "00052c80-729d-8705-0000-0000000051fa"
    }
  },
  "metadata": {
    "kind": "vm"
  }
}

def main():
    username = 'admin'
    password = 'Nutanix/1234'
    cluster_ip = '10.64.35.40'
    base_url = "https://%s:9440/api/nutanix/v3/" %cluster_ip
    api = nutanixApiv3(base_url, username, password)
    data = api.vm_create(body)
    if data.status_code != 202:
        print 'status code: %s' %data.status_code
    print 'Response data:\n%s' %data.text


if __name__ == '__main__':
    main()
