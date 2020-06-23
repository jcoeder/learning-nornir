import nornir

nr = nornir.InitNornir('config.yaml')
result = nr.run(netmiko_send_command, command_string='show ip interface brief')
print_result(result)
