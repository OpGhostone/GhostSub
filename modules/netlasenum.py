import netlas
import json

def netlas_enum(target):
    subdomains = []
    try:
        f = open('apikeys.json', 'r')
        netlas_key = json.load(f)['netlas']
        netlas_connection = netlas.Netlas(api_key=netlas_key)
        for resp in netlas_connection.download(
            query=f'domain:*.{target}', 
            datatype='domain',
            fields='domain',
            size=200
        ):
            response = json.loads(resp.decode('utf-8'))
            subdomains.append(response['data']['domain'])
    except Exception as error: return [f'[!] netlas Exception: {error}'] 
    return subdomains
