import requests

def chaos_enum(target):
    subdomains = []
    f = open('apikeys.txt', 'r')
    for apikey in f.read().split('\n'):
        if 'chaos' in apikey:
            chaoskey = apikey.split('=')[1]
    try:
        res = requests.get(f'https://dns.projectdiscovery.io/dns/{target}/subdomains', headers={'Authorization':chaoskey}).json()['subdomains']
        for i in res:
            subdomains.append(f'{i}.{target}')
            if f'{i}.{target}' not in subdomains:
                subdomains.append(f'{i}.{target}')
    except:
        pass
    return subdomains