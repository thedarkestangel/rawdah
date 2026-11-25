#!/usr/bin/env python3
"""Bygger testversjonene av Rawdah fra index.html.
Bruk: python3 tools/build_tests.py  (kjør fra repo-roten etter hver endring i index.html)

- Kahwa 7142: kort smakebit (15–20 min) med testrull, tidsmaskin og mannen med rosinhodet.
- Jabal: den fulle appen i 7 spilldager (en dag = en dag med fullført vers). Ibrahim-versjonen har utviklerpanel.
Hver tester får egen mappe, egen lagring og egen logo per versjon."""
import json, os, subprocess, time, shutil
FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSfhQfSX3VhlaC9TOgYXpMutZIooLstS9pAyjfBrbaF47s3lwQ/viewform'
TESTERS = [
    {'mode': 'kahwa', 'name': 'saleem', 'who': 'Saleem', 'form': FORM, 'notes': True},
    {'mode': 'jabal', 'name': 'haroon', 'who': 'Haroon', 'form': FORM},
    {'mode': 'jabal', 'name': 'najaat', 'who': 'Najaat', 'form': FORM},
    {'mode': 'jabal', 'name': 'sadia', 'who': 'Sadia', 'form': FORM},
    {'mode': 'jabal', 'name': 'luqman', 'who': 'Luqman', 'form': FORM},
    {'mode': 'jabal', 'name': 'noxiphone', 'who': 'noxp (iPhone)', 'form': FORM, 'notes': True, 'skip': True},
    {'mode': 'jabal', 'name': 'noxpixl', 'who': 'noxp (Pixel)', 'form': FORM, 'notes': True, 'skip': True},
    {'mode': 'jabal', 'name': 'ibrahim', 'who': 'Ibrahim', 'form': None, 'dev': True},
]
src = open('index.html', encoding='utf-8').read()
try:
    rev = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], text=True).strip()
except Exception:
    rev = '?'
BUILD = 'bygg ' + time.strftime('%d.%m.%Y') + ' · ' + rev
NAMES = {'kahwa': ('Rawdah Kahwa 7142', 'Rawdah Kahwa', 'kahwatest-', '#140a04'), 'jabal': ('Rawdah Jabal', 'Rawdah Jabal', 'jabal-', '#08121a')}
for t in TESTERS:
    mode, name = t['mode'], t['name']
    title, short, prefix, bg = NAMES[mode]
    cfg = {k: v for k, v in t.items() if k != 'mode'}
    cfg['build'] = BUILD
    var = 'KAHWA' if mode == 'kahwa' else 'JABAL'
    shift = (('kahwa_' if mode == 'kahwa' else 'jabal_') + name + '_off')
    head = ('<script>window.' + var + '=' + json.dumps(cfg, ensure_ascii=False) + ';'
            '(function(){var o=+(localStorage.getItem("' + shift + '")||0);if(!o)return;var D=Date,sh=o*864e5;'
            'class F extends D{constructor(...a){if(a.length)super(...a);else super(D.now()+sh);}static now(){return D.now()+sh;}}'
            'window.Date=F;})();</script>')
    out = src.replace('<head>', '<head>\n' + head, 1)
    out = out.replace('href="icon-180.png"', 'href="icon-180.png?v=' + mode + '"')
    out = out.replace('<title>Rawdah</title>', '<title>' + title + '</title>')
    out = out.replace('content="Rawdah">', 'content="' + short + '">')
    d = prefix + name
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(out)
    man = {"name": title, "short_name": short, "start_url": "./", "scope": "./", "display": "standalone",
           "background_color": "#0b0920", "theme_color": "#0b0920",
           "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
                     {"src": "icon-maskable-192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable"}, {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
    json.dump(man, open(os.path.join(d, 'manifest.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for f in os.listdir('icons/' + mode):
        if f.endswith('.png'):
            shutil.copy(os.path.join('icons', mode, f), os.path.join(d, f))
    print('bygget', d)
