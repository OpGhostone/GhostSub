import requests
from bs4 import BeautifulSoup

def crtsh_enum(target):
    subdomains = []
    try:
        res = requests.get(f'https://crt.sh/?q={target}')
        if not res.ok: return subdomains
        else: res = res.content
        soup = BeautifulSoup(res, "html.parser")
        for row in soup.body.find_all('table')[1].tr.td.table.find_all('tr')[1:]:
            subs = row.find_all('td')[5].contents
            for sub in subs:
                if '*' in sub: sub = sub[2:]
                if sub not in subdomains and target in sub and '@' not in sub and '\\' not in sub and ' ' not in sub:
                    subdomains.append(sub)
    except Exception as error: return [f'[!] crt.sh Exception: {error}']
    return subdomains
