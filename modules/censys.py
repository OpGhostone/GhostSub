import requests
import base64

def censys_enum(target):
    subdomains = []
    api_limit = 1
    f = open('apikeys.txt', 'r')
    for apikey in f.read().split('\n'):
        if 'censys_id' in apikey:
            censys_id = apikey.split('=')[1]
        if 'censys_secret' in apikey:
            censys_secret = apikey.split('=')[1]
    api_credential = base64.b64encode(f'{censys_id}:{censys_secret}'.encode('ascii')).decode('ascii')
    res = requests.get(
        f'https://search.censys.io/api/v2/certificates/search?q={target}&per_page=100', 
        headers={
            'Accept':'application/json', 
            'Authorization':f'Basic {api_credential}'
        }).json()
    while api_limit < 10:
        next = res['result']['links']['next']
        res = requests.get(
        f'https://search.censys.io/api/v2/certificates/search?q={target}&per_page=100&cursor={next}', 
        headers={
            'Accept':'application/json', 
            'Authorization':f'Basic {api_credential}'
        }).json()
        for cert in res['result']['hits']:
            for i in cert['parsed']['subject_dn'].split(','):
                for sub in i.split('='):
                    if target in sub and sub not in subdomains:
                        subdomains.append(sub)
            for sub in cert['names']:
                if target in sub and sub not in subdomains:
                    subdomains.append(sub)
        if len(next) == 0: break
        api_limit += 1
    return subdomains
