from nornir import InitNornir

nr = InitNornir('config.yaml')
print(nr.inventory.groups)
print(nr.inventory.groups['csr_routers'])
print(nr.inventory.groups['mx_routers'].data['snmp_community'])
print(nr.inventory.groups['mx_routers'].platform)
print(nr.inventory.groups['site1'].data)
