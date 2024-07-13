import requests
import base64
import json

def censys_enum(target):
    subdomains = []
    try:
        api_limit = 1
        f = open('apikeys.json', 'r')
        keys = json.load(f)
        censys_id = keys['censys_id']
        censys_secret = keys['censys_secret']
        api_credential = base64.b64encode(f'{censys_id}:{censys_secret}'.encode('ascii')).decode('ascii')
        res = requests.get(
            f'https://search.censys.io/api/v2/certificates/search?q={target}&per_page=100', 
            headers={
                'Accept':'application/json', 
                'Authorization':f'Basic {api_credential}'
            }).json()
        extract_sub(res, subdomains, target)
        while api_limit < 10:
            next = res['result']['links']['next']
            res = requests.get(
            f'https://search.censys.io/api/v2/certificates/search?q={target}&per_page=100&cursor={next}', 
            headers={
                'Accept':'application/json', 
                'Authorization':f'Basic {api_credential}'
            }).json()
            extract_sub(res, subdomains, target)
            if len(next) == 0: break
            api_limit += 1
    except Exception as error: return [f'[!] censys Exception: {error}']
    return subdomains


def extract_sub(res, subdomains, target):
    for cert in res['result']['hits']:
        for i in cert['parsed']['subject_dn'].split(','):
            for sub in i.split('='):
                if '*' in sub: sub = sub[2:]
                if target in sub and sub not in subdomains and '@' not in sub and ' ' not in sub:
                    subdomains.append(sub)
        for sub in cert['names']:
            if '*' in sub: sub = sub[2:]
            if target in sub and sub not in subdomains:
                subdomains.append(sub)
