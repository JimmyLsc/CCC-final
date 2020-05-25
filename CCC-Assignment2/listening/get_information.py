import psutil
import requests
import listening_information
import time

host = listening_information.frontend_host
url_root = 'http://' + host + '/api/information/get_info?'

while True:
    instance_num = listening_information.instance_number
    cpu_num = psutil.cpu_count()
    storage_usage = psutil.virtual_memory().percent
    cpu_usage = psutil.cpu_percent(None)
    disk_usage = psutil.disk_usage('/').percent

    request_information = 'instance_num={}&cpu_num={}&storage_usage={}&cpu_usage={}&disk_usage={}'\
        .format(instance_num, cpu_num, storage_usage, cpu_usage, disk_usage)

    requests.get(url_root + request_information)

    time.sleep(10)