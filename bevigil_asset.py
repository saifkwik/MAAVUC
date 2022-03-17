import requests
import config
import time
# Getting APP assets from OSINT BeVigil API:
t1 = time.perf_counter()
# taking input of app_id:
app_id = input('Enter APP ID here (com.example.com) : ').lower().strip()


# retrieving assets from  OSINT API
def get_data(app_id):
    api_base_url = f'http://osint.bevigil.com/api/'
    endpoint_path = f'{app_id}/all-assets/'
    headers = {
        'X-Access-Token': config.api_key
    }

    endpoint = f'{api_base_url}{endpoint_path}'
    # print(endpoint)

    r = requests.get(endpoint, headers=headers)

    if r.status_code in range(200, 299):
        contents = r.json()
        # pprint.pprint(contents)
        data = contents.get('assets')
        return data


data = get_data(app_id)

try:
    hostnames = data.get('host')
except AttributeError as ae:
    print('Invalid App Id: ' + app_id)
    exit()

ip = data.get('IP Address disclosure')
if ip is None:
    ip = []
