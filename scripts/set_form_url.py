#!/usr/bin/env python3
from pathlib import Path
import sys
if len(sys.argv) != 2:
    print("Usage: python3 scripts/set_form_url.py 'https://forms.gle/...'", file=sys.stderr)
    raise SystemExit(2)
url = sys.argv[1].strip()
if not (url.startswith('https://forms.gle/') or url.startswith('https://docs.google.com/forms/')):
    print('Warning: URL does not look like a Google Form URL', file=sys.stderr)
base = Path(__file__).resolve().parents[1]
for rel in ['index.html','netlify.toml','vercel.json','_redirects']:
    p = base / rel
    s = p.read_text(encoding='utf-8')
    s = s.replace('FORM_URL_PLACEHOLDER', url)
    p.write_text(s, encoding='utf-8')
print('Updated form URL in public-site files')
