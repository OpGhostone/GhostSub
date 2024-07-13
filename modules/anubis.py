import requests

def anubis_enum(target):
    subdomains = []
    try:
        res = requests.get(f'https://jonlu.ca/anubis/subdomains/{target}').json()
        for i in res:
            subdomains.append(i)
    except Exception as error: return [f'[!] anubis Exception: {error}']
    return subdomains
