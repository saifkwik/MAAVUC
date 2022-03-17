import time
import dns.resolver
import requests
import bevigil_asset
import pprint
import concurrent.futures


# INTERNET DB SHODAN API:
def hosts_threat(x):
    api_base_url = f'https://internetdb.shodan.io/'
    endpoint_path = f'{x}'

    endpoint = f'{api_base_url}{endpoint_path}'

    r = requests.get(endpoint)

    if r.status_code in range(200, 299):
        contents = r.json()
        data = contents
        return data


# Function to Resolve DNS from Hostname:
def get_ip_from_hostname(single_host):
    try:
        _r = dns.resolver.resolve(single_host)
        _r.nameservers = ['8.8.8.8']
        for val in _r:
            y = (val.to_text())
            # y is the Ip we from this function
            return y

    except dns.resolver.NXDOMAIN as e:
        pass
    except dns.resolver.NoNameservers as q:
        pass
    except dns.resolver.LifetimeTimeout as p:
        pass
    except dns.resolver.NoAnswer as no:
        pass
    except dns.name.EmptyLabel as emp:
        pass


# appending direct IPs from app into result:
try:
    result = bevigil_asset.ip
    direct_ip = len(result)
except TypeError as t:
    result = []
    direct_ip = 0

print(bevigil_asset.hostnames)
print("Total Hostnames found in APP: " + str(len(bevigil_asset.hostnames)))
print(bevigil_asset.ip)
print('Direct IPs disclosed in app: ' + str(len(result)))

# Thread to make the Loop run faster:
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    f = {executor.submit(get_ip_from_hostname, h): h for h in bevigil_asset.hostnames}
    for future in concurrent.futures.as_completed(f):
        fut = f[future]
        if future.result() is not None:
            futures = future.result()
            result.append(futures)

result = list(set(result))
print('IPs found from Hostnames :' + str(len(result) - direct_ip))
print('Total Ip in APP = Disclosed IPs + IPs found from Hostnames :' + str(len(result)))
print(result)

# appending results found from InternetDB API of all IP to ip_result list
ip_result = []
count = 1
try:
    for threats in result:
        print(str(count) + '- ' + str(threats))
        ip_result.append(hosts_threat(threats))
        count += 1
except TypeError as te:
    pprint.pprint('No IPs found in this APP')

# Removing None Values from the list:
ip_result = list(filter(None, ip_result))

pprint.pprint('Information from Ips Found: ' + str(len(ip_result)))

t2 = time.perf_counter()
print(f'Time taken: {t2 - bevigil_asset.t1} seconds')
