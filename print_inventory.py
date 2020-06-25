from nornir import InitNornir
nr = InitNornir(config_file="config.yaml")

print(nr.inventory.hosts)
print(nr.inventory.groups)
print(nr.inventory.hosts["csr1"])
host = nr.inventory.hosts["csr1"]
print(host.keys())