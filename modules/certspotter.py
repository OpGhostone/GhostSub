import requests

def certspotter_enum(target):
    subdomains = []
    res = requests.get(f'https://api.certspotter.com/v1/issuances?domain={target}&include_subdomains=true&expand=dns_names').json()
    try:
        for i in res:
            for sub in i['dns_names']:
                if '*' in sub: sub = sub[2:]
                if sub not in subdomains and target in sub:
                    subdomains.append(sub)
    except Exception as error: return [f'[!] certspotter Exception: {error}']
    return subdomains
