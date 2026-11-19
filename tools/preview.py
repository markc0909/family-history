#!/usr/bin/env python3
"""Local preview with byte-range support for timestamped audio seeking."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re, shutil, os
ROOT=Path(__file__).resolve().parents[1]
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(ROOT),**kwargs)
 def send_head(self):
  self.byte_range=None
  path=self.translate_path(self.path)
  if self.headers.get('Range') and os.path.isfile(path):
   size=os.path.getsize(path);m=re.fullmatch(r'bytes=(\d*)-(\d*)',self.headers['Range'])
   if m:
    start=int(m[1]) if m[1] else max(0,size-int(m[2] or 0));end=min(size-1,int(m[2])) if m[1] and m[2] else size-1
    if start>=size or end<start:self.send_error(416);return None
    file=open(path,'rb');file.seek(start);self.byte_range=(start,end)
    self.send_response(206);self.send_header('Content-Type',self.guess_type(path));self.send_header('Accept-Ranges','bytes');self.send_header('Content-Range',f'bytes {start}-{end}/{size}');self.send_header('Content-Length',str(end-start+1));self.end_headers();return file
  return super().send_head()
 def end_headers(self):self.send_header('Accept-Ranges','bytes');super().end_headers()
 def copyfile(self,source,outputfile):
  if not self.byte_range:return super().copyfile(source,outputfile)
  left=self.byte_range[1]-self.byte_range[0]+1
  while left:
   data=source.read(min(left,64*1024))
   if not data:break
   outputfile.write(data);left-=len(data)
print('Family archive preview: http://127.0.0.1:8766',flush=True)
ThreadingHTTPServer(('127.0.0.1',8766),Handler).serve_forever()
