import argparse
from modules.anubis import anubis_enum
from modules.censys import censys_enum
from modules.certspotter import certspotter_enum
from modules.chaos import chaos_enum
from modules.dnsrepo import dnsrepo_enum
from modules.netlasenum import netlas_enum
from modules.crtsh import crtsh_enum
from modules.binaryedge import binaryedge_enum
from modules.virustotal import virustotal_enum
from modules.facebook import facebook_enum

# arguments
parser = argparse.ArgumentParser(prog="GhostSub", description="Subdomain enumeration tool with nothing special")
parser.add_argument('-d', help='target domain', required=True, dest='domain')
parser.add_argument('-s', action="store_true", help='only shows subdomains', dest='silent')
parser.add_argument('-o', action="store_true", help='shows where the subdomain was found', dest='origin')
parser.add_argument('-x', help='exclude unwanted sources', dest='exclude')
args = parser.parse_args()
enums = {
    'anubis': anubis_enum,
    'censys': censys_enum,
    'certspotter': certspotter_enum,
    'chaos': chaos_enum,
    'dnsrepo': dnsrepo_enum,
    'netlas': netlas_enum,
    'crtsh': crtsh_enum,
    'binaryedge': binaryedge_enum,
    'virustotal': virustotal_enum,
    'facebook': facebook_enum
}
if args.exclude: 
    exclude = args.exclude.split(',')
    for enum in exclude: enums.pop(enum)

# show origin
if args.origin:
    for enum in enums:
        for sub in enums[enum](args.domain):
            print(f'[{enum}]', sub)
    quit()

# menu
if not args.silent:
    print(f'''
  _______            __  ____     __
 / ___/ /  ___  ___ / /_/ __/_ __/ /
/ (_ / _ \/ _ \(_-</ __/\ \/ // / _ \\
\___/_//_/\___/___/\__/___/\_,_/_.__/

[>] Subdomain enumeration tool with nothing special
[>] github.com/opghostone/ghostsub

[!] Target -> {args.domain}
''')

subdomains = []
for enum in enums:
    for sub in enums[enum](args.domain):
        if sub not in subdomains: 
            if '[!]' not in sub: subdomains.append(sub)
            if not ('[!]' in sub and args.silent): print(sub)

if not args.silent: print(f'\n[!] {len(subdomains)} subdomains discovered')
