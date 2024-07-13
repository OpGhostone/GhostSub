import requests
import json

def virustotal_enum(target):
    subdomains = []
    try:
        f = open('apikeys.json', 'r')
        virustotal_key = json.load(f)['virustotal']
        res = requests.get(f'https://www.virustotal.com/api/v3/domains/{target}/subdomains?limit=1000', 
        headers={'x-apikey':virustotal_key}).json()
        for obj in res['data']:
            subdomains.append(obj['id'])
        while len(res['links']) > 1:
            res = requests.get(res['links']['next'], headers={'x-apikey':virustotal_key}).json()
            for obj in res['data']:
                if obj['id'] not in subdomains: subdomains.append(obj['id'])
    except Exception as error: return [f'[!] virustotal Exception: {error}']
    return subdomains
