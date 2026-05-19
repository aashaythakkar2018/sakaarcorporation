import os
import urllib.request
import urllib.error
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

os.makedirs('assets/logos', exist_ok=True)

companies = {
    'ongc': ('ONGC', 'ongcindia.com'),
    'adani': ('Adani Ports', 'adaniports.com'),
    'ultratech': ('UltraTech', 'ultratechcement.com'),
    'lt': ('Larsen & Toubro', 'larsentoubro.com'),
    'amns': ('AM/NS India', 'amns.in'),
    'jcb': ('JCB', 'jcb.com'),
    'batliboi': ('Batliboi', 'batliboi.com'),
    'avvl': ('AWL Agri Business', 'adaniwilmar.com'),
    'citizen': ('Citizen', 'citizen.co.in'),
    'weavetech': ('Weavetech', 'weavetech.com'),
    'bindal': ('Bindal', 'bindalmill.com'),
    'ctx': ('CTX Lifesciences', 'ctxls.com'),
    'ascolite': ('Ascolite', 'ascolite.in'),
    'mahavir': ('Mahavir Synthesis', 'mahavirsynthesis.com'),
    'rbl': ('Ranjit Buildcon', 'ranjitbuildcon.in')
}

for key, (name, domain) in companies.items():
    filepath = f"assets/logos/{key}.png"
    clearbit_url = f"https://logo.clearbit.com/{domain}"
    placehold_url = f"https://placehold.co/400x200/ffffff/333333.png?text={urllib.parse.quote(name)}"
    
    try:
        req = urllib.request.Request(clearbit_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Downloaded {name} from clearbit.")
    except urllib.error.HTTPError:
        print(f"Clearbit failed for {name}, using placehold.")
        req = urllib.request.Request(placehold_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
    except Exception as e:
        print(f"Error for {name}: {e}")

