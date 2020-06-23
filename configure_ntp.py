from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file='config.yaml')

def configure_ntp_ios(task):
    banner = task.run(send_configs, configs=['ntp server ' + str(task.host['ntp_servers'][0])])

result = nr.run(task=configure_ntp_ios)
print_result(result)
