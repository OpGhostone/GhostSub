import argparse
from modules.anubis import anubis_enum
from modules.censys import censys_enum
from modules.certspotter import certspotter_enum
from modules.chaos import chaos_enum
from modules.dnsrepo import dnsrepo_enum

# otimizar o código
# renomear as variaveis
# fazer filtragens (como o wildcard * e o símbolo de @ pra emails que pertencem ao dominio alvo)

# crt.sh
# api.c99.nl/
# dnsdumpster.com
# virustotal
# developers.facebook.com/docs/certificate-transparency
# ui.ctsearch.entrust.com/ui/ctsearchui
# rapiddns.io/subdomain
# netlas.io
# dnsspy.io
# app.binaryedge.io/services/domains

parser = argparse.ArgumentParser(prog="GhostSub", description="Subdomain enumeration tool with nothing special")
parser.add_argument('-d', '--domain')
parser.add_argument('-s', '--silent', action="store_true")
parser.add_argument('-o', '--origin', action="store_true")
args = parser.parse_args()

# show origin
if args.origin:
    for sub in anubis_enum(args.domain):
        print('[anubis]', sub)
    for sub in dnsrepo_enum(args.domain):
        print('[dnsrepo]', sub)
    for sub in chaos_enum(args.domain):
        print('[chaos]', sub)
    for sub in certspotter_enum(args.domain):
        print('[certspotter]', sub)
    for sub in censys_enum(args.domain):
        print('[censys]', sub)
    quit()

subdomains = set(anubis_enum(args.domain) + certspotter_enum(args.domain) + chaos_enum(args.domain) + dnsrepo_enum(args.domain) + censys_enum(args.domain))

# menu
if args.silent:
    for subdomain in subdomains:
        print(subdomain)

else:
    print(f'''
  _______            __  ____     __
 / ___/ /  ___  ___ / /_/ __/_ __/ /
/ (_ / _ \/ _ \(_-</ __/\ \/ // / _ \\
\___/_//_/\___/___/\__/___/\_,_/_.__/

[>] Subdomain enumeration tool with nothing special
[>] github.com/opghostone/ghostsub

[!] Target -> {args.domain}
''')

    for subdomain in subdomains:
        print(subdomain)

    print(f'\n[!] {len(subdomains)} subdomains discovered')
