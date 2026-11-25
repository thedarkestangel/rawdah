#!/usr/bin/env python3
"""Bygger testversjonen «Rawdah Kahwa 7142» fra index.html.
Bruk: python3 tools/build_kahwa.py  (kjør fra repo-roten etter hver endring i index.html)
Hver tester får egen mappe, egen lagring og egen tidsforskyvning."""
import json, os, subprocess, time, shutil
TESTERS = {
    'saleem': {'who': 'Saleem', 'form': 'https://docs.google.com/forms/d/e/1FAIpQLSfhQfSX3VhlaC9TOgYXpMutZIooLstS9pAyjfBrbaF47s3lwQ/viewform'},
}
src = open('index.html', encoding='utf-8').read()
try:
    rev = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], text=True).strip()
except Exception:
    rev = '?'
BUILD = 'bygg ' + time.strftime('%d.%m.%Y') + ' · ' + rev
for name, cfg in TESTERS.items():
    cfg = dict(cfg, name=name, build=BUILD)
    head = ('<script>window.KAHWA=' + json.dumps(cfg, ensure_ascii=False) + ';'
            '(function(){var o=+(localStorage.getItem("kahwa_' + name + '_off")||0);if(!o)return;var D=Date,sh=o*864e5;'
            'class F extends D{constructor(...a){if(a.length)super(...a);else super(D.now()+sh);}static now(){return D.now()+sh;}}'
            'window.Date=F;})();</script>')
    out = src.replace('<head>', '<head>\n' + head, 1)
    out = out.replace('href="icon-180.png"', 'href="icon-180.png?k=1"')
    out = out.replace('<title>Rawdah</title>', '<title>Rawdah Kahwa 7142</title>')
    out = out.replace('content="Rawdah">', 'content="Rawdah Kahwa">')
    d = 'kahwatest-' + name
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(out)
    man = {"name": "Rawdah Kahwa 7142", "short_name": "Rawdah Kahwa", "start_url": "./", "scope": "./", "display": "standalone",
           "background_color": "#0b0920", "theme_color": "#0b0920",
           "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
                     {"src": "icon-maskable-192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable"}, {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
    json.dump(man, open(os.path.join(d, 'manifest.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for f in os.listdir('icons/kahwa'):
        if f.endswith('.png'): shutil.copy(os.path.join('icons/kahwa', f), os.path.join(d, f))
    print('bygget', d)
