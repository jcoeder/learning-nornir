from nornir import InitNornir
nr = InitNornir(config_file="config.yaml")

print(nr.filter(site='site1').inventory.hosts.keys())

print(nr.filter(site='site1', platform='ios').inventory.hosts.keys())

print(nr.inventory.children_of_group('site1'))
