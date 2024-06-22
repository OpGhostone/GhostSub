import requests

def certspotter_enum(target):
    subdomains = []
    res = requests.get(f'https://api.certspotter.com/v1/issuances?domain={target}&include_subdomains=true&expand=dns_names').json()
    try:
        for i in res:
            for sub in i['dns_names']:
                if target in sub:
                    subdomains.append(sub)
                    if sub not in subdomains:
                        subdomains.append(sub)
    except:
        pass
    return subdomains