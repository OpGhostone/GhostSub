import requests
import json

def chaos_enum(target):
    subdomains = []
    try:
        f = open('apikeys.json', 'r')
        chaoskey = json.load(f)['chaos']
        res = requests.get(f'https://dns.projectdiscovery.io/dns/{target}/subdomains', 
        headers={'Authorization':chaoskey}).json()['subdomains']
        for i in res:
            if ('*' in i or '%2a' in i) and len(i) > 2: i = i[2:]
            if f'{i}.{target}' not in subdomains and '*' not in i and '%2a' not in i:
                subdomains.append(f'{i}.{target}')
    except Exception as error: return [f'[!] chaos Exception: {error}']
    return subdomains
