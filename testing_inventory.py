from nornir import InitNornir

nr = InitNornir('config.yaml')
print(nr.inventory.hosts)
print(nr.inventory.hosts['csr1'])
print(nr.inventory.hosts['csr1'].hostname)
print(nr.inventory.hosts['csr1'].username)
print(nr.inventory.hosts['csr1'].password)

