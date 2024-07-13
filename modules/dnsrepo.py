import requests
from bs4 import BeautifulSoup

def dnsrepo_enum(target):
    subdomains = []
    try:
        res = requests.get(f'https://dnsrepo.noc.org/?search={target}').content
        soup = BeautifulSoup(res, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            if target.split('.')[0] in link.get('href') and link.get('href').split('=')[1][:-1] not in subdomains:
                subdomains.append(link.get('href').split('=')[1][:-1])
    except Exception as error: return [f'[!] dnsrepo Exception: {error}']
    return subdomains
