import json
from amnesia import nutanixApiv3


body = {
  "spec": {
    "cluster_reference": {
      "kind": "cluster",
      "name": "Prolix",
      "uuid": "00052c80-729d-8705-0000-0000000051fa"
    },
    "description": "string",
    "resources": {
      "vnuma_config": {
        "num_vnuma_nodes": 0
      },
      "nic_list": [
        {
          "ip_endpoint_list": [],
          "nic_type": "NORMAL_NIC",
          "subnet_reference": {
            "kind": "subnet",
            "name": "vlan25",
            "uuid": "565784d2-7a68-4a16-a1bd-92473760f607"
          },
          "uuid": "39aacea6-f5b9-4be6-8a0b-27e9db7fee91",
          "mac_address": "50:6b:8d:b2:b2:33"
        }
      ],
      "num_vcpus_per_socket": 2,
      "num_sockets": 1,
      "gpu_list": [],
      "memory_size_mib": 4096,
      "power_state": "OFF",
      "hardware_clock_timezone": "UTC",
      "power_state_mechanism": {
        "mechanism": "HARD"
      },
      "vga_console_enabled": True,
      "disk_list": [
        {
          "device_properties": {
            "disk_address": {
              "device_index": 1,
              "adapter_type": "SCSI"
            },
            "device_type": "DISK"
          },
          "uuid": "9f053c80-3e7f-4964-88ba-835920e0cdfb",
          "disk_size_bytes": 26484932608,
          "disk_size_mib": 25258
        },
        {
          "device_properties": {
            "disk_address": {
              "device_index": 2,
              "adapter_type": "SCSI"
            },
            "device_type": "DISK"
          },
          "disk_size_mib": 15258
        },
        {
          "device_properties": {
            "disk_address": {
              "device_index": 0,
              "adapter_type": "IDE"
            },
            "device_type": "CDROM"
          }
        }
      ]
    },
    "name": "nuran_v3api1"
  },
  "api_version": "3.1",
  "metadata": {
    "last_update_time": "2018-11-03T01:01:51Z",
    "kind": "vm",
    "uuid": "1dfe6d6c-428d-4d71-8a72-7152734328a6",
    "project_reference": {
      "kind": "project",
      "name": "default",
      "uuid": "f86d420a-f601-4ca9-9135-082bc38554c6"
    },
    "spec_version": 1,
    "creation_time": "2018-11-02T20:47:12Z",
    "owner_reference": {
      "kind": "user",
      "uuid": "00000000-0000-0000-0000-000000000000",
      "name": "admin"
    },
    "categories": {}
  }
}

def main():
    username = 'admin'
    password = 'Nutanix/1234'
    cluster_ip = '10.64.35.40'
    base_url = "https://%s:9440/api/nutanix/v3/" %cluster_ip
    vm_uuid = "1dfe6d6c-428d-4d71-8a72-7152734328a6"
    api = nutanixApiv3(base_url, username, password)
    data = api.vm_update(vm_uuid, body)
    if data.status_code != 202:
        print 'status code: %s' %data.status_code
    print 'Response data:\n%s' %data.text


if __name__ == '__main__':
    main()
