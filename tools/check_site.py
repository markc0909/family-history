"""Check generated pages, anchor targets, local files and catalogue references."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json,sys
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.links=[];self.errors=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:
   if a['id'] in self.ids:self.errors.append('Duplicate id: '+a['id'])
   self.ids.add(a['id'])
  for key in ('href','src'):
   if a.get(key):self.links.append(a[key])
  if tag=='img' and 'alt' not in a:self.errors.append('Image missing alt')
pages={}
for f in ROOT.glob('*.html'):
 p=Page();p.feed(f.read_text());pages[f.resolve()]=p
errors=[];links=0
for f,p in pages.items():
 errors.extend(f.name+': '+e for e in p.errors)
 for link in p.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=(f.parent/unquote(u.path)).resolve() if u.path else f
  if not target.is_relative_to(ROOT):errors.append(f'{f.name}: local link escapes site: {link}');continue
  if not target.exists():errors.append(f'{f.name}: missing file: {link}');continue
  links+=1
  if u.fragment and target.suffix=='.html' and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append(f'{f.name}: missing anchor: {link}')
for data in ('sources','people','timeline','branches','recordings','passages','asset-register'):
 json.loads((ROOT/'data'/f'{data}.json').read_text())
for f in ROOT.rglob('*'):
 if '.git' in f.relative_to(ROOT).parts:continue
 if f.is_file() and f.stat().st_size>100*1024*1024:errors.append(f'{f.relative_to(ROOT)} exceeds GitHub 100 MiB individual-file limit')
print(f'Checked {len(pages)} pages and {links} local links.')
if errors:
 print('\n'.join(errors));sys.exit(1)
print('All local files, image descriptions and anchor targets passed.')
