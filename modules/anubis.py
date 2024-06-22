import requests

def anubis_enum(target):
    subdomains = []
    res = requests.get(f'https://jonlu.ca/anubis/subdomains/{target}').json()
    for i in res:
        subdomains.append(i)
    return subdomains
