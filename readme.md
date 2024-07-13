# GhostSub
Subdomain enumeration tool with nothing special.
## Passive Sources
- chaos.projectdiscovery.io
- crt.sh
- api.certspotter.com
- virustotal
- developers.facebook.com/docs/certificate-transparency
- jonlu.ca/anubis
- dnsrepo.noc.org
- netlas.io
- binaryedge.io
- censys
## Usage
```bash
Subdomain enumeration tool with nothing special

options:
  -h, --help  show this help message and exit
  -d DOMAIN   target domain
  -s          only shows subdomains
  -o          shows where the subdomain was found
  -x EXCLUDE  exclude unwanted sources
```
```bash
# Exclude all sources
python3 ghostsub.py -d DOMAIN -x anubis,censys,certspotter,chaos,dnsrepo,netlas,crtsh,binaryedge,virustotal,facebook

# Only-subdomains output
python3 ghostsub.py -d DOMAIN -s

# Show sources
python3 ghostsub.py -d DOMAIN -o
```

## API Keys
just paste your API keys into the apikeys.json file as in the example:
```json
{
    "chaos": "chaosKey",
    "censys_id": "censysId",
    "censys_secret": "censysSecret",
    "netlas": "netlasKey",
    "binaryedge": "binaryedgeKey",
    "virustotal": "virustotalKey",
    "facebook": "facebookToken"
}
```