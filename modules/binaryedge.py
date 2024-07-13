import requests
from math import ceil
import json

def binaryedge_enum(target):
    subdomains = []
    try:
        api_limit = 1
        f = open('apikeys.json', 'r')
        binarykey = json.load(f)['binaryedge']
        res = requests.get(f'https://api.binaryedge.io/v2/query/domains/subdomain/{target}?page={api_limit}', 
        headers={'X-Key':binarykey}).json()
        for sub in res['events']: subdomains.append(sub)
        if res['total'] > res['pagesize']:
            while api_limit < 250 and res['page'] < ceil(res['total'] / res['pagesize']):
                api_limit += 1
                res = requests.get(f'https://api.binaryedge.io/v2/query/domains/subdomain/{target}?page={api_limit}', 
                headers={'X-Key':binarykey})
                if res.ok: res = res.json()
                else: return subdomains
                for sub in res['events']:
                    if sub not in subdomains: subdomains.append(sub)
    except Exception as error: return [f'[!] binaryedge Exception: {error}']
    return subdomains
