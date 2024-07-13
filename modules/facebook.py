import requests
import json

def facebook_enum(target):
    subdomains = []
    try:
        f = open('apikeys.json', 'r')
        facebook_key = json.load(f)['facebook']
        res  = requests.get(f'https://graph.facebook.com/certificates?query={target}&access_token={facebook_key}&fields=domains&limit=2000').json()
        for cert in res['data']:
            for sub in cert['domains']:
                if '*' in sub: sub = sub[2:]
                if target in sub and sub not in subdomains: subdomains.append(sub)
        while 'next' in res['paging']:
            res = requests.get(res['paging']['next']).json()
            for cert in res['data']:
                for sub in cert['domains']:
                    if '*' in sub: sub = sub[2:]
                    if target in sub and sub not in subdomains: subdomains.append(sub)
    except Exception as error: return [f'[!] facebook Exception: {error}']
    return subdomains
