### yaml inventory example

```yaml
---
dietpi:
  vars:
    ansible_user: root
  hosts:
    dietpi1.example.com:
      ansible_ssh_host: 10.0.0.7
    dietpi2.example.com:
      ansible_ssh_host: 10.0.0.6
  children:
    group1:
      hosts:
        dietpi1.example.com:
    group2:
      hosts:
        dietpi2.example.com:
    ddns:
      children:
        group1:
        group2:
```


### datasource ddns.yml
```yaml
ddns:
  - dns_name: dietpi1
    domain: example.com
    target:
      - name: dietpi1.example.com
  - dns_name: dietpi2
    domain: example.com
    target:
      - name: dietpi2.example.com
```
