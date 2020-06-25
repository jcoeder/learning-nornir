from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_get

nr = InitNornir(
    core={"num_workers": 100},
    inventory={
        "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
        "options": {
            "host_file": "hosts.yaml",
            "group_file": "groups.yaml"
        }
    }
)

results = nr.run(
    task=napalm_get, getters=["facts", "interfaces"]
)
print_result(results)